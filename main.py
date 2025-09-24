# WARNING: Educational testing file - contains intentional vulnerabilities
# DO NOT USE IN PRODUCTION - Testing GitHub Copilot detection only

import os
import subprocess
import hashlib
import random

def greet(name):
    # Original function
    return f"Hello, {name}! Welcome to our sample repository."

def login_system(username, password):
    """Testing security detection - multiple vulnerabilities"""
    
    # VULNERABILITY 1: Weak hashing algorithm (MD5 is broken)
    password_hash = hashlib.md5(password.encode()).hexdigest()
    
    # VULNERABILITY 2: SQL injection pattern
    query = "SELECT * FROM users WHERE user='%s' AND pass='%s'" % (username, password)
    
    # VULNERABILITY 3: Weak random token generation
    session_token = random.randint(1000, 9999)  # Predictable randomness
    
    # VULNERABILITY 4: Hardcoded database credentials
    DB_HOST = "prod.database.internal"
    DB_PASSWORD = "admin@2024!"
    DB_USER = "root"
    
    # VULNERABILITY 5: Subprocess with shell=True
    user_file = input("Enter config file: ")
    result = subprocess.run(f"grep password {user_file}", shell=True, capture_output=True)
    
    # VULNERABILITY 6: Path traversal vulnerability
    with open(f"./data/{username}.txt", 'r') as f:
        user_data = f.read()  # No path validation
    
    return {"token": session_token, "query": query}

# VULNERABILITY 7: Exposed API keys
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

if __name__ == "__main__":
    print(greet("World"))
    print("WARNING: Test file with vulnerabilities - EDUCATIONAL ONLY")
