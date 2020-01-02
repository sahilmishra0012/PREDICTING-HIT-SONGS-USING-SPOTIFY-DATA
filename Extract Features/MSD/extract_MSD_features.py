import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from tqdm import tqdm

client_credentials = SpotifyClientCredentials(client_id = '69d5ceec0f8d42299ac8fce0969a6beb', client_secret = 'f35d4f91afc64282832550504da49790')
spotify = spotipy.Spotify(client_credentials_manager = client_credentials)

data=pd.read_excel('/home/samthekiller/Downloads/Projects/Machine Learning/Spotify/Extract Spotify ID/MSD/MSD_spotify_id_year_1990.xls',header=None)

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

for i in tqdm(data.iterrows()):
    results = spotify.audio_features(i[1][5])
    if results[0]!=None:
        danceability.append(results[0]['danceability'])
        energy.append(results[0]['energy'])
        key.append(results[0]['key'])
        loudness.append(results[0]['loudness'])
        mode.append(results[0]['mode'])
        speechiness.append(results[0]['speechiness'])
        acousticness.append(results[0]['acousticness'])
        instrumentalness.append(results[0]['instrumentalness'])
        liveness.append(results[0]['liveness'])
        valence.append(results[0]['valence'])
        tempo.append(results[0]['tempo'])
        duration_ms.append(results[0]['duration_ms'])
    if results[0]==None:
        danceability.append(-999)
        energy.append(-999)
        key.append(-999)
        loudness.append(-999)
        mode.append(-999)
        speechiness.append(-999)
        acousticness.append(-999)
        instrumentalness.append(-999)
        liveness.append(-999)
        valence.append(-999)
        tempo.append(-999)
        duration_ms.append(-999)

data['danceability']=danceability
data['energy']=energy
data['key']=key
data['loudness']=loudness
data['mode']=mode
data['speechiness']=speechiness
data['acousticness']=acousticness
data['instrumentalness']=instrumentalness
data['liveness']=liveness
data['valence']=valence
data['tempo']=tempo
data['duration_ms']=duration_ms

data.to_excel('MSD_Features.xls',index=False,header=True)
