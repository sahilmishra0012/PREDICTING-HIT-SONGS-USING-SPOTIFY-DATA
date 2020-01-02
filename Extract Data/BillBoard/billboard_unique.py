import pandas as pd
from tqdm import tqdm

data=pd.read_csv('billboard.csv',header=None)

artists=[]
tracks=[]

for i in tqdm(range(data.shape[0])):
    for j in range(data.shape[1]):
        k=tuple(data.iloc[i][j].split(', '))
        tracks.append(k[0][2:-1])
        artists.append(k[1][1:-1])

new_data=pd.DataFrame(columns=['Track','Artist'])
new_data['Track']=tracks
new_data['Artist']=artists
new_data.drop_duplicates(keep="first", inplace=True)
new_data.to_excel('billboard_unique.xls',header=None,index=False)