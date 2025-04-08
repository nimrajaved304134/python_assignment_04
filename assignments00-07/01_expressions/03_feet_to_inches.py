# Value of 1 foot in inches
foot:int = 12

def main():

    # Ask user length in feet
    feet = float(input('Enter length in feet: '))

    # Convert feet in to inches
    inches:float = feet * foot

    # Display result
    print(f'{feet} feet is equal to {inches} inches.')

if __name__ == '__main__':
    main()

