Dataset **PASCAL context** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/0/a/kD/3HQtTVN8QrToTdPm4136D8ANc3rsnxGnJkhVLC7DyydTtm1nzoXS9dPLTm6NUxQUzos8fyX3vR97taBIwatmEeNv35RCrlduwNH7NbXCHwLcTq4iidDbdzydzTKi.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PASCAL context', dst_path='~/dtools/datasets/PASCAL context.tar')
```
The data in original format can be downloaded here:

- 🔗[Training/validation data](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCtrainval_03-May-2010.tar)
- 🔗[Training/validation annotations](https://www.cs.stanford.edu/~roozbeh/pascal-context/trainval.tar.gz)
- 🔗[Development kit code and documentation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/VOCdevkit_08-May-2010.tar)
- 🔗[PDF documentation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/devkit_doc_08-May-2010.pdf)
- 🔗[HTML documentation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/htmldoc/index.html)
- 🔗[Guidelines used for annotating the database (VOC2010)](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/guidelines.html)
