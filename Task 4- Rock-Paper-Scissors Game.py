import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()

    player_label.config(text=f"Your choice: {user_choice}")
    computer_label.config(text=f"Computer's choice: {computer_choice}")

    result_text = determine_winner(user_choice, computer_choice)
    result.set(result_text)

app = tk.Tk()
app.title("Rock, Paper, Scissors Game")

user_choice_var = tk.StringVar()
user_choice_var.set("Rock")

label = tk.Label(app, text="Choose Rock, Paper, or Scissors:")
label.pack()

choices = tk.OptionMenu(app, user_choice_var, "Rock", "Paper", "Scissors")
choices.pack()

play_button = tk.Button(app, text="Play", command=play_game, padx=10, pady=5)
play_button.pack()

player_label = tk.Label(app, text="Your choice: ")
player_label.pack()

computer_label = tk.Label(app, text="Computer's choice: ")
computer_label.pack()

result = tk.StringVar()
result.set("Result will be shown here.")
result_label = tk.Label(app, textvariable=result, font=("Arial", 12, "bold"))
result_label.pack()

app.mainloop()
