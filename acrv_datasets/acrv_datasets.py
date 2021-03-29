import colorama
import glob
import math
import os
import tarfile
import yaml
import zipfile

from .downloader import Download

DATASETS_FILE = os.path.join(os.path.dirname(__file__), 'datasets.yaml')

DEFAULT_SAVE_DIRECTORY = os.path.expanduser('~/.acrv_datasets')


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
    unsupported_datasets = [
        d for d in datasets if d not in _dataset_identifiers()
    ]
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


def supported_datasets():
    print('The following dataset identifiers are supported:\n\t%s\n' %
          '\n\t'.join(_dataset_identifiers()))
    print('New datasets can be added to the YAML definition file:\n\t%s' %
          DATASETS_FILE)


def _dataset_group(identifier):
    return identifier.split('/')[0]


def _dataset_identifier(group, name=None):
    return group if name is None else '%s/%s' % (group, name)


def _dataset_identifiers(groups=None):
    ret = []
    for k, v in DATASETS.items():
        if 'group' in v and v['group'] not in ret:
            ret.append(v['group'])
        ret.append(k)
    return ret


def _dataset_path(datasets_directory, dataset_identifier):
    return os.path.join(datasets_directory, dataset_identifier)


def _download_dataset(dataset, datasets_directory):
    # Get dataset urls (and handle simplified syntax)
    datasets = {d: DATASETS[d] for d in _expand_identifier(dataset)}

    # Create downloaders from dataset urls
    downloaders = {
        k: Download(v['url'], _dataset_path(datasets_directory, k))
        for k, v in datasets.items()
    }

    # Download files
    for k, d in downloaders.items():
        if os.path.exists(d.download_path):
            print('Found existing file at: ' + d.download_path + '!')
            d.resume()
        else:
            print('Could not find existing file at: ' + k +
                  '. Starting new download...')
            os.makedirs(os.path.dirname(d.download_path), exist_ok=True)
            d.download()


def _exit():
    # Exit tidily
    colorama.deinit()
    return False


def _expand_identifier(dataset_identifier):
    return ([dataset_identifier]
            if dataset_identifier in DATASETS.keys() else [
                k for k, v in DATASETS.items()
                if v.get('group', None) == dataset_identifier
            ])


def _is_group(dataset_identifier):
    return dataset_identifier.endswith('/') or '/' not in dataset_identifier


def _prepare_dataset(dataset, datasets_directory):
    # Create a map of expanded identifiers to destinations
    datasets = {
        d: _dataset_path(datasets_directory, d)
        for d in _expand_identifier(dataset)
    }

    # Extract the contents of each archive to the target destination
    for k, v in datasets.items():
        source = glob.glob('%s.*' % v)
        if len(source) != 1:
            raise RuntimeError(
                "Failed to find a unique matching local source archive for '%s'"
                "\n(this should never happen). Found the following:\n\t%s" %
                (k, source))

        ext = os.path.splitext(source[0])[1]
        with (zipfile.ZipFile if ext == '.zip' else tarfile.open)(source[0],
                                                                  'r') as f:
            print('Extracting to: %s' % v)
            f.extractall(v)


def _print_block(text):
    text = ' %s ' % text
    pad_length = 0.5 * (80 - len(text))
    print('-' * 80)
    print('-' * math.floor(pad_length) + text + '-' * math.ceil(pad_length))
    print('-' * 80)


def _process_yaml(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)

    ret = {}
    for k, v in data.items():
        if type(v) is dict:
            ret.update({
                _dataset_identifier(k, kk): {
                    'url': vv,
                    'group': k
                }
                for kk, vv in v.items()
            })
        else:
            ret[_dataset_identifier(k)] = {'url': v}
    return ret


DATASETS = _process_yaml(DATASETS_FILE)
