import os

import numpy as np
import supervisely as sly
from scipy.io import loadmat
from supervisely.io.fs import get_file_name
from tqdm import tqdm

BATCH_SIZE = 500


def create_meta(path_to_labels):
    labels_map = {}
    with open(path_to_labels, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(": ")
                labels_map[int(key)] = value

    obj_classes = []
    for label_name in labels_map.values():
        obj_classes.append(sly.ObjClass(label_name, sly.Bitmap))

    train_tag_meta = sly.TagMeta("train", sly.TagValueType.NONE)
    val_tag_meta = sly.TagMeta("val", sly.TagValueType.NONE)
    meta = sly.ProjectMeta(obj_classes=obj_classes, tag_metas=[train_tag_meta, val_tag_meta])
    return meta, labels_map


def create_trainval_sets(train_path, val_path):
    trainval_map = {}

    with open(train_path, "r") as file:
        train_names = [line.strip() for line in file.readlines()]
        trainval_map["train"] = train_names
    with open(val_path, "r") as file:
        val_names = [line.strip() for line in file.readlines()]
        trainval_map["val"] = val_names
    return trainval_map


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "../datasets-bot/datasets/PASCAL-context"
    labels_file_path = os.path.join(dataset_path, "labels.txt")
    train_file_path = os.path.join(dataset_path, "train.txt")
    val_file_path = os.path.join(dataset_path, "val.txt")

    meta, labels_map = create_meta(labels_file_path)
    trainval_map = create_trainval_sets(train_file_path, val_file_path)

    img_dir = os.path.join(dataset_path, "JPEGImages")
    ann_dir = os.path.join(dataset_path, "trainval")

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    api.project.update_meta(project.id, meta.to_json())
    for ds_name in trainval_map:
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
        names = trainval_map[ds_name]
        ann_paths = [os.path.join(ann_dir, f"{name}.mat") for name in names]
        img_paths = [os.path.join(img_dir, f"{name}.jpg") for name in names]

        tag = sly.Tag(meta.get_tag_meta(f"{ds_name}"))
        with tqdm(total=len(img_paths), desc=f"Processing images in {dataset.name}") as pbar:
            for img_paths_batch, ann_paths_batch in zip(
                sly.batched(img_paths, batch_size=BATCH_SIZE),
                sly.batched(ann_paths, batch_size=BATCH_SIZE),
            ):
                images_names = [get_file_name(img_path) for img_path in img_paths_batch]
                anns = []
                for ann_path in ann_paths_batch:
                    data = loadmat(ann_path)
                    image_data = data["LabelMap"]
                    unique_labels = np.unique(image_data)
                    labels = []
                    for label_id in unique_labels:
                        lbl_mask = image_data == label_id
                        label = sly.Label(
                            sly.Bitmap(lbl_mask), obj_class=meta.get_obj_class(labels_map[label_id])
                        )
                        labels.append(label)
                    ann = sly.Annotation(img_size=image_data.shape, labels=labels, img_tags=[tag])
                    anns.append(ann)

                img_infos = api.image.upload_paths(dataset.id, images_names, img_paths_batch)
                img_ids = [im_info.id for im_info in img_infos]
                api.annotation.upload_anns(img_ids, anns)
                pbar.update(len(img_paths_batch))

    return project
