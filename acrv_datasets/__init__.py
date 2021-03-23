import os
import yaml

# from .utils import get_datasets

DATASETS_FILE = os.path.join(os.path.dirname(__file__), 'datasets.yaml')
DATASETS = yaml.safe_load(open(DATASETS_FILE, 'r'))

DEFAULT_SAVE_DIRECTORY = os.path.expanduser('~/.acrv_datasets')
