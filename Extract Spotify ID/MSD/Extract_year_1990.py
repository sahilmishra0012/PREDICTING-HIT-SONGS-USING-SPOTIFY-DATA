import pandas as pd
data=pd.read_excel('MSD_spotify_id_non_null_year.xls',header=None)
data=data[data[3]>=1990]
data.to_excel('MSD_spotify_id_year_1990.xls',index=False,header=False)