# Social Network Project

## Authors
- Alice
- Bob

## Overview
This project implements a simple social network and its database schema. The database includes tables for users, accounts, posts, followers, likes/dislikes, and saved posts. The Python modules provide functions to add, view, edit, and delete records. In addition, you can follow/unfollow accounts and view a feed of posts from followed accounts.

## Setup

1. **Ensure you have Python and SQLite installed.**

2. **Initialize the database**  
   Run the shell script to remove any existing database, create the new schema, and populate initial data:
   ```bash
   chmod +x init.sh
   ./init.sh
   ```

## Usage

The main user interface is provided by `turbo.py`. Use the command-line arguments to perform operations.

### Example Commands

- **Add a User**
  ```bash
  python3 turbo.py --action add --record user --email user@example.com --birthday 1990-01-01
  ```

- **View All Users**
  ```bash
  python3 turbo.py --action view --record user
  ```

- **Edit a User (update birthday)**
  ```bash
  python3 turbo.py --action edit --record user --email user@example.com --birthday 1992-02-02
  ```

- **Delete a User**
  ```bash
  python3 turbo.py --action delete --record user --email user@example.com
  ```

- **Add an Account**
  ```bash
  python3 turbo.py --action add --record account --username user1 --email user@example.com --acct_type user
  ```

- **View All Accounts**
  ```bash
  python3 turbo.py --action view --record account
  ```

- **Edit an Account (update acct_type)**
  ```bash
  python3 turbo.py --action edit --record account --username user1 --acct_type admin
  ```

- **Delete an Account**
  ```bash
  python3 turbo.py --action delete --record account --username user1
  ```

- **Add a Post**
  ```bash
  python3 turbo.py --action add --record post --username user1 --message "Hello World!"
  ```

- **View All Posts**
  ```bash
  python3 turbo.py --action view --record post
  ```

- **Edit a Post**
  ```bash
  python3 turbo.py --action edit --record post --id 1 --message "Updated post"
  ```

- **Delete a Post**
  ```bash
  python3 turbo.py --action delete --record post --id 1
  ```

- **Follow an Account**
  ```bash
  python3 turbo.py --action add --record follow --follower user1 --followee user2
  ```

- **Unfollow an Account**
  ```bash
  python3 turbo.py --action delete --record follow --follower user1 --followee user2
  ```
- **Saved Posts:**
  To view all saved posts for a specific account, run:
  ```bash
  python3 turbo.py --action view --record saved --username user1
  ```

- **View Feed (posts from followed accounts)**
  ```bash
  python3 turbo.py --action view --record feed --username user1
  ```

## Notes
- Additional features (like detailed like/dislike views and custom "interesting queries") can be added later.
- Every operation is performed as a single call, so all required parameters must be supplied via command-line arguments.
- If any error occurs, the transaction is rolled back and an error message is printed.

Happy coding!

## Walkthrough

This section provides a complete walkthrough for interacting with each table in the social network database using the CLI tool (`turbo.py`).

### Viewing Data

**Users Table**
- View all users:
  ```bash
  python3 turbo.py --action view --record user
  ```
- View a specific user by email:
  ```bash
  python3 turbo.py --action view --record user --email testuser1@example.com
  ```

**Accounts Table**
- View all accounts:
  ```bash
  python3 turbo.py --action view --record account
  ```
- View a specific account by username:
  ```bash
  python3 turbo.py --action view --record account --username user1
  ```

**Posts Table**
- View all posts (each post displays like/dislike counts):
  ```bash
  python3 turbo.py --action view --record post
  ```
- View a specific post by its ID:
  ```bash
  python3 turbo.py --action view --record post --id 1
  ```

**Feed Data**
- View the feed (posts from followed accounts) for a specific user:
  ```bash
  python3 turbo.py --action view --record feed --username user1
  ```

*Note:* Other tables such as `followers`, `likes_dislikes`, and `saved` are managed implicitly:
  - Follow relationships and post reactions (likes/dislikes) are visible through feed and post views.

### Followers and Following Data

**Followers Data**
- View all followers of a specific account:
  To view all followers of an account, run:
  ```bash
  python3 turbo.py --action view --record followers --username user1
  ```

**Following Data**
- View all accounts a specific account is following:
  To view the accounts that a user is following, run:
  ```bash
  python3 turbo.py --action view --record following --username user1
  ```

### Inserting Data

**Insert User**
```bash
python3 turbo.py --action add --record user --email newuser@example.com --birthday 1995-05-05
```

**Insert Account**
```bash
python3 turbo.py --action add --record account --username newacct --email newuser@example.com --acct_type user
```

**Insert Post**
```bash
python3 turbo.py --action add --record post --username newacct --message "Hello, this is my first post!"
```

**Follow an Account**
```bash
python3 turbo.py --action add --record follow --follower user1 --followee user2
```

**Like/Dislike a Post**
To add a like or dislike to a post (where `liked` is 1 for like and 0 for dislike):
```bash
python3 turbo.py --action add --record like --id 1 --username user2 --liked 1
```
*Note:* The reaction details will be visible when viewing the post.

### Editing Data

**Edit User Birthday**
```bash
python3 turbo.py --action edit --record user --email newuser@example.com --birthday 1996-06-06
```

**Edit Account Type**
```bash
python3 turbo.py --action edit --record account --username newacct --acct_type admin
```

*Note:* Editing posts is not directly supported via this CLI.

### Deleting Data

**Delete User**
```bash
python3 turbo.py --action delete --record user --email newuser@example.com
```

**Delete Account**
```bash
python3 turbo.py --action delete --record account --username newacct
```

**Delete Post**
```bash
python3 turbo.py --action delete --record post --id 1
```

**Unfollow an Account**
```bash
python3 turbo.py --action delete --record follow --follower user1 --followee user2
```

**Remove a Like/Dislike**
```bash
python3 turbo.py --action delete --record like --id 1 --username user2
```
