import argparse
import os
import sys

import acrv_datasets as ad

if __name__ == "__main__":
    # Parse arguments
    p = argparse.ArgumentParser(
        description='ACRV wrappers for dataset management')
    p.add_argument('--datasets',
                   nargs=1,
                   help='Comma-separated list of datasets to download '
                   '(see --supported-datasets for valid values)')
    p.add_argument('--datasets-directory',
                   nargs=1,
                   help='Location where downloaded datasets are stored')
    p.add_argument('--supported-datasets',
                   action='store_true',
                   help="List currently supported datasets and exit "
                   "(edit 'datasets.yaml' to add extra datasets)")
    args = p.parse_args()

    # Handle special cases
    if args.supported_datasets:
        print('The following dataset names are supported:\n\t%s\n' %
              '\n\t'.join(ad.DATASETS.keys()))
        print('New datasets can be added to the YAML definition file:\n\t%s' %
              ad.DATASETS_FILE)
        sys.exit()
    if not args.datasets_directory:
        print('NO SAVE')

    # Defer the call to the 'get_datasets' function
    # ad.get_datasets()
