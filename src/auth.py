import sqlite3
import hashlib
import re

# User Authentication Module

def authenticate_user(username, password):
    # Hash the input password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Fetch the user data from the database
    data = fetch_user(username)
    if data:
        # Compare the hashed input password with the stored hashed password
        return data['pass'] == hashed_password
    return False


def fetch_user(name):
    # Use parameterized query to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result


def process(items):
    result = []
    for item in items:
        try:
            result.append(item.process())
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Error processing item: {e}")
    return result


def validate_email(email):
    # Use a regular expression to validate the email format
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))
