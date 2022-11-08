
def main():

    import random
    import math
    import time

    def guess_number():
        # Game instructions
        print("Hello. Let's play a game. I will choose a random number between a lower and an upper bound based on your choice, and you have to guess what that number is.\n")

        # Receiving user lower bound input
        lower_bound = int(input("Please enter a lower bound of your choice: "))

        # Receiving user upper bound input
        upper_bound = int(input("\nPlease enter an upper bound of your choice: "))

        # Generating a random integer between lower and upper bounds
        x = random.randint(lower_bound, upper_bound)
        print("\nYou have only ", round(math.log(upper_bound - lower_bound + 1, 2)), " chances to guess the integer.\n")

        # Initializing the number of guesses
        count = 0

        # Algorithm for determining the minimum number of guesses based on range
        while count < math.log(upper_bound - lower_bound + 1,2):
            count += 1

            # Taking number guessed as input
            guess = int(input("Guess a number: "))

            # Testing the conditions
            if x == guess:
                print("\nCongratulations! You managed to guess the correct number in ", count, " tries.")
                # Once guessed, loop will break
                break
            elif x > guess:
                print("You guessed the number too small.")
            elif x < guess:
                print("You guessed the number too high.")

        # Output if player guesses is more than the required guesses
        if count >= math.log(upper_bound - lower_bound + 1, 2):
            print("\nThe number is %d" % x)
            print("\nBetter luck next time!")

    guess_number()


    def restart():
        repeat = input("\nDo you wish to play again? 'y' for yes, 'n' for no\n")
        if repeat == 'y':
            main()
        elif repeat == 'n':
            print("\nFarewell. See you next time.")
            time.sleep(2.5)
            exit()
        else :
            print("\nPlease input a valid answer.")
            return restart()

    print(restart())

main()