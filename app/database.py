import mysql.connector

def get_conversation_history(user_id):
    """ Fetch conversation history from the database for a specific user. """
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="200515",
            database="chatbot_db"
        )

        cursor = db_connection.cursor()

        cursor.execute("SELECT user_message, bot_response, timestamp FROM conversation_history WHERE user_id = %s", (user_id,))
        conversation = cursor.fetchall()

        for message in conversation:
            print(f"User: {message[0]}")
            print(f"Bot: {message[1]}")
            print(f"Timestamp: {message[2]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
