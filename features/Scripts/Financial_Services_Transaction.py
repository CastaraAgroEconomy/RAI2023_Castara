#    Financial Services Transaction feature launch pad
import streamlit as st

def feature_script():
#   Description
    st.write("This app embeds a YouTube video and plays it within the browser.")
    st.write("⚠️ - Note : the video make take some seconds before it plays.")

#   YouTube video URL
    video_url = "https://www.youtube.com/watch?v=YFtW1YD-5WY&t=630"
  
#   Embed the video in the app
    st.video(video_url)

    return