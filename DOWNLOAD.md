Dataset **PASCAL Context** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/q/2/b4/KRHuANFh5K2lFOga0jBJ3EmSknj9wSI1xEtzQ4DGC5GcnEp9yXUzOys6V4CUkxQ0thnsqXLZgQOsGT24OkRQyGEk7cKD0vSLV4LooI8HXWJRERBKLzfgLDKPhLX6.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PASCAL Context', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Training/validation data](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar)
- [Training/validation annotations](https://www.cs.stanford.edu/~roozbeh/pascal-context/trainval.tar.gz)
- [Development kit code and documentation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCdevkit_08-May-2010.tar)
- [PDF documentation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/devkit_doc_08-May-2010.pdf)
- [HTML documentation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/htmldoc/index.html)
- [Guidelines used for annotating the database (VOC2010)](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/guidelines.html)
