def get_valid_height():
    """Prompt user for height input with validation"""
    while True:
        height = input("Enter your height in centimeters (or press Enter to quit): ").strip()
        
        if not height:  # If empty input
            print("Exiting the program. Have a great day!")
            return None
        
        if not height.isdigit():
            print("Please enter a valid number!")
            continue
            
        return int(height)

def check_ride_eligibility(height_cm):
    """Determine and display ride eligibility with fun messages"""
    MIN_HEIGHT = 50
    MAX_REASONABLE_HEIGHT = 250  # For input validation
    
    if not height_cm:
        return  # Exit case
        
    if height_cm > MAX_REASONABLE_HEIGHT:
        print("Wow! You're taller than the tallest person ever recorded!")
    elif height_cm >= MIN_HEIGHT:
        print("✅ You're tall enough to ride! Enjoy!")
    else:
        print(f"🚧 You need {MIN_HEIGHT - height_cm}cm more to ride. Keep growing!")
    print()  # Empty line for spacing

def main():
    print("Welcome to the Ride Height Checker!\n")
    
    while True:
        height = get_valid_height()
        check_ride_eligibility(height)
        
        if height is None:  # User chose to exit
            break

if __name__ == '__main__':
    main()