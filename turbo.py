# this will be the actual file that gets run to do view and edit the database.

import sqlite3
from queries import *
import argparse

def view_user(db, args):
    if args.email:
        user = get_user(db, args.email)
        if user:
            print(dict(user))
        else:
            print("User not found")
    else:
        users = get_users(db)
        for user in users:
            print(dict(user))

def view_account(db, args):
    if args.username:
        account = get_account(db, args.username)
        if account:
            print(dict(account))
        else:
            print("Account not found")
    else:
        accounts = get_accounts(db)
        for account in accounts:
            print(dict(account))

def view_post(db, args):
    if args.id:
        post = get_post(db, args.id)
        if post:
            post_dict = dict(post)
            reactions = get_post_reactions(db, post["id"])
            post_dict["likes"] = reactions["likes"]
            post_dict["dislikes"] = reactions["dislikes"]
            print(post_dict)
        else:
            print("Post not found")
    else:
        posts = get_posts(db)
        for post in posts:
            post_dict = dict(post)
            reactions = get_post_reactions(db, post["id"])
            post_dict["likes"] = reactions["likes"]
            post_dict["dislikes"] = reactions["dislikes"]
            print(post_dict)

def view_feed(db, args):
    if args.username:
        feed_posts = get_feed(db, args.username)
        if feed_posts:
            for post in feed_posts:
                post_dict = dict(post)
                reactions = get_post_reactions(db, post["id"])
                post_dict["likes"] = reactions["likes"]
                post_dict["dislikes"] = reactions["dislikes"]
                print(post_dict)
        else:
            print("No posts in feed")
    else:
        print("Username is required to view feed")

def edit_user(db, args):
    if args.email and args.birthday:
        update_user_birthday(db, args.email, args.birthday)
        print(f"User with email {args.email} updated")
    else:
        print("Email and new birthday are required to edit a user")

def edit_account(db, args):
    if args.username and args.acct_type:
        update_account_type(db, args.username, args.acct_type)
        print(f"Account with username {args.username} updated")
    else:
        print("Username and new acct_type are required to edit an account")

def delete_user(db, args):
    if args.email:
        remove_user(db, args.email)
        print(f"User with email {args.email} deleted")
    else:
        print("Email is required to delete a user")

def delete_account(db, args):
    if args.username:
        remove_account(db, args.username)
        print(f"Account with username {args.username} deleted")
    else:
        print("Username is required to delete an account")

def add_user_ui(db, args):
    if args.email and args.birthday:
        add_user(db, args.email, args.birthday)
        print(f"User created with email {args.email}")
    else:
        print("Email and birthday are required to add a user")

def add_account_ui(db, args):
    if args.username and args.email and args.acct_type:
        add_account(db, args.username, args.email, args.acct_type)
        print(f"Account created with username {args.username} for email {args.email}")
    else:
        print("Username, email, and acct_type are required to add an account")

def add_post_ui(db, args):
    if args.username and args.message:
        add_post(db, args.username, args.message)
        print(f"Post added for user {args.username}")
    else:
        print("Username and message are required to add a post")

def add_follow_ui(db, args):
    if args.follower and args.followee:
        add_follow(db, args.follower, args.followee)
        print(f"{args.follower} now follows {args.followee}")
    else:
        print("Follower and followee are required to add a follow relationship")

def add_like_ui(db, args):
    if args.id is not None and args.username and args.liked is not None:
        liked_bool = True if args.liked == 1 else False
        add_like_dislike(db, args.id, args.username, liked_bool)
        print(f"Like/dislike added by {args.username} for post {args.id} with liked={liked_bool}")
    else:
        print("Post ID, username, and liked (1 or 0) are required to add a like/dislike")

def view_followers(db, args):
    if args.username:
        followers = get_followers(db, args.username)
        if followers:
            print(f"Followers of {args.username}:")
            for row in followers:
                print(row["follower"])
        else:
            print(f"No followers found for {args.username}")
    else:
        print("Username is required to view followers")

def view_following(db, args):
    if args.username:
        following = get_following(db, args.username)
        if following:
            print(f"{args.username} is following:")
            for row in following:
                print(row["followee"])
        else:
            print(f"{args.username} is not following anyone")
    else:
        print("Username is required to view following accounts")

def view_saved(db, args):
    if args.username:
        saved_posts = get_saved_posts(db, args.username)
        if saved_posts:
            for post in saved_posts:
                post_dict = dict(post)
                reactions = get_post_reactions(db, post["id"])
                post_dict["likes"] = reactions["likes"]
                post_dict["dislikes"] = reactions["dislikes"]
                print(post_dict)
        else:
            print(f"No saved posts for {args.username}")
    else:
        print("Username is required to view saved posts")

def view_biggest_hater(db, args):
    hater = get_biggest_hater(db)
    if hater:
        print(f"Biggest Hater: {hater['username']}")
        print(f"Total Dislikes: {hater['dislike_count']}")
        print(f"Total Reactions: {hater['total_reactions']}")
        print(f"Dislike Percentage: {hater['dislike_percentage']}%")
    else:
        print("No dislikes found in the system")

