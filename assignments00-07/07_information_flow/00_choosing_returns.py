# Standard adult age
ADULT_AGE : int = 18 

# Age verifying function
def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    

# Main function
def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()