# fed-uni

Code to process data from our partnership with Federation University.

## Fixing file metadata

The FFDI files (as associated variables) from Federation Uni have a number of issues with file metadata:
- The time axis is called `date` and the values are date strings
- The latitude and longitude coordinates have no attributes (e.g. units, long name, standard name etc)

The `fix_metadata.py` command line script fixes those issues.
It takes a Fed Uni file name and an output file name as inputs.

The easiest way to use the command line script is to use the cloned copy at `/g/data/wp00/fed-uni/code/fix_metadata.py`.
It can be run using the Python environment at `/g/data/wp00/dbi599/miniconda3/envs/cih/bin/python`.
For example, to create a fixed precipitation file for the year 1995 you can run:

```
$ /g/data/wp00/dbi599/miniconda3/envs/cih/bin/python /g/data/wp00/fed-uni/code/fix_metadata.py /g/data/wp00/fed-uni/data/corrected/rainfall/prate_1995.nc prate-fixed_1995.nc
```

