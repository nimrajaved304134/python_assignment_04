def main():

    # Ask user two numbers to be divided
    num1 = float(input('Please enter an integer to be divided : '))
    num2 = float(input('Please enter an integer to divide by: '))

    # Calculation
    quotient = num1 // num2
    remainder = num1 % num2

    # Display results
    print(f'The result of this division is {quotient} with a remainder of {remainder}')

if __name__ == '__main__':
    main()