# Maintenance Log updates launch pad

import streamlit as st

def feature_script():
#   Description
    st.write("This app embeds a YouTube video and plays it within the browser.")
    st.write("⚠️ - Note : the video make take some seconds befote it plays.t")

#   YouTube video URL
    video_url = "https://www.youtube.com/watch?v="

#   hEmbed the video in the app
    st.video(video_url)

    return
