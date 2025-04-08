def print_ones_digit(num):
    """
    Prints the ones digit of an integer using modulo arithmetic.
    
    Parameters:
        num (int): The number whose ones digit we want to print
        
    Example:
        >>> print_ones_digit(327)
        7
        >>> print_ones_digit(-19)
        9
    """
    ones_digit = abs(num) % 10  # Handle negative numbers with abs()
    print(ones_digit)

def main():

    # Interactive version
    user_num = int(input("Enter a number: "))
    print_ones_digit(user_num)

if __name__ == '__main__':
    main()