AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: \n'{AFFIRMATION}'\n")
    
    attempts = 0
    while True:
        user_input = input("Your response: ").strip()  # Remove extra spaces
        
        if user_input.lower() == AFFIRMATION.lower():  # Case-insensitive check
            break  # Exit loop if correct
        
        attempts += 1
        print("\nThat's not quite right. Let's try again!")
        
        # Give a hint if the user struggles after 2 attempts
        if attempts >= 2:
            print("(Hint: Make sure to type it exactly, but capitalization doesn't matter.)")
        
        print(f"\nPlease type: '{AFFIRMATION}'")
    
    # Custom success message based on attempts
    if attempts == 0:
        print("\nPerfect on the first try! You're amazing! 😊")
    else:
        print(f"\nYou got it in {attempts + 1} tries! Great job! ✨")

if __name__ == '__main__':
    main()