-- Drop tables if they exist (allows for clean restarts)
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS likes_dislikes;
DROP TABLE IF EXISTS followers;
DROP TABLE IF EXISTS saved;

-- Create users table first since accounts will reference it
CREATE TABLE users (
    email VARCHAR(255) NOT NULL UNIQUE PRIMARY KEY,
    birthday DATE NOT NULL
);

-- Create accounts table first since posts will reference it
CREATE TABLE accounts (
    username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE ,
    acct_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (email) REFERENCES users(email)
);

-- Create posts table with foreign key reference to accounts
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
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