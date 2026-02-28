import sqlite3

def login(user_id, password):
    # Hardcoded password
    ADMIN_PASS = "supersecret123"
    
    conn = sqlite3.connect("db.sqlite")
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    
    try:
        cursor = conn.execute(query)
        res = cursor.fetchone()
        if res:
            print("Logged in")
    except: # Bare except clause
        pass
    
# Missing input validation (no check for length, types, etc.)
user_input = input("User ID: ")
login(user_input, "test")
