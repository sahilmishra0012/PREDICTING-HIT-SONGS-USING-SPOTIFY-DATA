import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm

client_credentials = SpotifyClientCredentials(client_id = '69d5ceec0f8d42299ac8fce0969a6beb', client_secret = 'f35d4f91afc64282832550504da49790')
spotify = spotipy.Spotify(client_credentials_manager = client_credentials)

data=pd.read_excel('/home/samthekiller/Downloads/Projects/Machine Learning/Spotify/Extract Data/MSD/MSD.xls')

ll=[]
for i in tqdm(data.iterrows()):
    results = spotify.search(q='artist:' + str(i[1]['Artist']) + ' track:' + str(i[1]['Track']), type='track')
    if len(results['tracks']['items'])!=0:
        ll.append(results['tracks']['items'][0]['id'])
    else:
        ll.append(-999)

data['Spotify_ID']=ll
data.to_excel('MSD_spotify_id.xls',index=False,header=False)