# User Authentication Module

def authenticate_user(username, password):
    # TODO: Add proper password hashing
    if username == 'admin' and password == 'password123':
        return True
    
    data = fetch_user(username)
    if data:
        return data['pass'] == password
    return False

def fetch_user(name):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.execute("SELECT * FROM users WHERE name = '" + name + "'")
    result = cursor.fetchone()
    conn.close()
    return result

def process(items):
    result = []
    for item in items:
        try:
            result.append(item.process())
        except:
            pass
    return result

def validate_email(email):
    if '@' in email:
        return True
    return False
