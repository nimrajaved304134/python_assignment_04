from collections import defaultdict

class PhoneBook:
    def __init__(self):
        self.contacts = defaultdict(list)  # Allows multiple numbers per name
    
    def add_contacts(self):
        """Interactive contact addition with validation"""
        print("\nAdd contacts (leave name blank to finish):")
        while True:
            name = input("Name: ").strip()
            if not name:
                break
            number = input("Number: ").strip()
            if not number.isdigit():
                print("Invalid number! Use digits only.")
                continue
            self.contacts[name].append(number)
            print(f"Added {name}: {number}")

    def display_contacts(self):
        """Show all contacts with pretty formatting"""
        print("\n📱 Phone Book Contacts:")
        if not self.contacts:
            print("No contacts yet!")
            return
            
        for name, numbers in sorted(self.contacts.items()):
            print(f"\n{name}:")
            for i, num in enumerate(numbers, 1):
                print(f"  {i}. {num}")

    def contact_lookup(self):
        """Enhanced lookup with suggestions for similar names"""
        print("\n🔍 Contact Lookup")
        while True:
            query = input("Search name (blank to exit): ").strip().lower()
            if not query:
                break
                
            # Exact match
            if query in self.contacts:
                print(f"\n{query}:")
                for i, num in enumerate(self.contacts[query], 1):
                    print(f"  {i}. {num}")
                continue
                
            # Fuzzy matching
            matches = [name for name in self.contacts if query in name.lower()]
            if matches:
                print("\nDid you mean?")
                for name in matches:
                    print(f"- {name}")
            else:
                print("No contacts found!")

def main():
    print("🌟 Smart Phone Book Manager 🌟")
    pb = PhoneBook()
    
    while True:
        print("\nMenu:")
        print("1. Add Contacts")
        print("2. View All Contacts")
        print("3. Lookup Contacts")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ").strip()
        
        if choice == "1":
            pb.add_contacts()
        elif choice == "2":
            pb.display_contacts()
        elif choice == "3":
            pb.contact_lookup()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()