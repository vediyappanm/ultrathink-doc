import sqlite3
import hashlib
import re

# User Authentication Module

def authenticate_user(username, password):
    # Hash the input password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    data = fetch_user(username)
    if data:
        # Compare the hashed input password with the stored hashed password
        return data['pass'] == hashed_password
    return False

def fetch_user(name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Use parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        # Convert the result to a dictionary for easier access
        return {'name': result[0], 'pass': result[1]}
    return None

def process(items):
    result = []
    for item in items:
        try:
            # Check if the item has a process method
            if hasattr(item, 'process'):
                result.append(item.process())
        except Exception as e:
            # Log the exception instead of ignoring it
            print(f"Error processing item: {e}")
    return result

def validate_email(email):
    # Use a regular expression to validate the email format
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))
