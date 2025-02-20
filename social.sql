-- Drop tables if they exist (allows for clean restarts)
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS likes_dislikes;
DROP TABLE IF EXISTS followers;
DROP TABLE IF EXISTS saved;

CREATE TABLE users (
    email VARCHAR(255) NOT NULL UNIQUE PRIMARY KEY,
    birthday DATE NOT NULL
);

CREATE TABLE accounts (
    username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
    email VARCHAR(255) NOT NULL ,
    acct_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (email) REFERENCES users(email)
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES accounts(username) ON DELETE CASCADE
);

CREATE TABLE likes_dislikes (
    post_id INTEGER NOT NULL,
    username VARCHAR(50) NOT NULL,
    liked BOOLEAN,
    PRIMARY KEY (post_id, username),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (username) REFERENCES accounts(username) ON DELETE CASCADE
);

CREATE TABLE followers (
    follower VARCHAR(50) NOT NULL,
    followee VARCHAR(50) NOT NULL,
    PRIMARY KEY (follower, followee),
    FOREIGN KEY (follower) REFERENCES accounts(username) ON DELETE CASCADE,
    FOREIGN KEY (followee) REFERENCES accounts(username) ON DELETE CASCADE
);

CREATE TABLE saved (
    post_id INTEGER NOT NULL,
    username VARCHAR(50) NOT NULL,
    PRIMARY KEY (post_id, username),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (username) REFERENCES accounts(username) ON DELETE CASCADE
);