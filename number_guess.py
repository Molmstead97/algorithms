import sys

def binary_search(low, high):
    
    for i in range(10):
        mid = (low + high) // 2
        response = input(f"\nIs your number {mid}? ( y | n ) ")
        
        if response == "y":
            print("\nI win GG.")
            sys.exit()
        elif response == "n":
            response = input(f"\nIs your number lower than {mid}? ( y | n ) ")
            
            if response == "y":
                high = mid - 1
            elif response == "n":
                low = mid + 1
            else:
                print("\nInvalid input. Enter 'y' or 'n'.")
        else:
            print("\nInvalid input. Enter 'y' or 'n'.")

    print("\nYou win this time.")


def main():
    print("\nWelcome to Number Guesser!")
    print("\nThink of a number between 1 and 100.")
    binary_search(1, 100)


if __name__ == "__main__":
    main()
