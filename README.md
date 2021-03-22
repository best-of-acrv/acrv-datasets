# README #

This repository downloads and sets up all the required datasets for the following Best-of-ACRV projects. This project include:

> Lin, Guosheng, et al. 'Refinenet: Multi-path refinement networks for 
> high-resolution semantic segmentation.' Proceedings of the IEEE conference on 
> computer vision and pattern recognition. 2017.

> Nekrasov, Vladimir, Chunhua Shen, and Ian Reid. "Light-Weight RefineNet for 
> Real-Time Semantic Segmentation." British Machine Vision Conference, 2018.

> Anderson, Peter, et al. "Bottom-up and top-down attention for image captioning and visual question answering." 
> Proceedings of the IEEE conference on computer vision and pattern recognition. 2018.

> Tian, Zhi, et al. "Fcos: Fully convolutional one-stage object detection." 
> Proceedings of the IEEE international conference on computer vision. 2019.


## Setup ##
First, create the corresponding Conda environment according to the specified [project](https://github.com/best-of-acrv):
```
$ conda env create -f requirements.yml
```
This should set up the conda environment with all prerequisites for running this code from the desired [project](https://github.com/best-of-acrv). 
Activate this Conda environment using the following command:
```
$ conda activate acrv-datasets
```

## Downloading Data ##
To download and prepare dataset, run the ``get_datasets.py``. This will download and setup all the corresponding data 
directories required for the models. The data directory should appear in the following structure:
```
root_dir
|--- datasets
|   |-- coco
|   |-- glove
|   |-- nyu
|   |-- pascal_voc
|   |-- sbd
|   |-- trainval36
```
To select datasets to download, use the ``--datasets`` argument. The supported datasets so far are:
* [NYUv2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)
* [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
* [SBD](http://home.bharathh.info/pubs/codes/SBD/download.html)
* [COCO](https://cocodataset.org/)
* [GloVe](https://nlp.stanford.edu/projects/glove/)

For example, to download the NYU and VOC datasets, run the following command from the root directory:
```
$ python get_datasets.py --datasets nyu voc
```

## Adding Datasets ##
To add your own datasets, please refer to the ``datasets_url.py``. A new dataset dictionary and ``elif`` should be added 
according to the provided example.