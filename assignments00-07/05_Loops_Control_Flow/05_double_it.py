def main():
    curr_value = int(input("Enter a number: "))
    steps = 0
    max_steps = 10  # Prevent infinite loops
    
    while curr_value < 100 and steps < max_steps:
        curr_value *= 2
        print(curr_value, end=" ")
        steps += 1
    
    if curr_value < 100:
        print("\nStopped after 10 steps (safety limit)")

if __name__ == '__main__':
    main()