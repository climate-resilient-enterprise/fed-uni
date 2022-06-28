"""Command line program for fixing the metadata in Federation Uni files."""

import argparse

import numpy as np
import xarray as xr
import cmdline_provenance as cmdprov


def main(args):
    """Run the program."""
    
    ds = xr.open_dataset(args.infile)
    time_values = np.array([np.datetime64(date) for date in ds['date'].values])
    time_values = time_values.astype('datetime64[ns]')
    ds = ds.rename({'date': 'time', 'latitude': 'lat', 'longitude': 'lon'})
    ds = ds.assign_coords({'time': time_values})
    ds['time'].attrs = {
        'axis': 'T',
        'long_name': 'time',
        'standard_name': 'time'
    }
    ds['lat'].attrs = {
        'units': 'degrees_north',
        'axis': 'Y',
        'long_name': 'Latitude',
        'standard_name': 'latitude'
    }
    ds['lon'].attrs = {
        'units': 'degrees_east',
        'axis': 'X',
        'long_name': 'Longitude',
        'standard_name': 'longitude'
    }
    ds.attrs['history'] = cmdprov.new_log()
    ds.to_netcdf(args.outfile, unlimited_dims='time')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )     
    parser.add_argument("infile", type=str, help="input files")
    parser.add_argument("outfile", type=str, help="output file name")
    args = parser.parse_args()
    main(args)

