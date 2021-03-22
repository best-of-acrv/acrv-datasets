import argparse
import os
import yaml

DATASETS = yaml.load(
    open(os.path.join(os.path.dirname(__file__), 'datasets.yaml'), 'r'))
