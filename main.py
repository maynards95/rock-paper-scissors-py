import random


#play function, plays one round
def play():
    #prompts user for choice
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    #if user and computer have the same choice it is a tie
    if user == computer:
        return 'tie'

    # rock > scissors, scissors > paper, paper > rock
    if is_win(user, computer):
        return 'You won!'

    # if its not a tie and the user did not win, print you lost
    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        #return true for a win!
        return True

#calls print function
print(play())