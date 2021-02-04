import requests
import os
from dotenv import load_dotenv, find_dotenv




####################################################GETTING AUTHORIZATION TOKEN DYNAMICALLY
AUTH_URL = 'https://accounts.spotify.com/api/token'


authtest="Basic " + os.getenv('CLIENTID') + ":" + os.getenv('CLIENTSECRET')

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'Authorization': authtest,
})


auth_response_data = auth_response.json()

print(auth_response_data)

access_token = auth_response_data['access_token']









url="https://api.spotify.com/v1/search/"

load_dotenv(find_dotenv())

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

params={
    'q':"weeknd"
    
}

api_response=requests.get(
    "https://api.spotify.com/v1/search?q=the%20weeknd&type=artist",
    headers = headers
)

data=api_response.json()
print(data)