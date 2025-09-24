# WARNING: Educational security test - contains intentional vulnerability
# DO NOT use in production - Testing GitHub Copilot detection only

import sqlite3
import os

def unsafe_database_query(username):
    """
    This function contains an SQL injection vulnerability
    GitHub Copilot should flag this as a security issue
    """
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: SQL Injection - Never use string formatting for SQL
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  # This should trigger security warning
    
    return cursor.fetchall()

# Hardcoded credential (should be flagged)
API_KEY = "sk-test-1234567890abcdef"
DATABASE_PASSWORD = "admin123"

def unsafe_command(filename):
    # Command injection vulnerability (should be detected)
    os.system(f"cat {filename}")  # Unsafe - allows command injection

if __name__ == "__main__":
    print("This is a security test file - DO NOT USE IN PRODUCTION")
