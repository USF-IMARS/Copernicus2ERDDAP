"""
copernicus_to_erddap package

This package provides tools for downloading NetCDF files from Copernicus
into a directory for ERDDAP.
"""

# Export key functions
from .download_granule import get_granule

__version__ = "0.1.0"
