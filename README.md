# Social Network Project

## Authors
- Trenonn Shumway
- Ash Wagner

## Overview
This project implements a simple social network database with tables for users, accounts, posts, followers, likes/dislikes, and saved posts. The Python modules provide a CLI interface to interact with the database.

## Setup

1. **Prerequisites**
   - Python 3.x
   - SQLite3

2. **Initialize the database**  
   ```bash
   chmod +x init.sh
   ./init.sh
   ```
   This will create a new database with sample data.

## Usage Guide

### Command Structure
```bash
python3 turbo.py --action <action> --record <record_type> [additional arguments]
```

### Actions
- `view`: Display records
- `add`: Create new records
- `edit`: Modify existing records
- `delete`: Remove records

### Record Types and Their Arguments

#### Users
- View all users:
  ```bash
  python3 turbo.py --action view --record user
  ```
- View specific user:
  ```bash
  python3 turbo.py --action view --record user --email user@example.com
  ```
- Add user:
  ```bash
  python3 turbo.py --action add --record user --email user@example.com --birthday 1990-01-01
  ```
- Edit user:
  ```bash
  python3 turbo.py --action edit --record user --email user@example.com --birthday 1992-02-02
  ```
- Delete user:
  ```bash
  python3 turbo.py --action delete --record user --email user@example.com
  ```

#### Accounts
- View all accounts:
  ```bash
  python3 turbo.py --action view --record account
  ```
- View specific account:
  ```bash
  python3 turbo.py --action view --record account --username user1
  ```
- Add account:
  ```bash
  python3 turbo.py --action add --record account --username user1 --email user@example.com --acct_type user
  ```
- Edit account type:
  ```bash
  python3 turbo.py --action edit --record account --username user1 --acct_type admin
  ```
- Delete account:
  ```bash
  python3 turbo.py --action delete --record account --username user1
  ```

#### Posts
- View all posts:
  ```bash
  python3 turbo.py --action view --record post
  ```
- View specific post:
  ```bash
  python3 turbo.py --action view --record post --id 1
  ```
- Add post:
  ```bash
  python3 turbo.py --action add --record post --username user1 --message "Hello World!"
  ```
- Delete post:
  ```bash
  python3 turbo.py --action delete --record post --id 1
  ```

#### Follow Relationships
- View followers of an account:
  ```bash
  python3 turbo.py --action view --record followers --username user1
  ```
- View accounts being followed:
  ```bash
  python3 turbo.py --action view --record following --username user1
  ```
- Follow account:
  ```bash
  python3 turbo.py --action add --record follow --follower user1 --followee user2
  ```
- Unfollow account:
  ```bash
  python3 turbo.py --action delete --record follow --follower user1 --followee user2
  ```

#### Post Reactions
- Add like/dislike:
  ```bash
  python3 turbo.py --action add --record like --id 1 --username user2 --liked 1
  ```
- Remove reaction:
  ```bash
  python3 turbo.py --action delete --record like --id 1 --username user2
  ```
- View biggest hater:
  ```bash
  python3 turbo.py --action view --record biggest_hater
  ```
  Shows the user with most dislikes, including:
  - Total number of dislikes
  - Total number of reactions
  - Percentage of reactions that are dislikes

#### Saved Posts
- View saved posts:
  ```bash
  python3 turbo.py --action view --record saved --username user1
  ```

#### Feed
- View feed (posts from followed accounts):
  ```bash
  python3 turbo.py --action view --record feed --username user1
  ```

#### Matchmaker
- Find most compatible pair:
  ```bash
  python3 turbo.py --action view --record matchmaker
  ```
  Shows the pair of users with the most shared interests, including:
  - Number of posts they both liked
  - Number of posts they both saved
  - Total shared interests

### Notes
- All operations are atomic - they either complete fully or roll back entirely
- The `--verbose` flag can be added to any command for additional output
- Post editing is not supported via the CLI
- Viewing posts always includes their current like/dislike counts

## Error Handling
If any operation fails, the transaction is rolled back and an error message is displayed. Common errors include:
- Missing required arguments
- Invalid record IDs
- Non-existent usernames or email addresses
- Duplicate entries where uniqueness is required
