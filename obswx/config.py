config = {
    "meta": {
        "noaa": "https://www.ncei.noaa.gov/pub/data/noaa/isd-history.csv",
        "uk": "https://raw.githubusercontent.com/envdes/envdes.github.io/main/_data/UK-hist-stataion-meta.csv",
        "hadisd": "https://www.metoffice.gov.uk/hadobs/hadisd/v341_202403p/files/hadisd_station_info_v341_202403p.txt",
    },
    "isd": {
        "aws":" https://noaa-global-hourly-pds.s3.amazonaws.com/{}/{}.csv",
        "noaa": "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/{}/{}.csv",
        "hadisd" : "https://www.metoffice.gov.uk/hadobs/hadisd/v341_202403p/data/hadisd.3.4.1.202403p_19310101-20240401_{}.nc.gz"
    },
    "map": {
        "isd": "https://envdes.github.io/obswx/isd_map",
        "uk": "https://envdes.github.io/obswx/UK-hist-station-map",
        "hadisd": "https://envdes.github.io/obswx/hadisd_map",
    },
}

source_alias = {"isd": ["ISD", "isd", "NOAA-isd", "noaa-isd", "noaa_isd", "NOAA-ISD"],
                "hadisd": ["HadISD", "hadisd", "Hadisd", "HADISD", "Had-isd", "had-isd", "HAD-ISD", "Had-isd"],
                "uk": ["UK-hist_station", "UK-hist-station", "UK_hist_station", "UK_hist-station", "UK_hist_station", "UK_hist-station"],
                "aws": ["AWS", "aws", "S3", "s3"],
                "noaa": ["NOAA", "noaa", "NOAA-isd", "noaa-isd", "noaa_isd", "NOAA-ISD"],}