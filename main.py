# WARNING: This file contains intentional vulnerabilities for testing GitHub Copilot
# EDUCATIONAL PURPOSE ONLY - DO NOT USE IN PRODUCTION

import os
import pickle

def greet(name):
    # Original function
    return f"Hello, {name}! Welcome to our sample repository."

def process_user_input(user_data):
    """Testing security detection - contains vulnerabilities"""
    
    # VULNERABILITY 1: Unsafe deserialization (should be flagged)
    data = pickle.loads(user_data)  # Dangerous - can execute arbitrary code
    
    # VULNERABILITY 2: OS command injection
    filename = input("Enter file to read: ")
    os.system(f"cat {filename}")  # Unsafe - allows command injection
    
    # VULNERABILITY 3: Hardcoded secret (should be detected)
    SECRET_KEY = "sk-prod-abc123xyz789"
    
    return data

if __name__ == "__main__":
    print(greet("World"))
    print("This file contains test vulnerabilities - EDUCATIONAL ONLY")
