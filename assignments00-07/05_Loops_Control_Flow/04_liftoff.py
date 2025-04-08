def countdown(n):
    if n >= 1:
        print(n, end=" ")
        countdown(n - 1)  # Recursive call
    else:
        print("Liftoff!")

def main():
    countdown(10)  # Start from 10

if __name__ == '__main__':
    main()