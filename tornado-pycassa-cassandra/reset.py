#! /usr/bin/python
"""
Script to reset DB from shell.
"""
import os

import db

def main():
    server = os.getenv("CASSANDRA_POOL")
    db.reset_db('%s:%s'%(server, "9160"))

if __name__ == '__main__':
    main()
