from random import choice

valid_options = ["rock", "paper", "scissors", "hoya"]

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_options:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_options)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
# ... (there may be a bug in this logic :-)

if u == "rock" and c == "rock":
    print("It's a tie!")
elif u == "rock" and c == "paper":
    print("The computer wins")
elif u == "rock" and c == "scissors":
    print("The user wins")

elif u == "paper" and c == "rock":
    print("The computer wins")
elif u == "paper" and c == "paper":
    print("It's a tie!")
elif u == "paper" and c == "scissors":
    print("The user wins")

elif u == "scissors" and c == "rock":
    print("The computer wins")
elif u == "scissors" and c == "paper":
    print("The user wins")
elif u == "scissors" and c == "scissors":
    print("It's a tie!")
VALID_OPTIONS = ["rock", "paper", "scissors"]



def determine_winner(user_choice, computer_choice):
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice



if __name__ == "__main__":

    # only run the code below when we run this file from the command-line

    # but not when we try to import from this file


    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    result = determine_winner(u, c).lower()

    if result == u:
        print("YOU WON")
    elif result == c:
        print("COMPUTER WON")
    else:
        print("TIE")