def main():

    # Prompt the user for the three side lengths
    side1= float(input('Enter the length of first side of the triangle: '))
    side2= float(input('Enter the length of second side of the triangle: '))
    side3= float(input('Enter the length of third side of the triangle: '))

    # Calculate the perimeter (sum of all sides)
    perimeter = side1 + side2 + side3

    # print the results
    print(f"The perimeter of the triangle is {perimeter:.2f} units.")

if __name__ == '__main__':
    main()