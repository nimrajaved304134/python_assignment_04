def main():

    # Prompt user number to square it

    number = float(input('Enter a number to get its squared value: '))

    # Calculate the square of a number
    square= number * number

    # Print the results
    print(f"The sqaure of {number} is {square:.2f}.")

if __name__ == '__main__':
    main()