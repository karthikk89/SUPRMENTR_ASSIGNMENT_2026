# Password Authentication System

import re

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&+=]", password):
        return False
    return True


# Set password
stored_password = "Strong@123"

# Login attempts
for attempt in range(3):
    entered_password = input("Enter your password: ")

    if entered_password == stored_password:
        print("Access Granted!")
        break
    else:
        print("Wrong password")

else:
    print("Too many attempts. Account locked.")