import requests
import os
import random
from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def hello_world():
    print("working!!!")
    ############################################################################################################################return '<b>Hello, World!</b>'
    
    load_dotenv(find_dotenv())



    AUTH_URL = 'https://accounts.spotify.com/api/token'
    
    # POST
    auth_response = requests.post(
        AUTH_URL,
        {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        }
    )
    
    # convert the response to JSON
    auth_response_data = auth_response.json()
    
    # save the access token
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
        print(data['tracks'][i]['name'])
        tracklist.append(data['tracks'][i]['name'])
        if i==tracknum:
            trackuri=data['tracks'][i]['uri'][14:]
            trackimage=data['tracks'][i]['album']['images'][0]['url']
            preview=data['tracks'][i]['preview_url']
            

        
       
    
       
     
   ######################################################################################################################################################
   
    return render_template(
        "index.html",
        len = len(tracklist),
        tracks = tracklist,
        artist=artist,
        trackuri=trackuri,
        track=tracklist[tracknum],
        trackimage=trackimage,
        preview=preview
        )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