def view_matchmaker(db, args):
    match = get_best_match(db)
    if match:
        print("\nBest Match Found!")
        print(f"Users: {match['user1']} and {match['user2']}")
        print(f"Shared Likes: {match['shared_likes']}")
        print(f"Shared Saved Posts: {match['shared_saves']}")
        print(f"Total Shared Interests: {match['total_shared']}")
    else:
        print("No matching pairs found with shared interests")

def parse_args():
    """
    Parse command line arguments for the database tool.
    
    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    

    parser = argparse.ArgumentParser(
        description="Database management tool for viewing and editing the database."
    )
    
    # Example arguments - customize these as needed for your specific requirements.
    parser.add_argument(
        '--action',
        type=str,
        choices=['view', 'edit', 'delete', 'add'],
        required=True,
        help="The action to perform on the database."
    )
    parser.add_argument(
        '--record',
        type=str,
        choices=['user', 'account', 'post', 'like', 'follow', 'feed', 
                'followers', 'following', 'saved', 'biggest_hater', 'matchmaker'],
        required=True,
        help="The type of record to inspect or modify."
    )
    parser.add_argument(
        '--id',
        type=int,
        help="The ID of the record to inspect or modify."
    )
    parser.add_argument('--email', type=str, help="Email address (for users/accounts)")
    parser.add_argument('--birthday', type=str, help="Birthday for user (YYYY-MM-DD)")
    parser.add_argument('--username', type=str, help="Username (for accounts, posts, feeds)")
    parser.add_argument('--acct_type', type=str, help="Account type (for accounts)")
    parser.add_argument('--message', type=str, help="Message text (for posts)")
    parser.add_argument('--follower', type=str, help="Follower's username (for follow relationships)")
    parser.add_argument('--followee', type=str, help="Followee's username (for follow relationships)")
    parser.add_argument('--liked', type=int, choices=[0, 1], help="1 for like, 0 for dislike (for likes)")
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")
    args = parser.parse_args()
    return args

def main():
    """
    Main function to dispatch and execute commands based on the parsed arguments.
    """
    args = parse_args()  # Retrieve parsed command line arguments
    
    # Connect to the database and set row factory for nicer dict outputs
    db = sqlite3.connect("social.db")
    db.row_factory = sqlite3.Row

    # If verbosity is enabled, print the arguments for debugging purposes
    if args.verbose:
        print("Parsed arguments:", args)
    
    # Dispatch based on the action and record type provided
    if args.action == 'view':
        if args.record == 'user':
            view_user(db, args)
        elif args.record == 'account':
            view_account(db, args)
        elif args.record == 'post':
            view_post(db, args)
        elif args.record == 'feed':
            view_feed(db, args)
        elif args.record == 'followers':
            view_followers(db, args)
        elif args.record == 'following':
            view_following(db, args)
        elif args.record == 'saved':
            view_saved(db, args)
        elif args.record == 'biggest_hater':
            view_biggest_hater(db, args)
        elif args.record == 'matchmaker':
            view_matchmaker(db, args)
        else:
            print(f"Viewing for record type '{args.record}' is not supported yet.")
    
    elif args.action == 'add':
        if args.record == 'user':
            add_user_ui(db, args)
        elif args.record == 'account':
            add_account_ui(db, args)
        elif args.record == 'post':
            add_post_ui(db, args)
        elif args.record == 'follow':
            add_follow_ui(db, args)
        elif args.record == 'like':
            add_like_ui(db, args)
        else:
            print(f"Addition for record type '{args.record}' is not supported yet.")
    
    elif args.action == 'edit':
        if args.record == 'user':
            edit_user(db, args)
        elif args.record == 'account':
            edit_account(db, args)
        else:
            print(f"Editing for record type '{args.record}' is not supported yet.")
    
    elif args.action == 'delete':
        if args.record == 'user':
            delete_user(db, args)
        elif args.record == 'account':
            delete_account(db, args)
        elif args.record == 'post':
            if args.id:
                remove_post(db, args.id)
                print(f"Post with id {args.id} deleted")
            else:
                print("Post id is required to delete a post")
        elif args.record == 'follow':
            if args.follower and args.followee:
                remove_follow(db, args.follower, args.followee)
                print(f"{args.follower} unfollowed {args.followee}")
            else:
                print("Follower and followee are required to delete a follow relationship")
        elif args.record == 'like':
            if args.id and args.username:
                remove_like_dislike(db, args.id, args.username)
                print(f"Like/dislike for post {args.id} by {args.username} removed (set to NULL)")
            else:
                print("Post id and username are required to delete a like/dislike")
        else:
            print(f"Deletion for record type '{args.record}' is not supported yet.")
    
    else:
        print(f"Action '{args.action}' is not implemented.")

    try:
        db.commit()  # commit changes if all is ok
    except Exception as e:
        db.rollback()
        print("An error occurred:", e)
    finally:
        db.close()

if __name__ == "__main__":
    main()