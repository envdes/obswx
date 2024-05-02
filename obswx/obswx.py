# encoding: utf-8
# Junjie Yu, Zhonghua Zheng, 2024-05-01, Manchester, UK

#import boto3
#import botocore
import pandas as pd
from geopy import distance
from .config import config, source_alias
from typing import Union
from .utils import read_hadisd
import urllib.request
import os


class obswx:
    def __init__(self, source="ISD"):

        self.source = source # source of data
    
    def get_meta(self, **kwargs):
            
        """
        Get metadata

        Args:

            source: str, source of the data
            load: bool, load data or not

        Returns:
            pandas dataframe
        """
        #print("Getting metadata")

        if "soure" in kwargs:
            self.source = kwargs["source"]

        if "load" in kwargs:
            load = kwargs["load"]
        else:
            load = False

        if self.source in source_alias["isd"]:  #["ISD", "isd", "NOAA-isd", "noaa-isd", "noaa_isd", "NOAA-ISD"]:
            metafile = config["meta"]["noaa"]

        if self.source in source_alias["hadisd"]: #["HADISD", "hadisd", "HAD-ISD", "had-isd"]:
            metafile = config["meta"]["hadisd"] 

        if self.source in source_alias["uk"]: #["UK-hist_station", "UK-hist-station", "UK_hist_station", "UK_hist-station", "UK_hist_station", "UK_hist-station"]:
            metafile = config["meta"]["uk"]

        if load:
            if self.source in source_alias["hadisd"]:
                meta = pd.read_csv(metafile, sep='\s+', header=None, names=['station_id', 'lat', 'lon', 'elevation'])
            else:
                meta = pd.read_csv(metafile)
            return meta
    
        else:
            print("Check Metadata here:{}".format(metafile))
            return 0
    
    def get_data(self, **kwargs):

        """
        Get data

        Args:

            year: int, year of the data

            station: str, station ID

            print_info: bool, print information or not

            isd_source: str, source of the ISD data

        RETURNS:
            pandas dataframe
        """


        if "isd_source" in kwargs:
            isd_source = kwargs["isd_source"]
        else:
            if self.source:
                isd_source = self.source
            else:
                raise ValueError("No isd source provided")
            

        if "year" in kwargs:
            year = kwargs["year"]

        if "station" in kwargs:

            station = kwargs["station"]

        if "print_info" in kwargs:
            print_info = kwargs["print_info"]
        else:
            print_info = True
        
        if self.source in source_alias["isd"]: #["ISD", "isd", "NOAA-isd", "noaa-isd", "noaa_isd", "NOAA-ISD"]:
            if print_info:
                print("Getting data from NOAA ISD")
                print("Here to help select station: ", config["map"]["isd"])
            self.resutl = self._get_isd(source=isd_source, year=year, station=station)
        
        if self.source in source_alias["hadisd"]: #["HadISD", "hadisd", "Hadisd", "HADISD", "Had-isd", "had-isd", "HAD-ISD", "Had-isd"]:
            if print_info:
                print("Getting data from HadISD")
                print("Here to help select station: ", config["map"]["hadisd"])
            self.resutl = self._get_isd(source=isd_source, station=station)


        if self.source in source_alias["uk"]: #["UK-hist_station", "UK-hist-station", "UK_hist_station", "UK_hist-station", "UK_hist_station", "UK_hist-station"]:
            if print_info:
                print("Getting data from UK Historical Station")
                print("Here to help select station: ", config["map"]["uk"])
            self.resutl = self._get_uk_hist(station=station)

        return self.resutl

        

    def _get_isd(self, **kwargs):

        """
        Get ISD data
        
        Args:

            year: int
                Year of the data
            station: str
                Station ID
            source: str
                Source of the data
            output: str
                Output file path (optional) for HadISD data
        
        RETURNS:

            filepath: str        
        """

        #if "bucket_name" in kwargs:
        #    self.bucket_name = kwargs["bucket_name"]
        #else:
        #    self.bucket_name = "noaa-global-hourly-pds"

        if "year" in kwargs:
            self.year = str(kwargs["year"])
        else:
            self.year = "2015"
        if "station" in kwargs:
            self.station = kwargs["station"]

        #if "target" in kwargs:
        #    self.targetfile = kwargs["target"]
        #else:
        #    self.targetfile = f'{self.station}.csv'

        if "source" in kwargs:
            source = kwargs["source"]
        else:
            source = "AWS"
        
        if "output" in kwargs:
            output_path = kwargs["output"]
        else:
            output_path = None

        if source in source_alias["aws"]: #["AWS", "aws", "S3", "s3"]:
            filepath = config["isd"]["aws"].format(self.year, self.station)
            data = pd.read_csv(filepath)
        if source in source_alias["noaa"]: #["NOAA", "noaa", "NOAA-isd", "noaa-isd", "noaa_isd", "NOAA-ISD"]:
            filepath = config["isd"]["noaa"].format(self.year, self.station)
            data = pd.read_csv(filepath)

        if source in source_alias["hadisd"]:
            filepath = config['isd']["hadisd"].format(self.station)
            if output_path:
                downloadfile = f"{output_path}/{self.station}.nc.gz"
            else:
                downloadfile = f"{self.station}.nc.gz"
            if not os.path.exists(downloadfile):
                print(f"Downloading data from {filepath}")
                r = urllib.request.urlopen(filepath)
                content = r.read()
                with open(downloadfile, 'wb') as f:
                    f.write(content)
            else:   
                print(f"File {downloadfile} already exists.")
                print(f"Reading data from {downloadfile}")

            data = read_hadisd(path=downloadfile)
        

        return data
    
    def _get_uk_hist(self, skiprows=5, header=[0,1], **kwargs):

        """
        GET UK HISTORICAL DATA

        Args:

        kwargs: dictionary
            station: str
                Station ID
            skiprows: int
                Skip rows
            header: list
                Header rows
        
        RETURNS:
            
                data: pandas dataframe
        """

        if "station" in kwargs:
            station = kwargs["station"].lower()
        else:
            station = "Aberporth".lower()

        meta = self.get_meta(load=True, source="UK-hist-station")

        meta = meta[meta['Name'].str.lower() == station]

        print(f"Getting data from {meta['Link'].values[0]}")

        df = pd.read_fwf(meta['Link'].values[0], skiprows= skiprows, header=0)

        df.columns = df.columns + '[' + df.iloc[0].astype(str) + ']'
        df.columns = df.columns.str.replace('[nan]', '')
        df = df.drop(0)

        return df
    

    def get_location(self, 
                     lat: Union[int, float, list, tuple],
                     lon: Union[int, float, list, tuple],
                     **kwargs):
        
        """
        Get location of the station

        Args:

            lat: int or float, latitude; list or tuple, latitude range

            lon: int or float, longitude; list or tuple, longitude range

            radius: int or float, distance in km

            source: str, source of the data

            ellipsoid: str, ellipsoid. Default is "WGS-84", Check geopy.distance.geodesic for more options. ref: https://geopy.readthedocs.io/en/stable/#module-geopy.distance

            year: int, list, tuple, year of the data or range of the year

        RETURNS:
            pandas dataframe  
        """


        if isinstance(lat, (list, tuple)):

            if len(lat) != 2:
                raise ValueError("Latitude should be a list or tuple with 2 elements")

            lat_max = max(lat)
            lat_min = min(lat)

        if isinstance(lon, (list, tuple)):

            if len(lon) != 2:
                raise ValueError("Longitude should be a list or tuple with 2 elements")
            lon_max = max(lon)
            lon_min = min(lon)

        if "soure" in kwargs:
            self.source = kwargs["source"]
        
        if "ellipsoid" in kwargs:
            ellipsoid = kwargs["ellipsoid"]
        else:
            ellipsoid = "WGS-84"

        if "year" in kwargs:
            year = kwargs["year"]
        
        if self.source in source_alias["isd"]: #["ISD", "isd", "NOAA-isd", "noaa-isd", "noaa_isd", "NOAA-ISD"]:
            loc = self.get_meta(load=True, source=self.source, print_info=False)
            loc.dropna(subset=['LAT', 'LON'], inplace=True)
            if isinstance(lat, int) or isinstance(lat, float):
                loc['distance'] = loc.apply(lambda x: distance.geodesic((lat, lon), (x['LAT'], x['LON']),
                                                        ellipsoid=ellipsoid).km,
                                        axis=1)
            elif isinstance(lat, list) or isinstance(lat, tuple):
                loc = loc[(loc['LAT'] <= lat_max) 
                          & (loc['LAT'] >= lat_min) 
                          & (loc['LON'] <= lon_max) 
                          & (loc['LON'] >= lon_min)]
            else:
                raise ValueError("Latitude and Longitude should be int, float, list or tuple")
            
            loc['station_id'] = loc['USAF'].astype(str).replace('\n',"") + loc['WBAN'].astype(str).replace('\n',"")

            if "year" in kwargs:
                loc['year_begain'] = loc['BEGIN'].apply(lambda x: int(str(x)[:4]))
                loc['year_end'] = loc['END'].apply(lambda x: int(str(x)[:4]))

                if isinstance(year, int):
                    loc = loc[(loc['year_begain'] <= year) & (loc['year_end'] >= year)]
                else:
                    loc = loc[(loc['year_begain'] <= year[0]) & (loc['year_end'] >= year[1])]

        if self.source in source_alias['uk']:#["UK-hist_station", "UK-hist-station", "UK_hist_station", "UK_hist-station", "UK_hist_station", "UK_hist-station"]:
            loc = self.get_meta(load=True, source=self.source, print_info=False)
            if isinstance(lat, int) or isinstance(lat, float):
                loc['distance'] = loc.apply(lambda x: distance.geodesic((lat,lon), (x['lat'], x['lon']), 
                                                                    ellipsoid=ellipsoid).km,
                                        axis=1)
            elif isinstance(lat, list) or isinstance(lat, tuple):
                loc = loc[(loc['lat'] <= lat_max) 
                          & (loc['lat'] >= lat_min) 
                          & (loc['lon'] <= lon_max) 
                          & (loc['lon'] >= lon_min)]
            else:
                raise ValueError("Latitude and Longitude should be int, float, list or tuple")
                
            loc['station_id'] = loc['name'].astype(str).lower().replace('\n',"")
            
        if isinstance(lat, int) or isinstance(lat, float):
            if "radius" in kwargs:
                radius = kwargs["radius"]
                res = loc[loc['distance'] < radius]
                if res.shape[0] == 0:
                    print("No station found at point ({}, {}) within {} km".format(lat, lon, radius))
                else:
                    print("Found {} stations at point ({}, {}) within {} km".format(res.shape[0], lat, lon, radius))
            else:
                res = loc[loc['distance'] == loc['distance'].min()]
                print("Closest station found at point ({}, {}) is {}, distance: {} km".format(lat, lon, res['station_id'].values[0], res['distance'].values[0]))

            
        return res
    
        
        
