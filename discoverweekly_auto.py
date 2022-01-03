
"""
Archives your weekly "Discover Weekly" playlist for
browsing through later.

Required Environment variables:
CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, DISCOVER_WEEKLY_ID

Dependencies: spotipy, dotenv

"""

from datetime import date 
import json 
import os 

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# load environment variables
load_dotenv()
CLIENT_ID = os.getenv('client_id')
CLIENT_SECRET = os.getenv('client_secret')
REDIRECT_URI = os.getenv('redirect_uri')
DISCOVER_WEEKLY_ID = os.getenv('discover_weekly_id')


# perform Spotify's Authorization Code Flow for authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='user-read-private playlist-modify-private user-library-modify playlist-modify-public'))

def create_todays_playlist():
    """ Creates a playlist with creation date."""
    today = date.today()
    sp.user_playlist_create('jsochin', f'Discover Weekly for {today}', public=True,
                        description=f'Your Discover Weekly for the week of {today}')

def get_playlist_id():
    """ Gets ID of most recently created playlist ("Discover Weekly for 'today') """
    current_week_playlist_id = ''

    todays_playlist = sp.current_user_playlists(limit=1)

    json_formatted_playlist_str = json.dumps(todays_playlist, indent=2)
    playlist_dict = json.loads(json_formatted_playlist_str)

    for x in playlist_dict['items']:
        current_week_playlist_id = current_week_playlist_id + x['id']

    return current_week_playlist_id

def get_tracks():
    """ Gets track IDs for each track in your current discover weekly.
        Returns a list of formatted URI as per Spotify API Docs. """
    tracks_to_add = []
    uri_list = []
    resp_dict = {}

    discover_weekly_items = sp.playlist_items(DISCOVER_WEEKLY_ID)
    json_formatted_str = json.dumps(discover_weekly_items, indent=2)
    resp_dict = json.loads(json_formatted_str)

    for x in resp_dict['items']:
        tracks_to_add.append(x['track']['id'])

    for item in tracks_to_add:
        uri_list.append(f'spotify:track:{item}')
    
    return uri_list

def add_tracks(uri_list):
    """ Adds each track in uri_list to the newly created playlist. """
    sp.playlist_add_items(get_playlist_id(), uri_list)

def main():
    create_todays_playlist()
    uri_list = get_tracks()
    add_tracks(uri_list)

if __name__ == "__main__":
    main()
