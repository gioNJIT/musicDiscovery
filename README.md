# project1-gd263

## Table of contents
* [General info](#general-info)
* [Bug Fixes](#Bug-Fixes)
* [Files involved](#files-involved)
* [Technologies](#technologies)
* [Setup](#setup)
* [Possible errors](#Possible-errors)

## General info
This project takes a hard coded set of artists and randomly displays one of the artist's top tracks along with album art, link to a lyrics page and a song preview.

## Bug Fixes
Added a loop that will take the top three search results for a song and will compare them to the artist name. This way, if there is a more famous song with the same title, that songs preview wont play unless the artist matches.

Instead of an error in place of the MP4 player if a preview is not found, the user will get rickrolled and will be warned that a preview was unavailable.
Prior to this, an ugly unavailable box would show making it look like the preview hadnt loaded.

## Files involved
### IMPORTANT: there is a .env file that you do not see. This file exports the necessary keys so that your python can use them without having them hardcoded in. 
Below are the contents of the .env file:

export CLIENT_ID="spotify client id"

export CLIENT_SECRET="spotify secret key"

export GENIUS_KEY="genius key"

the .env file should be in the same location as your python script

HTML file is going to be stored in a folder called "templates". CSS file needs to be stored in a file called static. The python file just needs to be in the parent directory of both of the previous files.

## Technologies
Project is created with:
* HTML/CSS
* PYTHON
* GENIUS and SPOTIFY API
* Heroku
	
## Setup
### IMPORTANT: It is assumed that you have python and pip installed


To run this project, install the following:

```
$ $ pip install Flask
```

your main file should hold spotifyapp.py, .env, static, and template. (static and template are folders and .env is a file mentioned in files section).


## Possible errors
if youre getting a key error for the data returned from the api:

check to make sure your .env file has the correct keys and that the contents of the .env file are exactly as shown in the files section. example line from above:

export CLIENT_ID="@#$Jnk2j4NJq@#$kj@n#$jkkNJ23K4"

^^keep the quotations. you should only be changing the text inside the quotes.


### readme format credit: https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
