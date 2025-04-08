import random
from time import sleep

def play_comparison_game():
    """Main function to run the number comparison game"""
    # Setup
    TOTAL_ATTEMPTS = 5
    player_points = 0
    
    # Welcome message
    display_welcome()
    
    # Game rounds
    for current_round in range(1, TOTAL_ATTEMPTS + 1):
        print(f"\n--- Round {current_round} of {TOTAL_ATTEMPTS} ---")
        
        # Generate numbers
        player_value = random.randint(1, 100)
        system_value = random.randint(1, 100)
        
        print(f"You received the number: {player_value}")
        
        # Get prediction
        prediction = get_valid_prediction()
        
        # Check result
        result_correct = check_prediction(prediction, player_value, system_value)
        
        # Display outcome
        display_round_result(result_correct, system_value)
        
        # Update score
        if result_correct:
            player_points += 1
        
        print(f"Current score: {player_points}/{current_round}")
        sleep(0.5)  # Brief pause between rounds
    
    # Final results
    display_final_results(player_points, TOTAL_ATTEMPTS)

def display_welcome():
    """Shows the game introduction"""
    print("*" * 40)
    print("* HIGHER OR LOWER NUMBER PREDICTION GAME *")
    print("*" * 40)
    print("Try to predict if your number is higher or lower than the computer's!")

def get_valid_prediction():
    """Gets and validates the player's prediction"""
    while True:
        user_input = input("Will your number be higher or lower than the computer's? (h/l): ").lower()
        if user_input in ['h', 'higher']:
            return "higher"
        elif user_input in ['l', 'lower']:
            return "lower"
        else:
            print("Please enter 'h' or 'l' only.")

def check_prediction(prediction, player_num, computer_num):
    """Checks if the player's prediction was correct"""
    if prediction == "higher":
        return player_num > computer_num
    else:  # prediction is "lower"
        return player_num < computer_num

def display_round_result(is_correct, computer_number):
    """Shows the result of the current round"""
    print(f"Computer's number was: {computer_number}")
    if is_correct:
        print("✓ Correct prediction! You earn a point.")
    else:
        print("✗ Incorrect prediction. No points earned.")

def display_final_results(score, max_score):
    """Shows the end-game message based on performance"""
    print("\n" + "=" * 30)
    print(f"FINAL SCORE: {score}/{max_score}")
    
    # Performance feedback
    if score == max_score:
        print("PERFECT SCORE! Incredible predictions!")
    elif score >= max_score * 0.6:
        print("Great job! You've got good intuition!")
    elif score >= max_score * 0.4:
        print("Not bad! You've got potential.")
    else:
        print("Keep practicing, prediction is a skill you can develop!")
    
    print("Thanks for playing!")

# Execute game when script is run
if __name__ == "__main__":
    play_comparison_game()