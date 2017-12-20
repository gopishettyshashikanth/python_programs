import pandas as pd
import glob, os
 
os.chdir("/home/user/shashi/Django/progs/CSV/combine_multiple_csv_files_onecsv_file")
results = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob("datayear*")):
    namedf = pd.read_csv(file, skiprows=0, usecols=[1,2])
    results = results.append(namedf)
 
results.to_csv('/home/user/shashi/Django/progs/CSV/combine_multiple_csv_files_onecsv_file/combinedfile.csv')

