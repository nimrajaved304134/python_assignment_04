from collections import defaultdict

def get_numbers():
    """Collect numbers from user until empty input"""
    numbers = []
    print("Enter numbers one by one (press Enter to finish):")
    while True:
        num = input("Enter a number: ").strip()
        if not num:  # Empty input ends the collection
            break
        try:
            numbers.append(int(num))
        except ValueError:
            print("Please enter a valid integer!")
    return numbers

def count_numbers(numbers):
    """Count occurrences of each number using defaultdict"""
    counts = defaultdict(int)
    for num in numbers:
        counts[num] += 1
    return dict(sorted(counts.items()))  # Return sorted dictionary

def display_counts(counts):
    """Display the counts in a user-friendly format"""
    print("\nNumber Counts:")
    for num, count in counts.items():
        print(f"{num} appears {count} time{'s' if count != 1 else ''}")

def main():
    print("=== Number Counter Program ===")
    numbers = get_numbers()
    if not numbers:
        print("No numbers were entered!")
        return
        
    counts = count_numbers(numbers)
    display_counts(counts)

if __name__ == '__main__':
    main()