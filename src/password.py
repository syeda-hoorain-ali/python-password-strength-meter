import random
import re

COMMON_PASSWORDS: list[str] = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "welcome",
    "qwerty", "abc123", "password1", "111111", "123123", "admin", "letmein", "password123",
    "beautyqueen", "princess", "admin123", "qwerty123", "1q2w3e4r", "password123", "asdfghjkl"
]

def check_password_strength(password: str) -> tuple[int, list[str]]:
    """
        A function to check password strength
        return a tuple including score and list of errors to improve password
    """
    
    score = 0
    errors: list[str] = []


    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        errors.append("Password should be at least 8 characters long.")


    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        errors.append("Include both uppercase and lowercase letters.")


    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        errors.append("Add at least one number (0-9).")


    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        errors.append("Include at least one special character (!@#$%^&*).")
    

    if password:

        # Common Passwords Check
        if password.lower() not in COMMON_PASSWORDS:
            score += 1
        else:
            errors.append("Avoid common passwords like 'password123'.")


        # Repeating Characters Check
        if not re.search(r'(.)\1\1', password): 
            score += 1
        else:
            errors.append("Avoid repeating characters like 'aaa' or '111'.")

    # Strength Rating
    if score == 6:
        print("✅ Strong Password!")
    elif score == 4:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")


    
    return (score, errors)


def generate_password():
    """A simple function to generate password"""

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special = '!@#$%^&*()'

    #* Later we will ask user to select what to include in thier password
    include = uppercase + lowercase + digits + special
    length = 12

    strength = 0
    password = ''

    while strength != 6:
        password = ''

        for _ in range(length):
            password += random.choice(include)
        
        strength, _ = check_password_strength(password)
    
    return password
