from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='acrv_datasets',
      version='0.9.0',
      author='Ben Talbot',
      author_email='b.talbot@qut.edu.au',
      description='Datasets manager for the Best of ACRV',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      package_data={'acrv_datasets': ['*.yaml']},
      install_requires=['colorama', 'pyyaml', 'requests', 'tqdm'],
      classifiers=(
          "Development Status :: 4 - Beta",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
      ))
