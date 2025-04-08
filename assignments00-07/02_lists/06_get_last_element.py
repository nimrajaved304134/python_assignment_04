def get_first_element(lst):
    """Prints the last element of a given non-empty list."""
    print("The last element in the list is:", lst[-1])

def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)

    get_first_element(lst)

if __name__ == '__main__':
    main()