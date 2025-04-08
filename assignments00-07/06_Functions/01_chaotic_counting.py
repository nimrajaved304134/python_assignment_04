import random
import time

# Configurable chaos parameters
DONE_LIKELIHOOD = 0.3  # 30% chance to stop early
MOOD_SWINGS = ["angry", "bored", "excited", "confused"]  # Possible moods

def chaotic_counting():
    mood = random.choice(MOOD_SWINGS)  # Random mood
    print(f"\nCounting in a {mood} tone...\n")
    
    for i in range(10):
        curr_num = i + 1
        
        if done():
            print(f"\n*{mood.upper()} INTERRUPTION*")
            print("I don't feel like counting anymore!")
            return  # Exit early
        
        # Unpredictable delays (0.1s to 1.5s)
        time.sleep(random.uniform(0.1, 1.5))
        
        # Randomly shout numbers > 5
        if curr_num > 5 and random.random() < 0.4:
            print(f"{curr_num}!", end=" ")
        else:
            print(curr_num, end=" ")
    
    print("\n*Phew* I made it to 10!")

def done():
    """Returns True randomly or if a cosmic event happens (RNG < 0.3)."""
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count to 10... or until chaos takes over.")
    chaotic_counting()
    print("\n*Chaotic counting session ended*\n")

if __name__ == "__main__":
    main()