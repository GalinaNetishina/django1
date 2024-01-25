import pandas as pd

from pagination.settings import BUS_STATION_CSV

df = pd.read_csv(BUS_STATION_CSV, sep=';', header=0, index_col='global_id', skiprows=[1])
print(df[0:5])