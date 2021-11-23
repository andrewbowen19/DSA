# dsa/nyc_open_data/jobs.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Testing out using static methods for this

class jobData:
    
    def __init__(self, data_path):
        '''
        Class to visualize NYC Open data jobs
        '''
        self.data_path = data_path
        self.df = pd.read_csv(self.data_path, nrows=10000)
        
        
    def scatter(self):
        '''Create scatter plot'''
        


if __name__=="__main__":
    
    data_path = os.path.join("data", "DOB_Job_Application_Filings.csv")
    jd = jobData(data_path)
#    jd.get_jobs_d÷ata()
    print(jd.df)
    print(jd.df.columns)

