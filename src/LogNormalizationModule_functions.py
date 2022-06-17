import pandas as pd
import cmapPy.pandasGEXpress.GCToo as GCToo
import math
from cmapPy.pandasGEXpress.write_gct import write
#!/usr/bin/env python3
#NB - all of these import statements should specify their versions and be executed in a separate script at Docker build time.
# Here is where I'd put my functions, if I had any!
def empty_function():
    return

def gct2df (file , summary = False): # convert the given gct file to dataframe 
    df =  pd.read_csv(file, sep='\t',skiprows=2) 
    # we will skip the first two rows as they do not contain the biological data 
    if summary:   
        print("number of rows imported", df.shape[0], "\number of columns imported", df.shape[1])
        
    return df

def lognormalize(df):
    for i in range(len(df)):
        for j in range(1, len(df.iloc[i,0])):
            if type(df.iloc[i,j]) is str:
              continue
            if df.iloc[i,j] <= 0:
                df.iloc[i,j]  = 0
            else: 
                df.iloc[i,j] = math.log(df.iloc[i,j])
    return df

def df2gct(df, output_filename):
    gctoo_instance = GCToo.GCToo(df)
    write(gctoo_instance, output_filename + '.gct')