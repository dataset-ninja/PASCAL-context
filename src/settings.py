from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "PASCAL context"
PROJECT_NAME_FULL: str = "PASCAL context"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    url="http://host.robots.ox.ac.uk/pascal/VOC/voc2010/index.html#rights"
)
INDUSTRIES: List[Industry] = [Industry.GeneralDomain()]
CV_TASKS: List[CVTask] = [
    CVTask.SemanticSegmentation(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_YEAR: int = 2014
HOMEPAGE_URL: str = "https://www.cs.stanford.edu/~roozbeh/pascal-context/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 867584
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/pascal-context"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Training/validation data": "http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar",
    "Training/validation annotations": "https://www.cs.stanford.edu/~roozbeh/pascal-context/trainval.tar.gz",
    "Development kit code and documentation": "http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCdevkit_08-May-2010.tar",
    "PDF documentation": "http://host.robots.ox.ac.uk/pascal/VOC/voc2010/devkit_doc_08-May-2010.pdf",
    "HTML documentation": "http://host.robots.ox.ac.uk/pascal/VOC/voc2010/htmldoc/index.html",
    "Guidelines used for annotating the database (VOC2010)": "http://host.robots.ox.ac.uk/pascal/VOC/voc2010/guidelines.html",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://www.cs.stanford.edu/~roozbeh/pascal-context/mottaghi_et_al_cvpr14.pdf"
CITATION_URL: Optional[
    str
] = "https://www.cs.stanford.edu/~roozbeh/pascal-context/mottaghi_et_al_cvpr14.bib"
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Stanford University"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://cs.stanford.edu/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
