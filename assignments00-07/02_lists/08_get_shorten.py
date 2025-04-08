# Maximum length that is allowed
MAX_LENGTH = 3  

# Function to remove elements that exceed list allowed length
def shorten(lst):
    while len(lst) > MAX_LENGTH: 
        removed_item = lst.pop() 
        print("Removed:", removed_item)  

# Main function
def main():
    lst = []  #
    
    # Take input from user
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)
    
    # display results
    print("Original list:", lst)  
    shorten(lst)  
    print("Shortened list:", lst)  


if __name__ == '__main__':
    main()