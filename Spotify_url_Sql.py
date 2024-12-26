from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector

sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='a31159743e6e45c5b6064d31775bdf93',
    client_secret='9b313fc1b75147318ec88d5ae1848323'
))

db_config={
    'host':'localhost',
    'user':'root',
    'password':'8096',
    'database':'spotify_db'
}

connection=mysql.connector.connect(**db_config)
cursor=connection.cursor()

file_path='artist_url.txt'
with open(file_path,'r') as file:
    artist_urls=file.readlines()

for artist_url in artist_urls:
    artist_url=artist_url.strip()
    try:
        artist_id = re.search(r'artist/([a-zA-Z0-9]+)', artist_url).group(1)

        artist=sp.artist(artist_id)

        print(artist)

        artist_data={
            'Artist_Name':artist['name'],
            'Artist_Photo_url':artist['images'][0]['url'],
            'Artist_Popularity':artist['popularity'],
            'genres':artist['genres'][0],
            'followers':artist['followers']['total']
        }
        insert_query= """
        INSERT INTO spotify_artist (artist_name,Artist_Photo_url,popularity,genres,followers) 
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            artist_data['Artist_Name'],
            artist_data['Artist_Photo_url'],
            artist_data['Artist_Popularity'],
            artist_data['genres'],
            artist_data['followers']
        ))
        connection.commit()
    except Exception as e:
        print(f"Some error is in {artist_url}, Error: {e}")

cursor.close()
connection.close()


print("All data is insert into database Successfully Please Check the Database once Thank you Have a Nice Day ❤️")
# print(artist_data)

# df=pd.DataFrame([artist_data])
# print("\nTrack Data as Dataframe:")
# # print(df)

# df.to_csv('spotify_artist_track.csv',index=False)

# features=['Artist_Popularity','followers']
# values=[artist['popularity'],artist['followers']['total']/1000000]
# print(values)
# plt.figure(figsize=(8,5))
# plt.bar(features,values,color='skyblue',edgecolor='red')
# plt.title(f"Artist Metadata for '{artist['name']}'")
# plt.ylabel('value')
# plt.show()