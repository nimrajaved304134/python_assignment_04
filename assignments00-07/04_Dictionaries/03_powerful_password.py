import hashlib
import json
import os

DATA_FILE = "user_logins.json"

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_logins():
    """Load stored logins from file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

def save_logins(logins):
    """Save logins to file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(logins, f, indent=2)

def register_user():
    """Register a new user."""
    print("\nUser Registration")
    print("-----------------")
    
    while True:
        email = input("Enter email (or 'menu' to return): ").strip().lower()
        if email == 'menu':
            return
        if not email:
            print("Email cannot be empty!")
            continue
        if '@' not in email or '.' not in email:
            print("Please enter a valid email address!")
            continue
            
        logins = load_logins()
        if email in logins:
            print("This email is already registered!")
            continue
            
        while True:
            password = input("Enter password (or 'menu' to cancel): ").strip()
            if password == 'menu':
                break
            if not password:
                print("Password cannot be empty!")
                continue
                
            confirm_password = input("Confirm password: ").strip()
            if password != confirm_password:
                print("Passwords don't match!")
                continue
                
            logins[email] = hash_password(password)
            save_logins(logins)
            print("\nRegistration successful! ✅")
            return

def login_user():
    """Login an existing user."""
    print("\nUser Login")
    print("----------")
    
    logins = load_logins()
    if not logins:
        print("No users registered yet!")
        return False
    
    while True:
        email = input("Enter email (or 'menu' to return): ").strip().lower()
        if email == 'menu':
            return False
        
        password = input("Enter password (or 'menu' to return): ").strip()
        if password == 'menu':
            return False
            
        if email in logins and logins[email] == hash_password(password):
            print("\nLogin successful! ✅")
            return True
        else:
            print("\nLogin failed! ❌ Incorrect email or password.")
            print("1. Try again")
            print("2. Return to menu")
            
            choice = input("Enter choice (1-2): ").strip()
            if choice == '2':
                return False
            # If choice is 1 or invalid, the loop continues and asks for credentials again

def main():
    """Main program loop."""
    while True:
        print("\nWelcome to the Login System")
        print("==========================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                # Placeholder for logged-in functionality
                print("\nYou are now logged in!")
                input("Press Enter to return to menu...")
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()