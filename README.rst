pyWX: A Python package for accessing observational meteorological data
----------------------------------------------------------------------
|doi| |docs| |GitHub| |license| |pepy|

.. |GitHub| image:: https://img.shields.io/badge/GitHub-pywx-brightgreen.svg
   :target: https://github.com/envdes/pywx

.. |Docs| image:: https://img.shields.io/badge/docs-pywx-brightgreen.svg
   :target: https://envdes.github.io/pywx/

.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/envdes/pywx/blob/main/LICENSE
   
.. |pepy| image:: https://static.pepy.tech/personalized-badge/pywx?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/pywx


Author: `Junjie Yu  <https://junjieyu-uom.github.io/>`_, `Yuan Sun  <https://github.com/YuanSun-UoM/>`_, `Haofang Wang  <https://github.com/Airwhf/>`_, `Zhiyi Song <https://github.com/onebravekid>`_, `David Topping <https://research.manchester.ac.uk/en/persons/david.topping>`_, `Zhonghua Zheng <https://zhonghuazheng.com>`_ (zhonghua.zheng@manchester.ac.uk)

Installation
------------
Step 1: create an environment::

    $ conda create -n pywx python=3.11

    $ conda activate pywx

    $ conda install -c conda-forge pandas geopy xarray -y


Step 2: install using pip::

    $ pip install pywx

(optional) install from source:: 

    $ git clone https://github.com/envdes/pywx.git
    $ cd pywx
    $ python setup.py install

How to use it?
--------------
Python

.. code-block:: python

   from pywx import *
   import os

   # Initialize
   met = pywx(source='UK-hist_station')
   
   # get meta data
   met.get_meta(load=True).head()

   # get data
   met.get_data(station="Armagh")

.. Please check `online documentation <https://envdes.github.io/pywx/>`_ for more information.

How to ask for help
-------------------
The `GitHub issue tracker <https://github.com/envdes/pywx/issues>`_ is the primary place for bug reports. 
