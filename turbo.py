# this will be the actual file that gets run to do view and edit the database.

import sqlite3
from queries import *
import argparse

def view_user():
    pass

def view_account():
    pass

def view_post():
    pass

def view_feed():
    pass    

def edit_user():
    pass

def edit_account():
    pass

def delete_user():
    pass

def delete_account():
    pass


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
        choices=['user', 'account', 'post', 'like', 'follow', 'feed'],
        required=True,
        help="The type of record to inspect or modify."
    )
    parser.add_argument(
        '--id',
        type=int,
        help="The ID of the record to inspect or modify."
    )
    args = parser.parse_args()
    return args

def main():
    """
    Main function to dispatch and execute commands based on the parsed arguments.
    """
    args = parse_args()  # Retrieve parsed command line arguments

    # If verbosity is enabled, print the arguments for debugging purposes
    if args.verbose:
        print("Parsed arguments:", args)
    
    # Dispatch based on the action and record type provided
    if args.action == 'view':
        if args.record == 'user':
            view_user(args.id)
        elif args.record == 'account':
            view_account(args.id)
        elif args.record == 'post':
            view_post(args.id)
        elif args.record == 'feed':
            view_feed(args.id)
        else:
            print(f"Viewing for record type '{args.record}' is not supported yet.")
    
    elif args.action == 'edit':
        if args.record == 'user':
            edit_user(args.id)
        elif args.record == 'account':
            edit_account(args.id)
        # Add additional elif branches for other record types
        else:
            print(f"Editing for record type '{args.record}' is not supported yet.")
    
    elif args.action == 'delete':
        if args.record == 'user':
            delete_user(args.id)
        # Add additional branches for other record types as needed
        else:
            print(f"Deletion for record type '{args.record}' is not supported yet.")
    
    elif args.action == 'add':
        if args.record == 'user':
            add_user()  # Possibly prompt for more details as needed
        # Implement for other record types as required
        else:
            print(f"Addition for record type '{args.record}' is not supported yet.")
    
    else:
        print(f"Action '{args.action}' is not implemented.")

if __name__ == "__main__":
    main()