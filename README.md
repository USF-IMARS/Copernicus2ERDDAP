# Copernicus2ERDDAP
Automation for downloading NetCDF files from Copernicus into a directory for ERDDAP.

TODO:
* copernicus credentials in file
* fetch copernicus data using Copernicus API (python?)
* run GenerateDatasetDDS to get dataset.xml for new copernicus dataset

NOTE: could incoporate this into ERDDAP eventually?

## Setup
```bash
pip install openeo
```

## Usage

### Command Line
You can run the script from the command line with an optional date parameter:

```bash
# Download granule for today
python download_granule.py

# Download granule for a specific date
python download_granule.py --date 2025-03-20
# or
python download_granule.py -d 2025-03-20
```

### Airflow Integration
The script can be called from Airflow by importing the `get_granule` function. An example DAG is provided in `example_airflow_dag.py`.

The function accepts a date parameter (string in format 'YYYY-MM-DD' or datetime object) or defaults to the current date if none is provided.

```python
# In your Airflow task
from download_granule import get_granule

# With a specific date
output_file = get_granule('2025-03-20')
# Or use Airflow's execution_date
output_file = get_granule(execution_date.strftime('%Y-%m-%d'))
```

### cronjob
```bash
# get copernicus granule for today
0 0 * * * cd /home/tylar/repos/Copernicus2ERDDAP/ && /usr/bin/python3 /root/Copernicus2ERDDAP/download_granule.py