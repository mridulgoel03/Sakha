import streamlit as st
import subprocess
import pandas as pd
import datetime
import os

# Function to log emotions
def log_emotion(emotion):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('emotion_log.txt', 'a') as f:
        f.write(f"{timestamp}: {emotion}\n")

# Function to read logged emotions
def read_emotions():
    if os.path.exists('emotion_log.txt'):
        with open('emotion_log.txt', 'r') as f:
            return f.readlines()
    return []

# Function to plot mood trends
def plot_mood_trends(emotions):
    df = pd.DataFrame(emotions, columns=["Log"])
    df["Emotion"] = df["Log"].str.split(": ").str[1]
    emotion_counts = df["Emotion"].value_counts()

    st.bar_chart(emotion_counts)

# Streamlit UI
st.title("Emotion Detection System")

# Sidebar for navigation
st.sidebar.header("Navigation")
option = st.sidebar.selectbox("Choose an option:", ["Home", "Run Chatbot", "View Emotions Log", "Show Mood Trends", "Support Resources"])

# Main application logic based on user selection
if option == "Home":
    st.write("Welcome to the Emotion Detection System!")
    st.write("Select options from the sidebar to proceed.")

elif option == "Run Chatbot":
    if st.button("Start Chatbot"):
        # Run the chatbot from chat.py
        subprocess.run(["python", "chat.py"])

elif option == "View Emotions Log":
    emotions = read_emotions()
    if emotions:
        st.write("Logged Emotions:")
        for entry in emotions:
            st.write(entry.strip())
    else:
        st.warning("No emotions logged yet.")

elif option == "Show Mood Trends":
    emotions = read_emotions()
    if emotions:
        plot_mood_trends(emotions)
    else:
        st.warning("No emotions logged yet.")

elif option == "Support Resources":
    st.subheader("Supportive Resources")
    st.write("If you're feeling low, here are some resources you can consider:")
    st.write("- **Crisis Text Line:** Text HOME to 741741 for 24/7 support.")
    st.write("- **National Suicide Prevention Lifeline:** Call 1-800-273-TALK (1-800-273-8255).")
    st.write("- **BetterHelp:** [Visit BetterHelp](https://www.betterhelp.com) for online therapy.")
    st.write("- **Mindfulness Apps:** Consider trying mindfulness apps like Headspace or Calm for stress relief.")
    st.write("- **Journaling:** Writing about your feelings can help. Use our logging feature to keep track of your emotions.")

