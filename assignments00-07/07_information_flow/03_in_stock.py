def num_in_stock(fruit):
    """
    Returns the number of the specified fruit in Sophia's inventory.
    
    Args:
        fruit (str): The name of the fruit to check
        
    Returns:
        int: The quantity of the fruit in stock
    """
    # This is a simplified inventory - in a real program,
    # this might be stored in a database or file
    inventory = {
        "apple": 500,
        "banana": 300,
        "orange": 200,
        "pear": 1000,
        "grape": 750,
        "strawberry": 150,
        "blueberry": 225
    }
    
    # Return the count if fruit exists, otherwise return 0
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt user for a fruit
    fruit = input("Enter a fruit: ")
    
    # Get the quantity in stock
    quantity = num_in_stock(fruit)
    
    # Check if the fruit is in stock
    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()