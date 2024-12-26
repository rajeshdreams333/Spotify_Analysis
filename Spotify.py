from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='a31159743e6e45c5b6064d31775bdf93',
    client_secret='9b313fc1b75147318ec88d5ae1848323'
))

artist_url="https://open.spotify.com/artist/1mYsTxnqsietFxj1OgoGbG"

artist_id = re.search(r'artist/([a-zA-Z0-9]+)', artist_url).group(1)

# print(artist_id)

artist=sp.artist(artist_id)

# print(artist)

artist_data={
    'Artist_Name':artist['name'],
    'Artist_Photo_url':artist['images'][0]['url'],
    'Artist_Popularity':artist['popularity'],
    'genres':artist['genres'],
    'followers':artist['followers']['total']
}

print(artist_data)

df=pd.DataFrame([artist_data])
print("\nTrack Data as Dataframe:")
# print(df)

df.to_csv('spotify_artist_track.csv',index=False)

features=['Artist_Popularity','followers']
values=[artist['popularity'],artist['followers']['total']/1000000]
print(values)
plt.figure(figsize=(8,5))
plt.bar(features,values,color='skyblue',edgecolor='red')
plt.title(f"Artist Metadata for '{artist['name']}'")
plt.ylabel('value')
plt.show()