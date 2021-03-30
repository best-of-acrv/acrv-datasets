import argparse
import os
import sys

import acrv_datasets as ad

if __name__ == "__main__":
    # Parse arguments
    p = argparse.ArgumentParser(
        description='ACRV wrappers for dataset management')
    p.add_argument('--datasets',
                   help='Comma-separated list of dataset identifiers to '
                   'download (see --supported-datasets for valid values)')
    p.add_argument('--datasets-directory',
                   help='Use this directory instead for this operation only.')
    p.add_argument(
        '--set-default-datasets-directory',
        help='Use the following directory by default for all future operations'
    )
    p.add_argument('--supported-datasets',
                   action='store_true',
                   help="List currently supported datasets and exit "
                   "(edit 'datasets.yaml' to add extra datasets)")
    args = p.parse_args()

    # Handle special cases
    if args.supported_datasets:
        ad.supported_datasets()
        sys.exit()
    elif args.set_default_datasets_directory:
        ad.set_datasets_directory(args.set_default_datasets_directory)
        sys.exit()

    # Defer the call to the 'get_datasets' function
    ad.get_datasets('' if args.datasets is None else args.datasets.split(','),
                    args.datasets_directory)
