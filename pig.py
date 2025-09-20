import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll


value=roll()
print(value)

while True:
    player=input("Enter the number of players (2-4): ")
    if player.isdigit():
        player=int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must be between 2-4.")
            
    else:
        print("Invalid, try again!")

max_score=50
player_scores=[0 for _ in range(player)]

while max(player_scores)<max_score:

    for player_idx in range(player):
        print("\n Player number ",player_idx+1,"has just started")
        print("Your total score is: ",player_scores[player_idx],"\n")
        current_score=0

        while True:
            should_roll=input("Do you want to roll (y)? ").lower()
            if should_roll != "y":
                break
            
            value=roll()
            if value==1:
                print("You rolled a 1! Turn over")
                current_score=0
                break
            else:
                print("You rolled a: ",value)
                current_score+=value
            
            print("Your score is: ",current_score)
    player_scores[player_idx]+=current_score
    print("Your total score is: ",player_scores[player_idx])

max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print("Player number",winning_idx+1,"is the winner with a score of:",max_score)