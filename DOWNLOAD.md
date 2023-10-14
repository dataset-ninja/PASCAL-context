Dataset **PASCAL Context** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/k/0/dB/Sm2dLIlHObD59znzbpyMhNS2NqS4ymzjJKGXlk2TEBOASMy1K41kbpn7mOq5bXd6czz5i73e9QsfqNooYY2A5T0VKno8ZyhlHoDAiQOFBP4jfcsTOKWh7LbaI7J0.tar)

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
