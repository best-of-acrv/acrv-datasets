import os
import downloader
import re
import tarfile
import zipfile
from dataset_urls import *

# downloads specified dataset into specified data directory
def download_dataset(dataset, data_directory):
    dataset = dataset.lower()

    # get corresponding dataset urls
    dataset_urls = get_urls(dataset)

    # create downloaders from dataset urls
    downloaders = {}
    for k,v in dataset_urls.items():
        folder_name = k.split('_')[0]
        dataset_directory = os.path.join(data_directory, folder_name)
        if dataset == 'voc' or dataset == 'sbd':
            dest = os.path.join(dataset_directory, k + '.tar')
        else:
            dest = os.path.join(dataset_directory, k + '.zip')
        downloaders[dest] = downloader.Download(v, dest)

    # download files
    for k, d in downloaders.items():
        if os.path.exists(k):
            print('Found existing file at: ' + k + '!')
            d.resume()
        else:
            print('Could not find existing file at: ' + k + '. Starting new download...')
            os.makedirs(os.path.dirname(k), exist_ok=True)
            d.download()

def prepare_dataset(dataset, data_directory):
    dataset = dataset.lower()
    upper_folder = re.sub(r'\d+', '', dataset)

    # full data directory
    data_location = os.path.join(data_directory, upper_folder)

    # list all archived files
    for file in os.listdir(data_location):
        print('Extracting ' + file + '...')
        filepath = os.path.join(data_location, file)
        # zip files
        if file.endswith('.zip'):
            with zipfile.ZipFile(filepath, 'r') as f:
                print('Extracting to: ' + data_location)
                f.extractall(data_location)

        # tarballs
        elif file.endswith('.tar'):
            with tarfile.open(filepath, 'r') as f:
                print('Extracting to: ' + data_location)
                f.extractall(data_location)

        # remove archived files
        if os.path.isfile(filepath):
            os.remove(filepath)
