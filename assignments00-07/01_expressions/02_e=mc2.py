# The speed of light in m/s
C: int = 299792458

def main():
    mass = float(input('Enter mass in kgn: '))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    energy:float= mass * (C**2)

    # Display work to the user
    print("e = m * C^2")
    print("m = " + str(mass) + " kg")
    print("C = " + str(C) + " m/s")

    print(str(energy) + " joules of energy!")

if __name__ == '__main__':
    main()