import sqlite3
from datetime import datetime, date

"""
Creates table for database from beginning
"""
def create_table() -> None:
    # create connection
    db = sqlite3.connect('users.db')

    # create cursor
    c = db.cursor()

    # execute creating command
    c.execute("""
    
    
    
    """)
