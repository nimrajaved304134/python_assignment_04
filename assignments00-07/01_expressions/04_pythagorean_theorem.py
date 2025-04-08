import math

def main():

    # Prompt values of base and perprndicular for calculating hypotaneous
    base = float(input('Enter the length of base of right-angled triangle: '))
    perprndicular = float(input('Enter the length of perpendicular of right-angled triangle: '))

    # Calculate hypotaneous
    hypotaneous = math.sqrt(base**2 + perprndicular**2)

    # Print results
    print(f'The hypotaneous of right-angled triangle with given base and perpendicular is {hypotaneous}.')

if __name__ == '__main__':
    main()
