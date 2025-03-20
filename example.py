from pathlib import Path
import openeo
from openeo import processes as eop
from shapely.geometry import box
import matplotlib.pyplot as plt
import xarray as xr
import os
from numpy import datetime_as_string
from datetime import datetime

## let us create a output directory

#os.mkdir("results")
base_path = Path("results")

backend_url = "openeo.dataspace.copernicus.eu/"

eoconn = openeo.connect(backend_url)
eoconn.authenticate_oidc()

bbox = [5.0, 51.2, 5.1, 51.3]

# Get the current date
current_date = datetime.now()

startdate = current_date.strftime("%Y-%m-%d")
enddate = current_date.strftime("%Y-%m-%d")

print(f"loading granule {startdate} to {enddate}")
# load a data cube for the current date
s2_bands = eoconn.load_collection(
    "SENTINEL2_L2A",
    temporal_extent=[startdate, enddate],
    spatial_extent=dict(zip(["west", "south", "east", "north"], bbox)),
    bands=["B04", "B08", "SCL"],
    max_cloud_cover=20,
)

# assume there is only one granule today 
# TODO: handle multiple granules

print("saving granule to file {base_path / f'{startdate}.nc'}")
# save the cube to a netcdf file
s2_bands.download(base_path / f"{startdate}.nc", format="NetCDF")
