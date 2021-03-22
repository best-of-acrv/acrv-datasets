import os
import argparse
import downloader
import zipfile
from utils import download_dataset, prepare_dataset

# get general arguments
parser = argparse.ArgumentParser(description='ACRV datasets')
# add dataset specific arguments
parser.add_argument('--name', type=str, default='acrv-datasets', help='custom prefix for naming model')
parser.add_argument('--datasets', nargs='+', help='name of dataset: choose from [nyu, voc, sbd, coco, glove, trainval36]', required=True)
parser.add_argument('--data_directory', type=str, default='datasets', help='directory to save datasets to')
args = parser.parse_args()

# valid datasets
valid_datasets = ['nyu', 'voc', 'sbd', 'coco', 'glove', 'trainval36']

if __name__ == '__main__':

    # get list of datasets specified for download
    dataset_list = args.datasets

    # go through each item in dataset list
    for d in dataset_list:

        # check if dataset name is valid
        if d.lower() not in valid_datasets:
            print(d + ' is not a valid dataset to download! Please choose from:')
            print(valid_datasets)
            continue

        # download dataset
        print('---------------------------------------------------')
        print('Downloading ' + d + ' dataset(s)')
        print('---------------------------------------------------')
        download_dataset(dataset=d, data_directory=args.data_directory)

        # unzip and then remove
        print('---------------------------------------------------')
        print('Preparing ' + d + ' dataset(s)')
        print('---------------------------------------------------')
        prepare_dataset(dataset=d, data_directory=args.data_directory)




