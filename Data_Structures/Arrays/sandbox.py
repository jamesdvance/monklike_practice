
"""
Multiple time series data coming in 
Let’s talk about a problem with multi-channel, time-series data. 
50 streams, sampled at 1 ksamples/second. 5 min of data. 
Walk me through some python pseudocode you might use to load, 
verify channel names and ordering, check for bad channels, 
clean artifacts, and handle dropped packets in data.

# Saved as parquet table

"""

import pandas as pd 

files = [] # *

def load(filename, colnames, type_vals):
    df = pd.read_parquet(filename)
    
    if not all(df.columns.values == colnames):
        raise ValueError(f"columns: {df.columns.values} does not match expected: {colnames}")
    

    type_validations = []
    for i, col in enumerate(colnames):
        type_validations.append(
            df[col].dtype == type_vals[i]
        )

    if not all(type_validations == type_vals):
        raise ValueError(f"data types: {type_validations} does not match expected: {type_vals}")
    
    return df


def validate_values(df, ts, cols):
    
    null_vals = [] 
    for col in df.columns.values:
        null_vals.append(df[col].isnull().sum() > 0)

    same_vals = []
    
    df["second"] = df[ts].date.time.round(1s) # floored at nearest second
    df_grp = df.groupby(["second"]+[cols]).agg({'all_same': lambda x: x.unique() == 1})
    for col in cols:
        same_vals.append(df_grp[col].sum() > 0)


    return null_vals, same_vals




            



