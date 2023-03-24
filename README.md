[![CircleCI](https://circleci.com/gh/ionpath/mibilib.svg?style=svg&circle-token=e798611a4abf9f2503a532c8ad5fd02d849d85a0)](https://circleci.com/gh/ionpath/mibilib)

# mibilib

Python client for IONpath MIBItracker API, plus utility functions for working
with MIBItiff images.

https://ionpath.github.io/mibilib/

## Setup

### Install Miniconda
Install the lastest version of [Miniconda](https://conda.io/miniconda.html).
Even if your system already has a standalone version of Python installed,
it is strongly recommended to use the `conda` environment manager to install and
manage this library's dependencies.

### Install `mibilib` with `conda` and `pip`
```bash
conda env create -f environment.yml
conda activate mibilib
```

## Usage
It's easy to work with MIBITIFFs using the `mibidata` module.
```Python3
from mibidata import tiff

# extract metadata from mibitiff (fast)
metadata = tiff.info("mibi.tif")  # returns a dictionary

# print FoV name from metadata
print(metadata["fov_name"])

# read a mibitiff into a MibiImage class instance (slow)
mibitiff = tiff.read("mibi.tif")

# print channel tuples from mibitiff
print(mibitiff.channels)

# copy MibiImage class into a new instance
newtiff = mibitiff.copy()

# rename a target channel
OLD_TARGET = "dsDNA"
NEW_TARGET = "dsDNA (nuclear marker)"
newtiff.rename_targets({OLD_TARGET: NEW_TARGET})

# offset pixel data of all channels
newtiff.data += 2.0

# multiply data of second channel only
CHANNEL = 1
newtiff.data[:, :, CHANNEL] *= 1.2

# write MibiImage class into a file
tiff.write("new.tiff", newtiff)
```

To use the MIBItracker API with `mibitracker`, you will need to use the backend url listed in the
About page. This can be accessed after you have logged in from the menu
under your username in the upper right of the window.
```Python3
from mibitracker.request_helpers import MibiRequests

request = MibiRequests(
    'https://your-mibitracker-backend.appspot.com',
    'user@example.com',
    'password1234'
)
image_id = request.image_id('20180927', 'Point3')
image_details = request.get('/images/{}/'.format(image_id))
```

More examples can be found in the following notebooks:

 - [MIBItracker_API_Tutorial](MIBItracker_API_Tutorial.ipynb)

 - [MibiImage_Tutorial](MibiImage_Tutorial.ipynb)

 - [SingleCellSpatialExamples](SingleCellSpatialExamples.ipynb)

Full documentation for this library can be found at
https://ionpath.github.io/mibilib/.

## Sample data
Access to sample data to run the tutorials in the notebooks can be
requested by creating an account at the following URL:
https://mibi-share.ionpath.com.
