# spotify-discoverweekly-auto
A Python script to automatically add your "Discover Weekly" playlist to an archive playlist for later use. 
  
# Overview
If you are a frequent user of Spotify, you surely know about the "Discover Weekly" playlist that Spotify updates
each and every week with music recommendations that are tailored to your listening habits. Sadly, the playlist of 
one week is most likely very different from the playlist of another week. 

This Python script solves the problem of missing out on your favorite new song by saving each week's playlist
as another playlist of yours, labeled with the date, so that you never miss out on your next new favorite song.

# Requirements
  - spotipy==2.19.0
  - python-dotenv==0.19.2
  - Python 3.9

# Set Up
You will need to create an Application in you Dashboard on the Spotify for Developers website, https://developer.spotify.com/dashboard/login, under your Spotify account. Once the application is created, a Redirect URI must be given to the Application in the Edit Settings area of the Application dashboard. The URI doesn't have to be an actual viable website, http://localhost:8888 should be just fine for at-home personal use. 

After that, you will need to create a .env file in the directory with discoverweekly_auto.py for your environment variables. You will need the following environment variables:
  - client_id='<the client ID from your application>'
  - client_secret='<the client secret from your application>'
  - redirect_uri='<the redirect URI you gave to your application on the Spotify website>'
  - discover_weekly_id='<the playlist id of your discover weekly playlist for your account>'
  
You can obtain the playlist ID number by going to your Discover Weekly playlist in the Spotify app and clicking Share > Copy Link to Playlist.
Then, you can paste the copied link anywhere and the playlist ID should be the random-looking alphanumeric string after /playlist/ in the URL. 
  
# Use
To use, simply run discoverweekly_auto.py every Monday (or once a week on a schedule) to archive your recommendations. 
