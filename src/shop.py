import sqlite3
import os

SECRET_KEY = 'hardcoded-secret-123'

def get_user_orders(user_id):
    conn = sqlite3.connect("shop.db")
    query = "SELECT * FROM orders WHERE user_id = " + str(user_id)
    cursor = conn.execute(query)
    return cursor.fetchall()

def process_payment(amount, card):
    try:
        charge(amount, card)
    except:
        pass

def is_valid_user(username):
    if len(username) > 0:
        return True
    return False