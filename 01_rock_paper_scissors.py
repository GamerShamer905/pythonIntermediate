from random import choice
import time
def win_condition(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif player_move == "rock" and computer_move == "paper":
        return "computer"
    elif player_move == "rock" and computer_move == "scissors":
        return "player"
    elif player_move == "scissors" and computer_move == "rock":
        return "computer"
    elif player_move == "scissors" and computer_move == "paper":
        return "player"
    elif player_move == "paper" and computer_move == "rock":
        return "player"
    elif player_move == "paper" and computer_move == "scissors":
        return "computer"
moves = ["rock","paper","scissors"]
player_wins = 0
computer_wins = 0
rounds = int(input("How many rounds?: "))
print("Ready?")
for i in range(rounds):
    print("Rock")
    time.sleep(0.5)
    print("Paper")
    time.sleep(0.5)
    print("Scissors")
    time.sleep(0.5)
    print("Shoot!")
    time.sleep(0.5)
    player_move = input("What move do you use?: ").lower()
    computer_move = choice(moves)
    winner = win_condition(player_move,computer_move)
    if winner == "tie":
        print(f"You tied since you both played {player_move}")
    if winner == "computer":
        print(f"The AI won as you played {player_move}, and the AI played {computer_move}")
        computer_wins += 1
        print(f"Currently, you have {player_wins} and the AI has {computer_wins}")
    if winner == "player":
        print(f"You won as you played {player_move}, and the AI played {computer_move}")
        player_wins += 1
        print(f"Currently, you have {player_wins} and the AI has {computer_wins}")
    time.sleep(2)

if player_wins == computer_wins:
    print("TIEBREAKER ROUND")
    tie = True
    while tie:
        print("Ready?")
        for i in range(rounds):
            print("Rock")
            time.sleep(0.5)
            print("Paper")
            time.sleep(0.5)
            print("Scissors")
            time.sleep(0.5)
            print("Shoot!")
            time.sleep(0.5)
            player_move = input("What move do you use?: ").lower()
            computer_move = choice(moves)
            winner = win_condition(player_move,computer_move)
            if winner == "tie":
                print("AGAIN")
            if winner == "player":
                player_wins += 1
                tie = False
                break
            if winner == "computer":
                computer_wins += 1
                tie = False
                break

if player_wins > computer_wins:
    print("YOU WON!")
    if player_wins - computer_wins <= 2:
        print("It was a close round!")
    elif player_wins <= rounds - 2:
        print("It was an average round, but you still won")
    elif player_wins == rounds:
        print("You destroyed the AI")

if player_wins < computer_wins:
    print("The AI won...")
    if computer_wins - player_wins <= 2:
        print("It was a close round!, but you still lost")
    elif computer_wins <= rounds - 2:
        print("It was an average round, do better next time")
    elif computer_wins == rounds:
        print("The AI destroyed you.")


