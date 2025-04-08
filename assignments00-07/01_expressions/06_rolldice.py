import random

num_sides = 6

def main():

    # Roll dice
    dice1:int = random.randint(1 , num_sides)
    dice2:int = random.randint(1 , num_sides)

    # Get their total
    total:int = dice1 + dice2

    # Print out the results
    print("Dice have", num_sides, "sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()