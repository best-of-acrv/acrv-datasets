<p align=center><strong>~Please note this is only a <em>beta</em> release at this stage~</strong></p>

# ACRV Datasets: dataset integration for Best of ACRV projects

[![Best of ACRV Repository](https://img.shields.io/badge/collection-best--of--acrv-%23a31b2a)](https://roboticvision.org/best-of-acrv)
![Primary language](https://img.shields.io/github/languages/top/best-of-acrv/acrv-datasets)
[![PyPI package](https://img.shields.io/pypi/pyversions/acrv-datasets)](https://pypi.org/project/acrv-datasets/)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/acrv_datasets.svg)](https://anaconda.org/conda-forge/acrv_datasets)
[![Conda Recipe](https://img.shields.io/badge/recipe-acrv_datasets-green.svg)](https://anaconda.org/conda-forge/acrv_datasets)
[![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/acrv_datasets.svg)](https://anaconda.org/conda-forge/acrv_datasets)
[![License](https://img.shields.io/github/license/best-of-acrv/acrv-datasets)](./LICENSE.txt)

_Note: support will be added soon for datasets that require end-users accept of licensing agreements_

The ACRV Datasets package is a light wrapper for generically managing datasets. The package supports any dataset, as long as it has a public URL. We emphasise that we do not own the datasets accessed through this package, we simply provide easy access and integration for projects like the [Best of ACRV codebases](https://roboticvision.org/best-of-acrv).

Datasets are defined in a YAML file, and there is full support for grouping sub-datasets together. For example, `'coco'` can be used to refer to 13 different COCO datasets with a single identifier. You can also easily add your own datasets simply by editing the same datasets YAML file. Once added, datasets can be downloaded and accessed from Python with simple function calls.

Our code is free to use, and licensed under BSD-3. If you use any datasets in your work, you must appropriately reference _the original dataset authors_! Please see [dataset references](#dataset-references) below.

## Installing the ACRV Datasets package

We offer the following methods for installing the ACRV Datasets package:

1. [Through our Conda and Pip packages](#conda-and-pip): single command installs the package and Python dependences (these are equivalent as there are no system dependencies)
2. [Directly from source](#from-source): allows easy editing and extension of our code, but you take care of building and all dependencies

### Conda and Pip

The ACRV Datasets package has no system dependencies, so installation is the same for both Conda & Pip package management systems.

For Pip, simply install via:

```
u@pc:~$ pip install acrv_datasets
```

Before installing via Conda, you need to make sure you have [Conda installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) on your system, and the [Conda Forge](https://conda-forge.org/) channel has been added globally with strict priority:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once you have access to the `conda-forge` channel, ACRV datasets is installed by running the following from inside a [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). From there, simply run:

```
u@pc:~$ conda install acrv_datasets
```

### From source

Installing from source is very similar to the `pip` method above due to the package only containing Python code. Simply clone the repository, enter the directory, and install via `pip`:

```
u@pc:~$ pip install -e .
```

_Note: the editable mode flag (`-e`) is optional, but allows you to immediately use any changes you make to the code in your local Python ecosystem._

## Downloading & accessing datasets

This package exposes a simple Python interface that automatically handles downloading, extracting, and accessing datasets. All of this complexity is hidden behind a single user action: getting datasets. For example to "get" the NYU dataset:

```python
import acrv_datasets as ad

nyu_location = ad.get_datasets(['nyu'])
```

When calling `get_datasets()`, the dataset will be downloaded and extracted if it doesn't already exist. For example the exact same call above works if you don't already have the `'nyu'` dataset, it will just block and report progress while it gathers the dataset.

Datasets are stored in a default directory, which can be configured via the following code:

```python
import acrv_datasets as ad

ad.set_datasets_directory('/mnt/hdd/acrv_datasets')
```

From this point on, all dataset operations would be performed in the `/mnt/hdd/acrv_datasets` directory. If no location has been set, a default will be used which is printed in yellow before all operations. You can also explicitly override the dataset directory for single operations:

```python
import acrv_datasets as ad

ad.get_datasets(['nyu'], 'mnt/hdd2/other_location')
```

You can see a live list of supported datasets, and access a dictionary containing each dataset's details, with the following code:

```python
import acrv_datasets as ad

details = ad.supported_datasets()
```

The module can also be accessed directly from the command line using the `python3 -m acrv_datasets ...` syntax. Equivalent commands for the above Python are shown below:

```
u@pc:~$ python3 -m acrv_datasets --datasets nyu
```

```
u@pc:~$ python3 -m acrv_datasets --set-default-datasets-directory /mnt/hdd/acrv_datasets
```

```
u@pc:~$ python3 -m acrv_datasets --datasets nyu --datasets-directory /mnt/hdd/acrv_datasets
```

```
u@pc:~$ python3 -m acrv_datasets --supported-datasets
```

There is also a help flag which documents the supported syntax:

```
u@pc:~$ python3 -m acrv_datasets --help
```

## Adding your own datasets

New datasets can be added by making additions to the [`'datasets.yaml'`](https://github.com/raw/master/acrv_datasets/datasets.yaml) file. All that is needed is a unique dataset identifier, and a public URL. A detailed description of the syntax for adding new datasets is provided at the top of the file:

    Datasets are listed in named groups. The group name is the top level key, the
    dataset name is the second level key, and the public URL is a required third
    level key value pair. The group name & dataset name combine to form a unique
    dataset identifier.

    For example, the following would specify a 2014 & 2021 version of my dataset
    called 'my_dataset' (with the unique identifiers 'my_dataset/2014' &
    'my_dataset/2021' respectively):

    my_dataset:
      2014:
        url: https://my_dataset.hosting/2014.tgz
      2021:
        url: https://my_dataset.hosting/2021.tgz

    For brevity the dataset name can be omitted if there is only 1 dataset in a
    group. For example, the following gives a dataset with the identifier
    'my_simple_dataset':

    my_simple_dataset:
      url: https://my_dataset.hosting/simply.tgz

## Dataset references

We again emphasise that you are required to meet all of the licensing terms of the specific dataset if you wish to use the dataset in your own work (we merely provide simplified access).

Below is a list of all datasets identifiers currently available grouped by their owner, with a link provided. Please follow the owner's citation instructions if using their datasets in your research:

- [COCO](https://cocodataset.org/): `coco`, `coco/train2014`, `coco/val2014`, `coco/train2014`, `coco/val2014`, `coco/annotations_trainval2014`, `coco/test2015`, `coco/train2017`, `coco/val2017`, `coco/annotations_trainval2017`, `coco/captions`, `coco/vqa_questions_train`, `coco/vqa_questions_val`, `coco/vqa_questions_test`, `coco/vqa_annotations_train`, `coco/vqa_annotations_val`
- [GloVe](https://nlp.stanford.edu/projects/glove/): `glove`
- [KITTI Odometry](http://www.cvlibs.net/datasets/kitti/eval_odometry.php): `kitti_odometry/gray`, `kitti_odometry/color`
- [NYUv2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html): `nyu`
- [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/): `voc`
- [SBD](http://home.bharathh.info/pubs/codes/SBD/download.html): `sbd`
- TODO???: `trainval36`
