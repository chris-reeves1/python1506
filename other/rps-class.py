import random

class Rock_paper_scissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def play_game(self):
        while True:
            player_choice = input("choose rock, paper or scissors: ")
            computer_choice = random.choice(self.choices)

            print(f"Player choice: {player_choice}")
            print(f"Computer choice: {computer_choice}")

            if player_choice not in self.choices:
                print("invalid choice try again!")
            elif player_choice == computer_choice:
                print("its a tie!")
            elif player_choice == "rock" and computer_choice == "scissors":
                print("Player wins!")
                self.player_score += 1
            elif player_choice == "paper" and computer_choice == "rock":
                print("Player wins!")
                self.player_score += 1
            elif player_choice == "scissor" and computer_choice == "paper":
                print("Player wins!")
                self.player_score += 1
            else:
                print("computer wins")
                self.computer_score += 1

            self.rounds_played += 1

            print(f"Rounds played: {self.rounds_played}")
            print(f"Player wins: {self.player_score}")
            print(f"Computer wins: {self.computer_score}")

            play_again = input("play again (y/n): ")

            if play_again.lower() == "y":
                continue
            else: 
                print("thanks for playing!!!")
                break


rock = Rock_paper_scissors()

rock.play_game()

