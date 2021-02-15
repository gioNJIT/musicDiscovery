import requests
import os
import random
from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
from datetime import datetime


app = Flask(__name__)

@app.route('/')#           connects route with function below
def spotifyapp():


    load_dotenv(find_dotenv())


############RETRIEVING TOKEN USING CREDENTIALS FOUND IN .ENV FILE
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    
    auth_response = requests.post(
        AUTH_URL,
        {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        }
    )
    
    # SAVING TEXT IN JSON FORMAT
    auth_response_data = auth_response.json()
    
    # SAVING TOKEN
    access_token = auth_response_data['access_token']
    
    
    
    url_list=['THE WEEKND','THE DRUMS','MAC DEMARCO']
    
    url_dict={'THE WEEKND':"https://api.spotify.com/v1/artists/1Xyo4u8uXC1ZmMpatF05PJ/top-tracks",'THE DRUMS':"https://api.spotify.com/v1/artists/0p5axeJsbtTCXBrRVoKjwu/top-tracks",'MAC DEMARCO':"https://api.spotify.com/v1/artists/3Sz7ZnJQBIHsXLUSo0OQtM/top-tracks"}
    #weekndurl="https://api.spotify.com/v1/artists/1Xyo4u8uXC1ZmMpatF05PJ/top-tracks"
    #drumsurl="https://api.spotify.com/v1/artists/0p5axeJsbtTCXBrRVoKjwu/top-tracks"
    #macurl="https://api.spotify.com/v1/artists/3Sz7ZnJQBIHsXLUSo0OQtM/top-tracks"
    
    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    params={
        'market':'US',
    }
    tracklist=[]
    random.seed(datetime.now())
    tracknum=random.randint(0,9)
    preview=''
    
       
    
    artist=random.choice(url_list)
    
    api_response=requests.get(
        url_dict[artist],
        params=params,
        headers = headers,
    )
    
    data=api_response.json()
    for i in range(10):
        #print(data['tracks'][i]['name'])
        tracklist.append(data['tracks'][i]['name'])
        if i==tracknum:
            trackuri=data['tracks'][i]['uri'][14:]
            trackimage=data['tracks'][i]['album']['images'][0]['url']
            preview=data['tracks'][i]['preview_url']
    
    rickRL="https://p.scdn.co/mp3-preview/22bf10aff02db272f0a053dff5c0063d729df988?cid=774b29d4f13844c495f206cafdad9c86"

####################################################genius lyrics section below        
       
    base_url = 'https://api.genius.com'

    song = tracklist[tracknum]

    path = 'search/'
    request_uri = '/'.join([base_url, path])
    
    
    params = {'q': song}
    
    token = 'Bearer {}'.format(os.getenv('GENIUS_KEY'))
    headers = {'Authorization': token}
    
    r = requests.get(request_uri, params=params, headers=headers)  
    geniusdata=r.json()
    
    
    artistlow=artist.lower()
    song_url=geniusdata['response']['hits'][0]['result']['url']
    for x in range(3):
        checkartist=geniusdata['response']['hits'][x]['result']['full_title']
        if artistlow in checkartist.lower().replace(' ',' '):
            break
        
    PHRASE="preview"
    print("preview")    
    if preview==None:
        preview=rickRL
        PHRASE="Sorry, no preview available"
     
    PHRASE   
   ###################### SENDING DATA TO HTML FILE 
   
    return render_template(
        "index.html",
        len = len(tracklist),
        tracks = tracklist,
        artist=artist,
        trackuri=trackuri,
        track=tracklist[tracknum],
        trackimage=trackimage,
        preview=preview,
        song_url=song_url,
        PHRASE=PHRASE
        )
        
        
     
        
    


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'), #setting app up to be an externally visible server
    debug=True
)
