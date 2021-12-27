# nyc_open_data/schools.py

'''Script to analyze educational data posted on NYC Open Data'''

import geopandas
import pandas as pd
import matplotlib.pyplot as plt
import os

sample_zipfile = os.path.join("data", "Public_School_Locations.zip")

class schoolPlot:

    def __init__(self, zipfile=sample_zipfile):
        self.zipfile = zipfile
        self.schools = geopandas.read_file(self.zipfile)
        self.zip_codes = geopandas.read_file(os.path.join('data', 'ZIP_CODE_040114.zip'))
        
    
    def scatter(self, path: str, column: str = '# Students Residing in Shelter', savefig: bool = False):
        '''
        Produces a scatter plot of NYC Schools Data for a given data file (csv) and column
        
        parameters:
            path : path to data file to be read
            columns : str; column name from dataframe to be plotted
            savefig : bool; if True, figure is saved to plots dir
        '''
        data = pd.read_csv(path).fillna(0)
        data = data.replace('s', 0) # Some NYC Schools data comes with weird 's' vals
        data = data.loc[:,~data.columns.str.contains('%')]
        for c in data.columns[3::]:
            data[c] = pd.to_numeric(data[c])

        # Merging School locs with school data
        df = pd.merge(self.schools, data, how='left', left_on='ATS_CODE', right_on='DBN').fillna(0)
        ax = df.plot(column='# Students Residing in Shelter',
                   markersize=5,
                   cmap='terrain')

        ax.set_axis_off()
        
        if savefig:
            plt.savefig(os.path.join('plots', f'school_data_{column}.pdf'))

    def arts_plot(self):
        '''Create plot exploring student access to arts
        
        https://data.cityofnewyork.us/Education/2021-Arts-Data-Report/9h53-fsqa

        parameters:

        '''
        df = pd.read_csv("data/2021_Arts_Data_Report.csv")
        print(df.head())
        print(df.columns)
        for c in df.columns:
            print(c)


    


if __name__ == "__main__":
    # Reading in data and plotting scatter
    data_path = os.path.join("data", "2021_Students_In_Temporary_Housing.csv")
    s = schoolPlot()
    # s.scatter(data_path, savefig=True)
    # plt.show()
    s.arts_plot()