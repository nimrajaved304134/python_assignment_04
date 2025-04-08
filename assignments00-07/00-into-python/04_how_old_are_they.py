def main():

    # Given ages and relationships
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    # Print the results
    print(f"Anton is {anton} years old.")
    print(f"Beth is {beth} years old (6 years older than Anton).")
    print(f"Chen is {chen} years old (20 years older than Beth).")
    print(f"Drew is {drew} years old (Chen's age plus Anton's age).")
    print(f"Ethan is {ethan} years old (same age as Chen).")

    if __name__ == '__main__':
        main()