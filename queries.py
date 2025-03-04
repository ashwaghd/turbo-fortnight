# queries.py
def add_user(db, email, birthday):
    db.execute("INSERT INTO users (email, birthday) VALUES (?, ?)", (email, birthday))

def remove_user(db, email):
    db.execute("DELETE FROM users WHERE email = ?", (email,))

def add_account(db, username, email, acct_type):
    db.execute("INSERT INTO accounts (username, email, acct_type) VALUES (?, ?, ?)", (username, email, acct_type))

def remove_account(db, username):
    db.execute("DELETE FROM accounts WHERE username = ?", (username,))

def add_post(db, username, message):
    db.execute("INSERT INTO posts (username, message) VALUES (?, ?)", (username, message))

def update_post(db, post_id, message):
    db.execute("UPDATE posts SET message = ? WHERE id = ?", (message, post_id))

def remove_post(db, post_id):
    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))

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
    db.execute("INSERT INTO saved (post_id, username) VALUES (?, ?)", (post_id, username))

def remove_saved_post(db, post_id, username):
    db.execute("DELETE FROM saved WHERE post_id = ? AND username = ?", (post_id, username))

def get_users(db):
    cursor = db.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_user(db, email):
    cursor = db.execute("SELECT * FROM users WHERE email = ?", (email,))
    return cursor.fetchone()

def update_user_birthday(db, email, birthday):
    db.execute("UPDATE users SET birthday = ? WHERE email = ?", (birthday, email))

def get_accounts(db):
    cursor = db.execute("SELECT * FROM accounts")
    return cursor.fetchall()

def get_account(db, username):
    cursor = db.execute("SELECT * FROM accounts WHERE username = ?", (username,))
    return cursor.fetchone()

def update_account_type(db, username, acct_type):
    db.execute("UPDATE accounts SET acct_type = ? WHERE username = ?", (acct_type, username))

def get_posts(db):
    cursor = db.execute("SELECT * FROM posts ORDER BY created_at DESC")
    return cursor.fetchall()

def get_post(db, post_id):
    cursor = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    return cursor.fetchone()

def get_feed(db, username):
    cursor = db.execute(
        "SELECT posts.* FROM posts INNER JOIN followers ON posts.username = followers.followee WHERE followers.follower = ? ORDER BY posts.created_at DESC",
        (username,)
    )
    return cursor.fetchall()

# New function to retrieve the like/dislike counts for a given post
def get_post_reactions(db, post_id):
    cursor = db.execute(
        "SELECT COALESCE(SUM(CASE WHEN liked = 1 THEN 1 ELSE 0 END), 0) as likes, "
        "COALESCE(SUM(CASE WHEN liked = 0 THEN 1 ELSE 0 END), 0) as dislikes "
        "FROM likes_dislikes WHERE post_id = ?",
        (post_id,)
    )
    result = cursor.fetchone()
    return result

# New function to get an account's followers (accounts that follow the provided username)
def get_followers(db, username):
    cursor = db.execute("SELECT follower FROM followers WHERE followee = ?", (username,))
    return cursor.fetchall()

# New function to get the accounts a given account is following
def get_following(db, username):
    cursor = db.execute("SELECT followee FROM followers WHERE follower = ?", (username,))
    return cursor.fetchall()

# New function to get the saved posts for a given account
def get_saved_posts(db, username):
    cursor = db.execute(
        "SELECT posts.* FROM posts INNER JOIN saved ON posts.id = saved.post_id WHERE saved.username = ? ORDER BY posts.created_at DESC",
        (username,)
    )
    return cursor.fetchall()

def get_biggest_hater(db):
    cursor = db.execute("""
        SELECT 
            username,
            COUNT(*) as dislike_count
        FROM likes_dislikes 
        WHERE liked = 0
        GROUP BY username
        ORDER BY dislike_count DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    if result:
        # Add total posts count for context
        cursor = db.execute("""
            SELECT COUNT(*) as total_reactions
            FROM likes_dislikes
            WHERE username = ?
        """, (result['username'],))
        total = cursor.fetchone()
        return {
            'username': result['username'],
            'dislike_count': result['dislike_count'],
            'total_reactions': total['total_reactions'],
            'dislike_percentage': round((result['dislike_count'] / total['total_reactions']) * 100, 2)
        }
    return None

def get_best_match(db):
    cursor = db.execute("""
        WITH shared_interests AS (
            -- Count shared likes
            SELECT 
                a.username as user1,
                b.username as user2,
                COUNT(*) as shared_count
            FROM likes_dislikes a
            JOIN likes_dislikes b ON a.post_id = b.post_id
            WHERE a.username < b.username  -- Avoid self-pairs and duplicates
                AND a.liked = 1 AND b.liked = 1
            GROUP BY a.username, b.username
            
            UNION ALL
            
            -- Count shared saves
            SELECT 
                a.username as user1,
                b.username as user2,
                COUNT(*) as shared_count
            FROM saved a
            JOIN saved b ON a.post_id = b.post_id
            WHERE a.username < b.username  -- Avoid self-pairs and duplicates
            GROUP BY a.username, b.username
        )
        SELECT 
            user1,
            user2,
            SUM(shared_count) as total_shared,
            COUNT(*) as interaction_types
        FROM shared_interests
        GROUP BY user1, user2
        ORDER BY total_shared DESC, interaction_types DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    
    if result:
        # Get additional details about their shared content
        cursor = db.execute("""
            SELECT COUNT(*) as shared_likes
            FROM likes_dislikes a
            JOIN likes_dislikes b ON a.post_id = b.post_id
            WHERE a.username = ? AND b.username = ?
                AND a.liked = 1 AND b.liked = 1
        """, (result['user1'], result['user2']))
        shared_likes = cursor.fetchone()['shared_likes']
        
        cursor = db.execute("""
            SELECT COUNT(*) as shared_saves
            FROM saved a
            JOIN saved b ON a.post_id = b.post_id
            WHERE a.username = ? AND b.username = ?
        """, (result['user1'], result['user2']))
        shared_saves = cursor.fetchone()['shared_saves']
        
        return {
            'user1': result['user1'],
            'user2': result['user2'],
            'shared_likes': shared_likes,
            'shared_saves': shared_saves,
            'total_shared': result['total_shared']
        }
    return None