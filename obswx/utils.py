import xarray as xr
import shutil
import os
import gzip

def read_hadisd(**kwargs):
    """
    Read HadISD data from a file.
    
    Args:
        path (str): Path to the file.
        output (str): Path to the output file.
    """
    
    if kwargs:
        if "path" in kwargs:
            path = kwargs["path"]
        else:
            raise ValueError("No file path provided.")
        
        if "output" in kwargs:
            output = kwargs["output"]
        else:
            output = path.replace(".gz", "")

    else:
        raise ValueError("No file path provided.")

    
    if path.endswith(".gz"):
        with gzip.open(path, 'rb') as f_in:
            with open(output, 'wb') as f_out:
                print("Extracting {} to {}" .format(path, output))
                shutil.copyfileobj(f_in, f_out)
        path = output
    elif path.endswith(".nc"):
        path = path
    else:
        raise ValueError("Invalid file format, only .nc and .gz are supported.")

    return xr.open_dataset(output)