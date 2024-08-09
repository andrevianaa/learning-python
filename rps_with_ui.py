import tkinter as tk
import random

player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    player_label.config(text=f"You played: {player_choice}")
    computer_label.config(text=f"Computer played: {computer_choice}")

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!")
        player_score += 100
    else:
        result_label.config(text="You lose!")
        computer_score += 100

    score_label.config(text=f"Player: {player_score} - Computer: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

player_label = tk.Label(root, text="")
computer_label = tk.Label(root, text="")
result_label = tk.Label(root, text="")
score_label = tk.Label(root, text="")

rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

player_label.pack()
computer_label.pack()
result_label.pack()
score_label.pack()

root.mainloop()
