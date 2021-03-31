# ACRV Datasets: dataset integration for Best of ACRV projects

The ACRV Datasets package is a light wrapper for generically managing datasets. The package allows any dataset to be added, as long as it has a public URL. We emphasise that we do not own the datasets accessed through this package, we simply provide easy access and integration for projects like the [Best of ACRV codebases](https://roboticvision.org/best-of-acrv).

Datasets are defined in a YAML file, and there is full support for grouping sub-datasets together. For example, `'coco'` can be used to refer to 13 different COCO datasets with a single identifier. Once added, datasets can be downloaded and accessed from Python with simple function calls. You can also easily add your own datasets simply by editing the same datasets YAML file.

Our code is free to use, and licensed under BSD-3. If you use any datasets in your work, you must appropriately reference _the original dataset authors_! Please see [dataset references](#dataset-references) below.

## Installing the ACRV Datasets package

We offer the following methods for installing the ACRV Datasets package:

1. [Through our Conda and Pip packages](#conda-and-pip): single command installs the package and Python dependences (these are equivalent as there are no system dependencies)
2. [Directly from source](#from-source): allows easy editing and extension of our code, but you take care of building and all dependencies

### Conda and Pip

The ACRV Datasets package has no system dependencies, so installation is the same for both Conda & Pip package management systems.

For Pip, simply install via:

```
u@pc:~$ pip install acrv-datasets
```

Installation via Conda is the same once you have [Conda installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) on your system, and are inside a [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). From there, simply run:

```
u@pc:~$ conda install acrv-datasets
```

You can see a list of the package's Python dependencies in the [`./requirements.yml`](./requirements.yml) file.

TODO make sure requirements location is actually correct ^

### From source

Installing from source is very similar to the `pip` method above due to the package only containing Python code. Simply clone the repository, enter the directory, and install via `pip` in editable mode:

```
u@pc:~$ pip install -e .
```

Editable mode allows you to immediately use any changes you make to RefineNet's code in your local Python ecosystem.

TODO: add instructions for from source method that doesn't use pip (i.e. just running scripts)

## Downloading & accessing datasets

TODO add some words....

Accessing datasets from your code. For example, get location of NYU dataset:

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

TODO information about `'datasets.yaml'` file

TODO information about running this via `python3 -m acrv_datasets ...`

TODO maybe via a script as well? Probably not necessary...

## Adding your own datasets

TODO proper information (in short, just edit the `'datasets.yaml'` file)

## Dataset references

TODO proper list of datasets & how to cite them

- [NYUv2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)
- [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
- [SBD](http://home.bharathh.info/pubs/codes/SBD/download.html)
- [COCO](https://cocodataset.org/)
- [GloVe](https://nlp.stanford.edu/projects/glove/)
