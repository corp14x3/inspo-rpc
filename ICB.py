from selenium import webdriver
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = 'spotify api client id'
client_secret = 'spotify api client secret'
redirect_uri = 'http://localhost:8888/callback'

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
options.profile = r"ur mozilla profile path"

browser = webdriver.Firefox(options=options)
browser.get("https://www.instagram.com/accounts/edit/")

def changer(biog):
    bio = browser.find_element(by="xpath",value='//*[@id="pepBio"]')
    bio.clear()
    bio.send_keys(f"{biog}")
    button = browser.find_element(by="xpath",value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/article/form/div[5]/div/div/div").click()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-read-playback-state'))

last_song = None

while True:
    try:
        current_track = sp.current_playback()
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        if track_name != last_song:
            changer(biog=f"""https://github.com/corp14x3\n{track_name} - {artist_name}\noyle iste..""")
        else:
            continue   
        last_song = track_name
    except:
        pass