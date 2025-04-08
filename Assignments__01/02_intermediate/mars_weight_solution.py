def calculate_weight_on_planet(earth_weight, planet):
    """
    Calculate the weight on a specified planet based on Earth weight.
    
    Args:
        earth_weight (float): Weight on Earth
        planet (str): Name of the planet
        
    Returns:
        float: Equivalent weight on the specified planet
    """
    # Dictionary of planetary gravity constants (as percentage of Earth's gravity)
    gravity_factors = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }
    
    # Check if the planet is in our dictionary
    if planet in gravity_factors:
        # Calculate the weight on the specified planet
        planet_weight = earth_weight * (gravity_factors[planet] / 100)
        return planet_weight
    else:
        return None

def main():
    """Main function to run the planetary weight calculator program."""
    # Print welcome message
    print("Welcome to the Planetary Weight Calculator!")
    print("-" * 40)
    
    # Get user input for Earth weight
    try:
        earth_weight = float(input("Enter a weight on Earth: "))
        
        # Get user input for planet name
        planet = input("Enter a planet: ")
        
        # Calculate weight on the specified planet
        planet_weight = calculate_weight_on_planet(earth_weight, planet)
        
        # Display the result
        if planet_weight is not None:
            # Round to 2 decimal places when necessary
            rounded_weight = round(planet_weight, 2)
            print(f"\nThe equivalent weight on {planet}: {rounded_weight}")
        else:
            print(f"\nSorry, {planet} is not recognized as a planet in our solar system.")
    
    except ValueError:
        print("Please enter a valid number for weight.")

# Execute the program when run directly
if __name__ == "__main__":
    main()