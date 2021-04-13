import colorama
import glob
import math
import os
import pkg_resources
import tarfile
import yaml
import zipfile

from .downloader import Download

DATASETS_FILE = pkg_resources.resource_filename(__name__, 'datasets.yaml')

DATASETS_DIRECTORY_RESOURCE = '.acrv_datasets_directory'
DEFAULT_DATASETS_DIRECTORY = os.path.expanduser('~/.acrv_datasets')


def get_datasets(dataset_names, datasets_directory=None):
    # Perform argument validation
    colorama.init()
    if not dataset_names:
        print("%sERROR: no datasets provided to download%s" %
              (colorama.Fore.RED, colorama.Style.RESET_ALL))
        return _exit()
    if type(dataset_names) == str:
        dataset_names = [dataset_names]
    unsupported_datasets = [
        d for d in dataset_names if d not in _dataset_identifiers()
    ]
    if unsupported_datasets:
        print("%sERROR: unsupported_datasets were requested "
              "(see 'supported_datasets()'):\n\t%s%s" %
              (colorama.Fore.RED, unsupported_datasets,
               colorama.Style.RESET_ALL))
        return _exit()
    colorama.deinit()

    # Get the datasets directory
    datasets_directory = get_datasets_directory(datasets_directory)

    # Download and prepare each of the datasets
    for d in dataset_names:
        _print_block('Downloading %s dataset/s' % d)
        results = _download_dataset(d, datasets_directory)
        _print_block('Preparing %s dataset/s' % d)
        _prepare_dataset(d,
                         datasets_directory,
                         skip_map={k: not v for k, v in results.items()})
    ps = [_dataset_path(datasets_directory, d) for d in dataset_names]
    return ps if len(ps) > 1 else ps[0]


def get_datasets_directory(requested_directory=None):
    if requested_directory is not None:
        return requested_directory
    else:
        fn = pkg_resources.resource_filename(__name__,
                                             DATASETS_DIRECTORY_RESOURCE)
        if os.path.exists(fn):
            with open(fn, 'r') as f:
                return f.readline()
        print("%sWARNING: no output directory provided, and no default set. "
              "Downloading to the default instead:\n\t%s%s" %
              (colorama.Fore.YELLOW, DEFAULT_DATASETS_DIRECTORY,
               colorama.Style.RESET_ALL))
        return DEFAULT_DATASETS_DIRECTORY


def set_datasets_directory(datasets_directory):
    fn = pkg_resources.resource_filename(__name__, DATASETS_DIRECTORY_RESOURCE)
    if pkg_resources.resource_exists(__name__, DATASETS_DIRECTORY_RESOURCE):
        with open(fn, 'r') as f:
            old = f.readline()
            print("Existing default datasets directory found:\n\t%s" % old)
    with open(fn, 'w') as f:
        f.write(datasets_directory)
    print("New default datasets directory set:\n\t%s" % datasets_directory)


def supported_datasets():
    print('The following dataset identifiers are supported:\n\t%s\n' %
          '\n\t'.join(_dataset_identifiers()))
    print('New datasets can be added to the YAML definition file:\n\t%s' %
          DATASETS_FILE)
    return DATASETS


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
    resps = {}
    for k, d in downloaders.items():
        if os.path.exists(d.download_path):
            print('Found existing file at: ' + d.download_path)
            resps[k] = d.resume()
        else:
            print('Could not find existing file at: ' + k +
                  '. Starting new download...')
            os.makedirs(os.path.dirname(d.download_path), exist_ok=True)
            resps[k] = d.download()
    return resps


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


def _prepare_dataset(dataset, datasets_directory, skip_map=None):
    # Create a map of expanded identifiers to destinations
    datasets = {
        d: _dataset_path(datasets_directory, d)
        for d in _expand_identifier(dataset)
    }

    # Extract the contents of each archive to the target destination
    for k, v in datasets.items():
        if skip_map is not None and skip_map.get(k, None):
            print("Skipping already prepared dataset '%s'" % k)
            continue
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
                } for kk, vv in v.items()
            })
        else:
            ret[_dataset_identifier(k)] = {'url': v}
    return ret


DATASETS = _process_yaml(DATASETS_FILE)
