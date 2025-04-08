import random

Num_Sides= 6

def roll_dice():
    dice1 = random.randint(1, Num_Sides)
    dice2 = random.randint(1, Num_Sides)
    total = dice1 + dice2
    print(f"Die 1: {dice1}, Die 2: {dice2} → Total: {total}")

def main():
    
    dice1 = 10  
    print(f"die1 in main() starts as: {dice1}")

    for _ in range(3):
        roll_dice()
    
    print(f"die1 in main() is still: {dice1}")  

if __name__ == '__main__':
    main()
