def main ():
    # Prompt the user for a temperature in Fahrenheit
    fahrenheit= float(input('Enter a temperature in fahrenheit: '))

    # Convert to Celsius: C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9

    # Display the result
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == '__main__':
    main()

