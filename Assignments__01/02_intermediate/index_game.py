def get_item(collection, position):
    """Retrieves an item from the collection at specified position."""
    if position in range(len(collection)):
        return f"Retrieved: {collection[position]} (from position {position})"
    else:
        return f"Error: Position {position} is not valid for this collection"

def update_item(collection, position, replacement):
    """Updates an item in the collection with a new value."""
    if position in range(len(collection)):
        original = collection[position]
        collection[position] = replacement
        return f"Changed '{original}' to '{replacement}' at position {position}"
    else:
        return f"Error: Cannot update position {position}"

def extract_section(collection, begin, finish):
    """Extracts a section from the collection between begin and finish."""
    if 0 <= begin < len(collection) and 0 <= finish <= len(collection):
        return f"Extracted section: {collection[begin:finish]}"
    else:
        return "Error: The specified section boundaries are invalid"

def run_program():
    """Main program function that handles user interaction."""
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("List Operations Tool")
    print(f"Working with: {fruits}")
    
    while True:
        print("\nAvailable Commands:")
        print("1 - Retrieve an item")
        print("2 - Update an item")
        print("3 - Extract a section")
        print("0 - Quit program")
        
        try:
            command = input("\nEnter command number: ")
            
            if command == "1":
                position = int(input("Enter position to retrieve: "))
                print(get_item(fruits, position))
                
            elif command == "2":
                position = int(input("Enter position to update: "))
                replacement = input("Enter new value: ")
                print(update_item(fruits, position, replacement))
                print(f"Current list: {fruits}")
                
            elif command == "3":
                begin = int(input("Enter starting position: "))
                finish = int(input("Enter ending position: "))
                print(extract_section(fruits, begin, finish))
                
            elif command == "0":
                print("Program terminated. Thank you!")
                break
                
            else:
                print("Invalid command. Please try again.")
                
        except ValueError:
            print("Error: Please enter numeric values where required.")

# Program entry point
if __name__ == "__main__":
    run_program()