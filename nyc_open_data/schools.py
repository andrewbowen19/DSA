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
        # Using geopandas plot functionality
        df = pd.merge(self.schools, data, how='left', left_on='ATS_CODE', right_on='DBN').fillna(0)
        ax = df.plot(column='# Students Residing in Shelter',
                     markersize=5,
                     cmap='terrain', legend=True)

        ax.set_axis_off()

        if savefig:
            plt.savefig(os.path.join('plots', f'school_data_{column}.pdf'))

    def get_stats(self, path):
        '''
        Prints some stats about the dataset to the screen
        
        parameters:
            path : str; path to datadet desired (using NYC Open Data as default in this script)
        '''
        df = pd.read_csv(path).fillna(0)
        borough_codes = {'M': "Manhattan",
                         'K': 'Brooklyn',
                         'X': 'Bronx',
                         'Q': 'Queens',
                         'R': 'Staten_Island'
                        }

        # Cleaning dataset
        df = df.replace('s', 0) # Some NYC Schools data comes with weird 's' vals
        df = df.loc[:,~df.columns.str.contains('%')]
        for c in df.columns[3::]:
            df[c] = pd.to_numeric(df[c])

        # Constructing some custom columns
        df['Borough'] = [borough_codes[v[2]] for v in df['DBN']]
        df['shelter_pct'] = 100 * df['# Students Residing in Shelter'] / df['# Total Students']

        # Printing out some stats from dataset
        borough_means = df.groupby('Borough')['# Students Residing in Shelter'].mean()
        print('Avg # of nyc public school students in shelters by borough:\n', borough_means)

        print('-------------------------------')
        borough_means = df.groupby('Borough')['# Students Residing in Shelter'].sum()
        print('Total # of nyc public school students in shelters by borough:\n', borough_means)

        print('-------------------------------')
        borough_means = df.groupby('Borough')['shelter_pct'].mean()
        print('Avg % of NY public school students in shelters by borough:\n', borough_means)

        print("#####################################")
        print('Statistics for all NYC:')
        print('Total number of students residing in shelters:')
        print(df['# Students Residing in Shelter'].sum())

        print('Total number of students in temporary housing:')
        sum_temp_housing = df['# Students in Temporary Housing'].sum()
        print(sum_temp_housing)

        print('% of NYC Public School students in temporary housing:')
        pct_temp_housing = round(100 * sum_temp_housing / df['# Total Students'].sum(), 2)
        print(f'{pct_temp_housing}%')


if __name__ == "__main__":
    # Reading in data and plotting scatter
    data_path = os.path.join("data", "2021_Students_In_Temporary_Housing.csv")
    s = schoolPlot()
    s.scatter(data_path, savefig=True)
    plt.show()

    s.get_stats(data_path, False)
