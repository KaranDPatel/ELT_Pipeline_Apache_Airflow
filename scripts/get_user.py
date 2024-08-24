# scripts/get_user.py

import os
import getpass

def get_current_user():
    # Get the current user's username (cross-platform)
    if os.name == 'posix':  # Unix-like system (Linux, macOS)
        import pwd
        user_name = pwd.getpwuid(os.getuid())[0]
    else:  # Windows system
        user_name = os.getenv('USERNAME') or getpass.getuser()

    return user_name
