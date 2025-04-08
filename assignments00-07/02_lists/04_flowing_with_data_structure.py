# Function to add 3 copies od data in lists showing its mutable behaviour
def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

# Main function
def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()