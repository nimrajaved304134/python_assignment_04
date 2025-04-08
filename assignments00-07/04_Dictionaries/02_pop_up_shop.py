def display_fruit_menu(fruits):
    """Display available fruits with prices in a formatted menu"""
    print("\n🍎 Welcome to the Fruit Shop! 🍌")
    print("Available Fruits:")
    print("-" * 30)
    for i, (fruit, price) in enumerate(fruits.items(), 1):
        print(f"{i}. {fruit.capitalize():<10} - ${price:.2f}")
    print("-" * 30)

def get_quantity(prompt):
    """Get valid quantity input from user"""
    while True:
        try:
            qty = int(input(prompt))
            if qty < 0:
                print("Please enter a positive number!")
                continue
            return qty
        except ValueError:
            print("Invalid input! Please enter a whole number.")

def calculate_discount(total):
    """Apply 10% discount for purchases over $100"""
    if total > 100:
        discount = total * 0.1
        print(f"\n🎉 Discount Applied! You saved ${discount:.2f}")
        return total - discount
    return total

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5,
        'strawberry': 0.5,
        'pineapple': 3.5
    }
    
    display_fruit_menu(fruits)
    
    total = 0
    cart = {}
    
    while True:
        print("\nEnter fruit number to add to cart (0 to checkout)")
        try:
            choice = int(input("Your choice: "))
            if choice == 0:
                break
            fruit = list(fruits.keys())[choice-1]
            qty = get_quantity(f"How many {fruit}s? (0 to cancel): ")
            if qty > 0:
                cost = fruits[fruit] * qty
                cart[fruit] = (qty, cost)
                total += cost
                print(f"Added {qty} {fruit}(s) for ${cost:.2f}")
        except (ValueError, IndexError):
            print("Invalid selection! Please try again.")
    
    if cart:
        total = calculate_discount(total)
        print("\n🛒 Your Order Summary:")
        for fruit, (qty, cost) in cart.items():
            print(f"{fruit.capitalize():<10} {qty:>3} x ${fruits[fruit]:.2f} = ${cost:.2f}")
        print("-" * 30)
        print(f"TOTAL: ${total:.2f}")
    else:
        print("\nYou didn't buy anything today. See you next time!")

if __name__ == '__main__':
    main()