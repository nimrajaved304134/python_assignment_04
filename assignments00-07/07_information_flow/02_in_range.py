def check_boundaries(value, minimum, maximum):
    """
    Determines if a value falls within specified boundaries (inclusive).
    Returns: Boolean indicating if value is within range
    """
    return minimum <= value <= maximum

def run_program():
    try:
        # Collect user inputs
        user_value = int(input("Please provide a value: "))
        lower_boundary = int(input("Please specify minimum boundary: "))
        upper_boundary = int(input("Please specify maximum boundary: "))
        
        # Check if value is within boundaries and display outcome
        is_within_range = check_boundaries(user_value, lower_boundary, upper_boundary)
        print("Within specified range:", is_within_range)
    except ValueError:
        print("Error: Please enter only numbers")

# Program entry point
if __name__ == "__main__":
    run_program()