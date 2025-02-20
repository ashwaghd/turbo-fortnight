#!/bin/bash
# Remove existing database
rm -f social.db
# Build the schema using sqlite3 and social.sql
sqlite3 social.db < social.sql
# Populate the database with initial data
python3 build.py 