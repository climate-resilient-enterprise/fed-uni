# fed-uni

Code to process data from partnership with Federation University

## Fixing file metadata

The FFDI files (as associated variables) from Federation Uni have a number of issues with file metadata:
- The time axis is called `date` and the values are date strings
- The latitude and longitude coordinates have no attributes (e.g. units, long name, standard name etc)

The `fix_metadata.py` command line script fixes those issues.
It takes a Fed Uni file name and an output file name as inputs.
e.g.

```
$ python fix_metadata.py /g/data/wp00/ffdi/corrected/rainfall/prate_1910.nc prate-fixed_1910.nc
```

In order for the script to run you must have the `xarray` and `netcdf4` libraries installed.
