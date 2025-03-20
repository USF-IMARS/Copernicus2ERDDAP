# Copernicus2ERDDAP
Automation for downloading NetCDF files from Copernicus into a directory for ERDDAP.

TODO:
* copernicus credentials in file
* cronjob to run fetch script
* fetch copernicus data using Copernicus API (python?)
* run GenerateDatasetDDS to get dataset.xml for new copernicus dataset

NOTE: could incoporate this into ERDDAP eventually?

## Setup
```bash
pip install openeo
```

### cronjob
```
# get copernicus granule for today
0 0 * * * /usr/bin/python3 /root/Copernicus2ERDDAP/getTodaysGranule.py
```