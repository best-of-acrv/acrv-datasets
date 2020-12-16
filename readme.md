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

### Install COCO API ### 
Optional: clone and install the official COCO API Git Repository (if using the COCO dataset):
```
$ git clone https://github.com/cocodataset/cocoapi
$ cd cocoapi/PythonAPI
$ make
$ python setup.py install
```

## Downloading Data ##
To download data, run the ``get_datasets.py``


## Datasets ##
We provide scripts to automatically download and set up all required datasets. You can download all datasets using the ```download_datasets.sh``` file. 
To download all relevant datasets, run the following:
```
$ cd data
$ sh download_datasets.sh
```

This will download and setup all the corresponding data directories required for the models. The data directory should
appear in the following structure:
```
root_dir
├── datasets
│   ├── coco
│   ├── nyu
│   ├── pascal_voc
│   └── sbd
```

## Adding New Datasets ##
To 