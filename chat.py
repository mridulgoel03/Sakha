import cv2
import pyttsx3
import speech_recognition as sr
import openai
from fer import FER
import time
import os
from dotenv import load_dotenv
from diary import log_conversation, log_emotion  # Import log functions

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize text-to-speech engine
def init_tts():
    return pyttsx3.init()

# Function for text-to-speech
def announce(text):
    engine = init_tts()
    engine.say(text)
    engine.runAndWait()

# Function to capture video and detect the initial emotion
def detect_initial_emotion(duration=3):
    cap = cv2.VideoCapture(0)
    detector = FER()
    emotion_counts = {}
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotions in the frame
        result = detector.detect_emotions(frame)
        if result:
            emotion = max(result[0]['emotions'], key=result[0]['emotions'].get)
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

            # Log the detected emotion
            log_emotion(emotion)

        # Display the frame and emotion
        cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Emotion Detection', frame)

        if time.time() - start_time > duration:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if emotion_counts:
        final_emotion = max(emotion_counts, key=emotion_counts.get)
        return final_emotion
    return "Neutral"

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

# Function to get a response from OpenAI's GPT model
def get_chat_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Ensure this is the correct model
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message['content']

# Main function to run the chatbot
def run_chatbot():
    emotion = detect_initial_emotion(duration=3)
    announce(f"You seem {emotion}. How can I assist you?")
    
    while True:
        user_input = recognize_speech()
        
        if user_input.lower() in ["exit", "quit", "stop"]:
            announce("Goodbye!")
            break

        if user_input:
            response = get_chat_response(user_input)
            announce(response)
            print("Chatbot:", response)

            # Log the conversation
            log_conversation(user_input, response)  # Log user input and bot response

if __name__ == "__main__":
    run_chatbot()
