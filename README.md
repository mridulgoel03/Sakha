# Sakha : Emotion Detection System



## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [Acknowledgments](#acknowledgments)

---

## Overview

The **Emotion Detection System** is an advanced interactive chatbot engineered to understand and respond to user emotions through cutting-edge technology. By harnessing the power of **computer vision** and **natural language processing**, this system effectively analyzes **facial expressions** and **voice inputs** to deliver a personalized conversational experience. The application is designed to enhance user interaction by accurately recognizing emotions and providing empathetic responses.

---

## Features

| Feature                       | Description                                                                                               |
|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Emotion Detection**         | Utilizes the **FER** library to analyze users' facial expressions in real time.                          |
| **Voice Interaction**         | Enables users to communicate naturally through speech using the **SpeechRecognition** library.            |
| **Text-to-Speech**           | Converts chatbot responses into spoken words utilizing the **pyttsx3** library for better engagement.     |
| **Conversation Logging**      | Automatically records user interactions in a diary log for future reference and self-reflection.          |
| **Emotion Logging**           | Tracks and logs detected emotions over time to provide insights into emotional trends.                    |
| **Mood Trend Visualization**  | Presents a graphical representation of logged emotions using **Streamlit**, making it easy to interpret trends.|

---

## Requirements

To run the Emotion Detection System, ensure you have **Python 3.x** installed, along with the following libraries:

| Library               | Description                                                 |
|-----------------------|-------------------------------------------------------------|
| `openai`              | Integrates OpenAI's API for natural language processing capabilities. |
| `opencv-python`       | Provides functionalities for real-time computer vision tasks.      |
| `fer`                 | Implements facial expression recognition for emotion detection.   |
| `SpeechRecognition`   | Facilitates voice command input for user interaction.            |
| `pyttsx3`            | Converts text responses into speech for a more engaging experience. |
| `streamlit`          | Enables the creation of a user-friendly web interface for interaction. |
| `pandas`              | Supports data manipulation and analysis for emotion tracking.    |
| `python-dotenv`      | Loads environment variables from a `.env` file for configuration. |

### Installation

You can easily install the necessary libraries using `pip`. Run the following command in your terminal:

```bash
pip install openai opencv-python fer SpeechRecognition pyttsx3 streamlit pandas python-dotenv

```

---

## Setup

Follow these steps to set up the Emotion Detection System:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Environment Configuration**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Running the Application**:
   - To launch the chatbot, execute:
   ```bash
   python chat.py
   ```
   - To access the Streamlit interface, run:
   ```bash
   streamlit run app.py
   ```

---

## Usage

- **Initiate the Chatbot**: Start the chatbot to detect your initial emotional state through webcam input.
- **Interact with the Chatbot**: Use voice commands to express your thoughts and feelings; the chatbot will respond accordingly.
- **Review Logs**: Access the Streamlit interface to view logged conversations and emotional trends, facilitating self-reflection.

---

## Future Enhancements

We aim to continuously improve the Emotion Detection System with the following features:

| Future Feature              | Description                                                    |
|-----------------------------|----------------------------------------------------------------|
| **Advanced Emotion Recognition** | Incorporate state-of-the-art machine learning models for more accurate emotion detection. |
| **Multi-language Support**  | Enable the chatbot to understand and respond in multiple languages, expanding accessibility. |
| **User Profiles**           | Allow users to create personal profiles to store their interaction history for customized responses. |
| **Sentiment Analysis**      | Implement sentiment analysis techniques to enhance context understanding and improve response quality. |
| **Data Export Functionality** | Enable users to export their logs (conversations and emotions) in various formats (CSV, JSON). |
| **Mood Tracking Notifications** | Send periodic notifications to users to check their mood and recommend mindfulness exercises or coping strategies. |

---

## Contributing

We welcome contributions from the community! If you have suggestions for improvements or would like to report a bug, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Open a pull request detailing your changes.


---

## Acknowledgments

- **OpenAI**: For providing access to the GPT model that powers the conversational capabilities.
- **FER**: For its robust emotion detection framework.
- **Streamlit**: For facilitating the development of an interactive web interface.
- **Community Contributors**: For their valuable feedback and contributions to the project.

---

For any inquiries or support, please contact the project maintainers via GitHub.
