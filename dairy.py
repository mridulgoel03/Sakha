import os
import datetime

# Function to log conversations to the diary
def log_conversation(user_input, bot_response):
    """Logs user input and bot response to a diary file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open('diary_log.txt', 'a') as f:
            f.write(f"{timestamp} - User: {user_input}\n")
            f.write(f"{timestamp} - Bot: {bot_response}\n\n")
    except Exception as e:
        print(f"Error logging conversation: {e}")

# Function to read logged conversations from the diary
def read_conversations():
    """Reads and returns all logged conversations from the diary file."""
    if os.path.exists('diary_log.txt'):
        try:
            with open('diary_log.txt', 'r') as f:
                return f.readlines()
        except Exception as e:
            print(f"Error reading diary: {e}")
            return []
    return []

# Example usage for testing the diary functions
if __name__ == "__main__":
    # This part can be used for testing the diary functions
    log_conversation("Hello, how are you?", "I'm just a program, but I'm doing well!")
    print("Logged conversations:")
    for entry in read_conversations():
        print(entry.strip())
