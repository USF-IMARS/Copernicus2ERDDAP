"""
Download granule from Copernicus Data Space Ecosystem

This script provides tools for downloading Sentinel-2 granules 
from the Copernicus Data Space Ecosystem for a specified date
or the current date if none is provided.
"""

from pathlib import Path
import openeo
from datetime import datetime
import argparse
import sys

def download_granule(target_date=None):
    """
    Download a Sentinel-2 granule for the specified date.
    If no date is provided, uses the current date.
    
    Args:
        target_date (datetime, optional): Target date to download granule for. Defaults to None (today).
    
    Returns:
        Path: Path to downloaded file
    """
    ## let us create a output directory
    #os.mkdir("results")
    base_path = Path("results")
    base_path.mkdir(exist_ok=True)

    backend_url = "openeo.dataspace.copernicus.eu/"

    eoconn = openeo.connect(backend_url)
    eoconn.authenticate_oidc()

    bbox = [5.0, 51.2, 5.1, 51.3]

    # Use provided date or get the current date
    if target_date is None:
        target_date = datetime.now()
    elif isinstance(target_date, str):
        # Parse string date if provided as string
        target_date = datetime.strptime(target_date, "%Y-%m-%d")

    date_str = target_date.strftime("%Y-%m-%d")
    
    print(f"Loading granule for date: {date_str}")
    # load a data cube for the target date
    s2_bands = eoconn.load_collection(
        "SENTINEL2_L2A",
        temporal_extent=[date_str, date_str],
        spatial_extent=dict(zip(["west", "south", "east", "north"], bbox)),
        bands=["B04", "B08", "SCL"],
        max_cloud_cover=20,
    )

    # assume there is only one granule for the target date
    # TODO: handle multiple granules

    output_file = base_path / f"{date_str}.nc"
    print(f"Saving granule to file {output_file}")
    # save the cube to a netcdf file
    s2_bands.download(output_file, format="NetCDF")
    
    return output_file

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download Sentinel-2 granule for a specific date')
    parser.add_argument('--date', '-d', type=str, help='Date in YYYY-MM-DD format. Defaults to today if not provided.')
    
    # Parse for command line use
    if len(sys.argv) > 1:
        args = parser.parse_args()
        target_date = args.date
    else:
        target_date = None
    
    # Download the granule
    output_file = get_granule(target_date)
    print(f"Successfully downloaded granule to {output_file}")

# This allows the script to be imported as a module or run directly
if __name__ == "__main__":
    main()
