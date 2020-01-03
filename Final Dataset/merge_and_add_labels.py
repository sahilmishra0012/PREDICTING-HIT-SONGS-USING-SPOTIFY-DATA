import pandas as pd
from tqdm import tqdm
billboard_data=pd.read_excel('/home/samthekiller/Downloads/Projects/Machine Learning/Spotify/Extract Features/BillBoard/BillBoard_Features.xls')
billboard_data.drop(['Track','Artist'],axis=1,inplace=True)
msd_data=pd.read_excel('/home/samthekiller/Downloads/Projects/Machine Learning/Spotify/Extract Features/MSD/MSD_Features.xls')
msd_data.drop([0,1,2,3,4],axis=1,inplace=True)
billboard_data['is_hit']=1
billboard_data.drop_duplicates(subset ="SpotifyID", keep = False, inplace = True) 
billboard_ID=list(billboard_data['SpotifyID'])
msd_data.drop_duplicates(subset =5, keep = False, inplace = True) 
k=list(msd_data.columns)
msd_not_hit=pd.DataFrame(columns=k)

SpotifyID=[]
danceability=[]
energy=[]
key=[]
loudness=[]
mode=[]
speechiness=[]
acousticness=[]
instrumentalness=[]
liveness=[]
valence=[]
tempo=[]
duration_ms=[]

for i in tqdm(msd_data.iterrows()):
    if i[1][5] not in billboard_ID:
        SpotifyID.append(i[1][5])
        danceability.append(i[1]['danceability'])
        energy.append(i[1]['energy'])
        key.append(i[1]['key'])
        loudness.append(i[1]['loudness'])
        mode.append(i[1]['mode'])
        speechiness.append(i[1]['speechiness'])
        acousticness.append(i[1]['acousticness'])
        instrumentalness.append(i[1]['instrumentalness'])
        liveness.append(i[1]['liveness'])
        valence.append(i[1]['valence'])
        tempo.append(i[1]['tempo'])
        duration_ms.append(i[1]['duration_ms'])

msd_not_hit[5]=SpotifyID
msd_not_hit['danceability']=danceability
msd_not_hit['energy']=energy
msd_not_hit['key']=key
msd_not_hit['loudness']=loudness
msd_not_hit['mode']=mode
msd_not_hit['speechiness']=speechiness
msd_not_hit['acousticness']=acousticness
msd_not_hit['instrumentalness']=instrumentalness
msd_not_hit['liveness']=liveness
msd_not_hit['valence']=valence
msd_not_hit['tempo']=tempo
msd_not_hit['duration_ms']=duration_ms

msd_not_hit['is_hit']=0

songs_data=pd.concat([billboard_data,msd_not_hit])

billboard_data.rename(columns={"SpotifyID":5},inplace=True)

songs_data=pd.concat([billboard_data,msd_not_hit])

songs_data.to_excel('songs.xls',index=False,header=True)