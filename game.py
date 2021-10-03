import random

while True:
    my_answer = input("choose: rock, paper or scissors:")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("plz, choose a correct answer")
        continue

    
    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"computer choose : {computer_answer}")

    if my_answer == computer_answer:
        print("game tied")
        continue

    elif my_answer == "paper" and computer_answer == "rock":
        print("you won")
        break

    elif my_answer == "rock" and computer_answer == "scissors":
        print("you won")
        break

    elif my_answer == "scissors" and computer_answer == "paper":
        print("you won") 
        break

    else:
        print("you lose. try again !")       


