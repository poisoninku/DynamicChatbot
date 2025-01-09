import spacy
import random
import mysql.connector
from datetime import datetime

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Persona definitions
personas = {
    "friendly": "Hey there! How can I help you today?",
    "formal": "Good day. How may I assist you?",
    "funny": "What’s up? Let’s have some fun!",
}

def get_personality_response(personality, user_input):
    """ Switches personalities based on user input. """
    if personality == "friendly":
        return "Hey there! I'm here to help. What’s on your mind?"
    elif personality == "formal":
        return "Good day. How may I assist you?"
    elif personality == "funny":
        return "What’s up? Let’s have some fun!"
    else:
        return "Sorry, I didn’t quite catch that."

def store_message(user_id, message, response):
    """ Store user messages and bot responses in MySQL. """
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="200515",
            database="chatbot_db" 
        )

        cursor = db_connection.cursor()

        # Insert user message and bot response into the database
        timestamp = datetime.now()
        cursor.execute(
            "INSERT INTO conversation_history (user_id, user_message, bot_response, timestamp) VALUES (%s, %s, %s, %s)",
            (user_id, message, response, timestamp)
        )
        db_connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()

def get_response(user_input, personality):
    """ Return bot response based on personality and user input. """
    # Basic NLP processing with spaCy
    doc = nlp(user_input)
    # Logic to adapt the bot's response based on personality
    return get_personality_response(personality, user_input)
