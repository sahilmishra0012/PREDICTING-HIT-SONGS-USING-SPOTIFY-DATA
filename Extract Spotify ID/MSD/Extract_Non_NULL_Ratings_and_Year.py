import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm

client_credentials = SpotifyClientCredentials(client_id = '69d5ceec0f8d42299ac8fce0969a6beb', client_secret = 'f35d4f91afc64282832550504da49790')
spotify = spotipy.Spotify(client_credentials_manager = client_credentials)

data=pd.read_excel('MSD_spotify_id.xls',header=None)

data=data[data[5]!=-999]
zero_year_data=data[data[3]==0]

ll=[]
for i in tqdm(zero_year_data.iterrows()):
    results = spotify.search(q='artist:' + str(i[1][0]) + ' track:' + str(i[1][2]), type='track')
    if len(results['tracks']['items'])!=0:
        ll.append(results['tracks']['items'][0]['album']['release_date'][0:4])
    else:
        ll.append(-999)

non_zero_year_data=data[data[3]!=0]
zero_year_data[3]=ll
new_data=pd.concat([zero_year_data,non_zero_year_data])
new_data.to_excel('MSD_spotify_id_non_null_year.xls',index=False,header=False)

