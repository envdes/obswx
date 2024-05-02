obswx: A Python package for accessing observational meteorological data
-----------------------------------------------------------------------
|DOI| |docs| |GitHub| |license|

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.11100151.svg
  :target: https://doi.org/10.5281/zenodo.11100151

.. |GitHub| image:: https://img.shields.io/badge/GitHub-obswx-brightgreen.svg
   :target: https://github.com/envdes/obswx

.. |Docs| image:: https://img.shields.io/badge/docs-obswx-brightgreen.svg
   :target: https://envdes.github.io/obswx/

.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/envdes/obswx/blob/main/LICENSE


Contributors: `Junjie Yu  <https://junjieyu-uom.github.io/>`_, `Yuan Sun  <https://github.com/YuanSun-UoM/>`_, `Haofan Wang  <https://github.com/Airwhf/>`_, `Zhiyi Song <https://github.com/onebravekid>`_, `David Topping <https://research.manchester.ac.uk/en/persons/david.topping>`_, `Zhonghua Zheng <https://zhonghuazheng.com>`_ (zhonghua.zheng@manchester.ac.uk)

Installation
------------
Step 1: create an environment::

    $ conda create -n obswx python=3.11

    $ conda activate obswx

    $ conda install -c conda-forge pandas geopy xarray -y


Step 2: install using pip::

    $ pip install obswx

(optional) install from source:: 

    $ git clone https://github.com/envdes/obswx.git
    $ cd obswx
    $ python setup.py install

How to use it?
--------------
Python

.. code-block:: python

   from obswx import *
   import os

   # Initialize
   met = obswx(source='UK-hist_station')
   
   # get meta data
   met.get_meta(load=True).head()

   # get data
   met.get_data(station="Armagh")

.. Please check `online documentation <https://envdes.github.io/obswx/>`_ for more information.

How to ask for help
-------------------
The `GitHub issue tracker <https://github.com/envdes/obswx/issues>`_ is the primary place for bug reports. 
