# queries.py
def add_user(db, email, birthday):
    db.execute("INSERT INTO users (email, birthday) VALUES (?, ?)", (email, birthday))

def remove_user(db, email):
    db.execute("DELETE FROM users WHERE email = ?", (email,))

def add_account(db, username, email, acct_type):
    db.execute("INSERT INTO accounts (username, email, acct_type) VALUES (?, ?, ?)", (username, email, acct_type))

def remove_account(db, username):
    db.execute("DELETE FROM accounts WHERE username = ?", (username,))

def add_post(db, username, post_text):
    db.execute("INSERT INTO posts (username, post_text) VALUES (?, ?)", (username, post_text))

def update_post(db, post_id, post_text):
    db.execute("UPDATE posts SET post_text = ? WHERE post_id = ?", (post_text, post_id))

def remove_post(db, post_id):
    db.execute("DELETE FROM posts WHERE post_id = ?", (post_id,))

def add_like_dislike(db, post_id, username, liked):
    db.execute("INSERT INTO likes_dislikes (post_id, username, liked) VALUES (?, ?, ?)", (post_id, username, liked))

def update_like_dislike(db, post_id, username, liked):
    db.execute("UPDATE likes_dislikes SET liked = ? WHERE post_id = ? AND username = ?", (liked, post_id, username))

def remove_like_dislike(db, post_id, username):
    db.execute("UPDATE likes_dislikes SET liked = NULL WHERE post_id = ? AND username = ?", (post_id, username))

def add_follow(db, follower, followee):
    db.execute("INSERT INTO followers (follower, followee) VALUES (?, ?)", (follower, followee))

def remove_follow(db, follower, followee):
    db.execute("DELETE FROM followers WHERE follower = ? AND followee = ?", (follower, followee))

def add_saved_post(db, post_id, username):
    db.execute("INSERT INTO saved_posts (post_id, username) VALUES (?, ?)", (post_id, username))

def remove_saved_post(db, post_id, username):
    db.execute("DELETE FROM saved_posts WHERE post_id = ? AND username = ?", (post_id, username))