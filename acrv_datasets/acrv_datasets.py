import colorama
import math
import os
import tarfile
import yaml
import zipfile

from .downloader import Download

DATASETS_FILE = os.path.join(os.path.dirname(__file__), 'datasets.yaml')
DATASETS = yaml.safe_load(open(DATASETS_FILE, 'r'))

DEFAULT_SAVE_DIRECTORY = os.path.expanduser('~/.acrv_datasets')


def dataset_identifier(group, name=None):
    return group if name is None else '%s/%s' % (group, name)


def dataset_identifiers(groups=None):
    ids = {}
    for k, v in DATASETS.items():
        ids[dataset_identifier(k)] = v
        if type(v) is dict:
            ids.update({dataset_identifier(k, kk): vv for kk, vv in v.items()})
    return ids


def get_datasets(datasets, datasets_directory):
    # Perform argument validation
    colorama.init()
    if not datasets_directory:
        print('%sWARNING: no output directory provided, downloading '
              'to the default instead:\n\t%s%s' %
              (colorama.Fore.YELLOW, DEFAULT_SAVE_DIRECTORY,
               colorama.Style.RESET_ALL))
        datasets_directory = DEFAULT_SAVE_DIRECTORY

    if not datasets:
        print("%sERROR: no datasets provided to download%s" %
              (colorama.Fore.RED, colorama.Style.RESET_ALL))
        return _exit()
    unsupported_datasets = [d for d in datasets if d not in DATASETS.keys()]
    if unsupported_datasets:
        print("%sERROR: unsupported_datasets were requested "
              "(see 'supported_datasets()'):\n\t%s%s" %
              (colorama.Fore.RED, unsupported_datasets,
               colorama.Style.RESET_ALL))
        return _exit()
    colorama.deinit()

    # Download and prepare each of the datasets
    for d in datasets:
        _print_block('Downloading %s dataset/s' % d)
        _download_dataset(d, datasets_directory)
        _print_block('Preparing %s dataset/s' % d)
        _prepare_dataset(d, datasets_directory)
    return True


def get_url(dataset_identifier):
    pass


def supported_datasets():
    print('The following dataset identifiers are supported:\n\t%s\n' %
          '\n\t'.join(dataset_identifiers()))
    print('New datasets can be added to the YAML definition file:\n\t%s' %
          DATASETS_FILE)


def _exit():
    # Exit tidily
    colorama.deinit()
    return False


def _download_dataset(dataset, data_directory):
    # Downloads dataset into a specified data directory
    dataset = dataset.lower()

    # Get dataset urls (and handle simplified syntax)
    get_urls(dataset)

    # create downloaders from dataset urls
    downloaders = {}
    for k, v in dataset_urls.items():
        folder_name = k.split('_')[0]
        dataset_directory = os.path.join(data_directory, folder_name)
        if dataset == 'voc' or dataset == 'sbd':
            dest = os.path.join(dataset_directory, k + '.tar')
        else:
            dest = os.path.join(dataset_directory, k + '.zip')
        downloaders[dest] = Download(v, dest)

    # download files
    for k, d in downloaders.items():
        if os.path.exists(k):
            print('Found existing file at: ' + k + '!')
            d.resume()
        else:
            print('Could not find existing file at: ' + k +
                  '. Starting new download...')
            os.makedirs(os.path.dirname(k), exist_ok=True)
            d.download()


def _prepare_dataset(dataset, data_directory):
    dataset = dataset.lower()

    # full data directory
    data_location = os.path.join(data_directory, dataset)

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


def _print_block(text):
    text = ' %s ' % text
    pad_length = 0.5 * (80 - len(text))
    print('-' * 80)
    print('-' * math.floor(pad_length) + text + '-' * math.ceil(pad_length))
    print('-' * 80)
