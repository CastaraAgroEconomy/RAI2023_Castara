# Compliance Report generation launch pad
import streamlit as st

# Description
st.write("This app embeds a YouTube video and plays it within the browser.")
st.write("⚠️ Note: it may take a few seconds before the video begins to play.")

# YouTube video URL
video_url = "https://www.Youtube.com/watch?v=v08sZvHyMtw"

# Embed the video in the app
st.video(video_url)

return
