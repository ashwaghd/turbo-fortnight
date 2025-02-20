# build.py

import sqlite3
from queries import *
import random  # Imported for generating random likes/dislikes and saved posts

def init_db(db):
    with open('social.sql', 'r') as sql_file:
        sql_script = sql_file.read()
        db.executescript(sql_script)

def make_users(db):
    # Generate 100 test users with unique emails
    for i in range(1, 101):
        email = f"testuser{i}@example.com"
        # Using different birth dates for variety
        birth_date = f"19{90 + (i % 10):02d}-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}"
        add_user(db, email, birth_date)

def make_accounts(db):
    # Create 10 accounts corresponding to testuser1 through testuser10
    for i in range(1, 11):
        username = f"user{i}"
        email = f"testuser{i}@example.com"
        acct_type = "user"
        add_account(db, username, email, acct_type)

def make_posts(db):
    # For each account generate 3 posts
    for i in range(1, 11):
        username = f"user{i}"
        for j in range(1, 4):
            message = f"Post {j} from {username}"
            add_post(db, username, message)

def make_follows(db):
    # Make each account follow the next 3 (cyclic)
    accounts = [f"user{i}" for i in range(1, 11)]
    n = len(accounts)
    for i in range(n):
        follower = accounts[i]
        for j in range(1, 4):
            followee = accounts[(i + j) % n]
            add_follow(db, follower, followee)

def make_likes(db):
    # For each post, let each account (except the post owner) have a 30% chance
    # to like or dislike the post. With 70% chance the reaction is a like.
    posts = get_posts(db)
    accounts = [f"user{i}" for i in range(1, 11)]
    for post in posts:
        post_id = post["id"]
        owner = post["username"]
        for account in accounts:
            if account == owner:
                continue
            if random.random() < 0.3:
                liked = True if random.random() < 0.7 else False
                add_like_dislike(db, post_id, account, liked)

def make_saved(db):
    # For each post, let accounts (excluding the post's owner) have a 10% chance to save it.
    posts = get_posts(db)
    accounts = [f"user{i}" for i in range(1, 11)]
    for post in posts:
        for account in accounts:
            if account == post["username"]:
                continue
            if random.random() < 0.1:
                add_saved_post(db, post["id"], account)

def main():
    db = sqlite3.connect("social.db")
    db.row_factory = sqlite3.Row
    with db:
        init_db(db)  # Initialize database tables first
        make_users(db)
        make_accounts(db)
        make_posts(db)
        make_follows(db)
        make_likes(db)
        make_saved(db)

if __name__ == "__main__":
    main()
