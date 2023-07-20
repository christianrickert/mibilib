# mibilib

Python client for IONpath MIBItracker API, plus utility functions for working
with MIBItiff images.

https://ionpath.github.io/mibilib/

`mibilib` has been updated for compatibility with `MIBIscope/mibin-commercial` MIBItiff images.  
In particular, custom [HIMSR](https://medschool.cuanschutz.edu/immunology-immunotherapy/himsr) tags have been added to the existing `ImageDescription` TIFF tag:
* `himsr.author`: [@christianrickert](https://www.linkedin.com/in/christianrickert)
* `himsr.back`: level of background correction (gold slide interference)
* `himsr.bloom`: level of bloom correction (horizontal stripes)
* `himsr.creation`: timestamp at time of MIBItiff creation
* `himsr.mph`: median pulse height for normalization
* `himsr.software`: "mibin-commercial, v.0.9.0"
* `himsr.window`: mass window for target

Optional tags can be added to the metadata:
* `mibi.norm`: normalization factor

Prefix optional tags with `mibi.` for compatibility with Bio-Formats.

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

# normalize pixel data of all channels
NRM = 1.23
newtiff.data *= NRM

# offset data of second channel only
CHANNEL = 1
newtiff.data[:, :, CHANNEL] += 3.0

# add custom tags with a dictionary
TAGS = {"mibi.norm": NRM}
newtiff.add_attr(**TAGS)

# write MibiImage class into a file
tiff.write("new.tiff", newtiff)
```

To use the MIBItracker API with `mibitracker`, you will need to use the backend url listed in the
About page. This can be accessed after you have logged in from the menu
under your username in the upper right of the window.
```Python3
from mibitracker.request_helpers import MibiRequests

request = MibiRequests(
    'https://[sitename].api.ionpath.com',
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
