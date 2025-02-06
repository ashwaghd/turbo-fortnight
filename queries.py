# queries.py
def add_user(db, email, birthday):
    db.execute("INSERT INTO users (email, birthday) VALUES (?, ?)", (email, birthday))

def add_account(db, username, email, acct_type):
    db.execute("INSERT INTO accounts (username, email, acct_type) VALUES (?, ?, ?)", (username, email, acct_type))