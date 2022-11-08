
def main():

    import random


    def play():
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return 'It\'s a tie'

        # r > s, s > p, p > r
        if is_win(user, computer):
            return 'You won!'

        return 'You lost!'

    def is_win(player, opponent):
        # return true if player wins
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
                or (player == 'p' and opponent == 'r'):
            return True
        else:
            print("Please input a valid choice")
            return play()


    print(play())


    def restart():
        repeat = input("Do you wish to play again? 'y' for yes, 'n' for no\n")
        if repeat == 'y':
            main()
        elif repeat == 'n':
            print("Goodbye. See you next time")
            exit()
        else :
            print("Please input a valid answer")
            return restart()

    print(restart())

main()