import pandas as pd
data = pd.read_csv('subset_unique_artists.txt', sep="<SEP>", header=None,engine='python')
data.columns = ["A","B","C","D"]

data.to_csv('artist.csv',header=True,index=False)