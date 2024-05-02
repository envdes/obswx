## About

obswx is A Python package for accessing observational meteorological data. For now, the [UK Historic station data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data), NOAA Integrated Surface Database from [AWS S3 sources](https://registry.opendata.aws/noaa-isd/) and [NOAA source](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) are available for download. The package also provides tool to read in a [HadISD - global sub-daily station dataset](https://www.metoffice.gov.uk/hadobs/hadisd/index.html) data.

## Installation

Step 1: create a conda environment

```bash
$ conda create -n obswx python=3.11
$ conda activate obswx
$ conda install -c conda-forge pandas xarray geopy
```

Step 2: install using `pip`

```bash
$ pip install obswx
```

(optional) install from source:: 

```bash
$ git clone https://github.com/envdes/obswx
$ cd obswx
$ python setup.py install
```
