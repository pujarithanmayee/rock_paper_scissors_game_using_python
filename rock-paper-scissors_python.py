import random



def get_choices():
    options = ["rock","paper","scissors"]
    computer_choice= random.choice(options)
    player_choice = input("enter a choice(rock, paper, scissors): ")
    choices = {"player": player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
       return "it is a tie!"
    elif player == "rock": 
        if computer == "scissors":
            return "rock smahes scissors! y0u win"
        else: 
         return"u loose"

    elif player == "paper": 
        if computer == "rock":
            return " y0u win"
        else: 
         return"u loose"
        
    elif player == "scissors": 
        if computer == "paper":
            return " y0u win"
        else: 
         return"u loose"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)


