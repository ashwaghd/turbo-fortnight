# build.py

import sqlite3
from queries import *

def init_db(db):
    with open('social.sql', 'r') as sql_file:
        sql_script = sql_file.read()
        db.executescript(sql_script)

def main():
    db = sqlite3.connect("social.db")
    with db:
        init_db(db)  # Initialize database tables first
        make_users(db)
        # make_accounts(db)

def make_users(db):
    # Generate 100 test users with unique emails
    for i in range(1, 101):
        email = f"testuser{i}@example.com"
        # Using different birth dates for variety
        birth_date = f"19{90 + (i % 10):02d}-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}"
        add_user(db, email, birth_date)

def make_accounts(db):
    add_account(db, "testuser", "testuser@example.com", "user")

if __name__ == "__main__":
    main()
