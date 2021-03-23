from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='acrv_datasets',
      version='0.1.0',
      author='Ben Talbot',
      author_email='b.talbot@qut.edu.au',
      description='Datasets manager for the Best of ACRV',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires=['pyyaml'],
      classifiers=(
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
      ),
      python_requires='>=3.6')
