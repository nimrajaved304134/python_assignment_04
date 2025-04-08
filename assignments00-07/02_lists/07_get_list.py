def get_user_list():
    """Prompts the user to enter values and returns a list of those values."""
    lst = []
    print("Enter values one by one. Press Enter with no input to finish.")
    
    while True:
        val = input("Enter a value (or press Enter to stop): ").strip()
        if not val:  # Exit loop if input is empty
            break
        lst.append(val)
    
    return lst

def display_list_info(lst):
    """Displays the list and its first element if not empty."""
    if lst:
        print("\nHere's your list:", lst)
    else:
        print("\nThe list is empty!")

def main():
    lst = get_user_list()
    display_list_info(lst)

if __name__ == '__main__':
    main()