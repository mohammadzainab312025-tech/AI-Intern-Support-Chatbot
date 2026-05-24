import sqlite3

def init_db():

    conn = sqlite3.connect('support_tickets.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_ticket(user_message, bot_response):

    conn = sqlite3.connect('support_tickets.db')

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tickets (user_message, bot_response)
        VALUES (?, ?)
    ''', (user_message, bot_response))

    conn.commit()
    conn.close()