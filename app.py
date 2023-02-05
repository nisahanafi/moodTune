import streamlit as st
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import test
import random

st.experimental_memo(suppress_st_warning= True)
client_id = '1224aac3c7a44e6da69f8ce6d5cdea24' #my given client id from spotify for developers website
client_secret = '41203fae0cb241b581752e5cf7fdc82d' #my client secret id from spotify for developers website

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)

#creating sections in streamlit web app
header  = st.container()
inp = st.container()
pred = st.container()
confirm = st.container()

with header:
    st.image('background.jpg')
    st.title('Recommending Songs Based on Human Facial Expression and Emotion')
    st.markdown('**Using this web app, you can discover and listen to the songs that suits your mood to lift them up!**')

with inp:
    st.title("Firstly, Let's Capture Your Emotion") 
    st.markdown("**Capturing a picture of you now, press 'Spacebar' to take the picture**")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    test.take_input() #sends input to another python file/module 'test.py', to run the take_input function in test.py

with pred:
    st.image('your emotion.jpg')
    img = cv2.imread('your emotion.jpg')

    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) 

    #This line uses the Deep Face lightweight package function to detect the emotions from 'your emotion.jpg'
    predictions = DeepFace.analyze(img,actions=['emotion'])


    #This line displays the current emotion captured, in text
    st.markdown("**Your current emotion is {}**".format(predictions['dominant_emotion']))  
    emotions = predictions['dominant_emotion']

#the whole function that connects with Spotify and returns a playlist of songs according to emotion shown
def recommend_music(mood):
    if(mood == 'happy'): 

            st.markdown("** 😀😸 Keep those smiles up! 😸😀 **")
            playlistHappy_id = '5fIkdOvzIJFdsMm4ku6kKg' #find a happy playlist


            def get_track_ids(playlistHappy_id):
                music_id_list = []
                playlist = sp.playlist(playlistHappy_id)

                for item in playlist['tracks']['items']:
                    music_track = item['track']
                    music_id_list.append(music_track['id'])
                return music_id_list #returning happy playlist 

            track_ids = get_track_ids(playlistHappy_id) 

            for i in range(5):

                random.shuffle(track_ids)

                my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="500" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

                st.markdown(my_html, unsafe_allow_html=True)
    #for sad emotions detected
    
    elif(mood == 'sad'):

        st.markdown("**😞😿 You look sad, here are some songs to match with your mood 😿😞 **")
        playlistSad_id = '7mtSYElQ8yW0AzGg2zgwTY' #right now im using a public playlist for sad songs

        def get_track_ids(playlistSad_id):
            music_id_list = []
            playlist = sp.playlist(playlistSad_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlistSad_id)

        for i in range(5):
            
            random.shuffle(track_ids)

            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="500" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html=True)

    #for anger emotions detected
    
    elif(mood == 'angry'): 

        st.markdown("**😡😾 You're looking angry, let's match that mood! 😾😡**")
        playlistAnger_id = '3XxLW4c1azOyKLIfB9IQfL' #playlist id for anger emotions (to be changed)

        def get_track_ids(playlistAnger_id):
            music_id_list = []
            playlist = sp.playlist(playlistAnger_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlistAnger_id)

        for i in range(5):
            
            random.shuffle(track_ids)
            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="500" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html = True)


    #for fear emotions detected

    elif(mood == 'fear'): 

        st.markdown("**😨🙀 Here are some songs to calm yourself from the fear! 🙀😨**")
        playlistFear_id = '2ff9I3txL0E2OiDkLsTwv0' #playlist id for fear emotions (to be changed)

        def get_track_ids(playlistFear_id):
            music_id_list = []
            playlist = sp.playlist(playlistFear_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlistFear_id)

        for i in range(5):
            
            random.shuffle(track_ids)
            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="500" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html = True)


    #for surprise emotions detected

    elif(mood == 'surprise'): 

        st.markdown("**😱🙀 Looks like you are surprised :0 Here are some songs to calm that mood 🙀😱**")
        playlistSurprise_id = '4Gjx6v1d7cyYUtL4VhAmj6' #playlist id for surprise emotions (to be changed)

        def get_track_ids(playlistSurprise_id):
            music_id_list = []
            playlist = sp.playlist(playlistSurprise_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlistSurprise_id)

        for i in range(5):
            
            random.shuffle(track_ids)
            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="500" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html = True)
    

    #for neutral emotions detected

    elif(mood == 'neutral'): 

        st.markdown("**😚😺 Here are some songs for you to explore! 😺😚**")
        playlistNeutral_id = '784NGRLmstvVUpzlaka15c' #playlist id for neutral emotions (to be changed)

        def get_track_ids(playlistNeutral_id):
            music_id_list = []
            playlist = sp.playlist(playlistNeutral_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlistNeutral_id)

        for i in range(5):
            
            random.shuffle(track_ids)
            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="500" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html = True)
        
with confirm:
    st.title("The Songs That Represent Your Emotion ")
    recommend_music(emotions)

    #st.markdown("Emotion shown not correct?")
    st.markdown("**PRESS 'r' TO CAPTURE YOUR EMOTION AGAIN! 🙌👀**")
   
#to run type python -m streamlit run app.py


# my problem right now:
# 1.  streamlit keeps running my web app everytime i click a button or radio button
# 2. tried st.form + st.form_submit_button, st.session_state, st.checkbox but none of them works, even after clearing cache
# 3. i suspect that its because of the data that is stored from taking pictures to be analyzed even after reloading, which somehow
#    changes the session state



