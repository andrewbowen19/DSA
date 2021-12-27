# dsa/nyc_open_data/jobs.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class jobData(object):
    
    def __init__(self, data_path):
        '''
        Class to visualize NYC Open data jobs
        '''
        self.data_path = data_path
        self.df = pd.read_csv(self.data_path, nrows=10000) # remove this nrows arg for the whole shebang
        
        
    def scatter(self, x_label, y_label, df=None):
        '''
        Create scatter plot
        
        parameters:
            x_label, y_label : str; self.df column names to be plotted on x and y axis, respectively
            df : pd.DataFrame, default None; if passed
        '''

        x = df[x_label] if df else self.df[x_label]
        y = df[y_label] if df else self.df[y_label]
        f, ax = plt.subplots()
        ax.scatter(x, y)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)


if __name__=="__main__":
    
    data_path = os.path.join("data", "DOB_Job_Application_Filings.csv")
    jd = jobData(data_path)
#    jd.get_jobs_d÷ata()
    print(jd.df.head())
    print(jd.df.columns)
#    print(jd.df['Approved'])
    # print(jd.df["Owner's Last Name"].loc[jd.df['Approved']!="NaN"].value_counts())

    # jd.scatter('')

    print(jd.df[["Street Name",'Block']])
    

