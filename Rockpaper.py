import random
import tkinter as tk

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def find_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_round(player_choice):
    global player_score, computer_score

    computer_choice = get_computer_choice()
    outcome = find_winner(player_choice, computer_choice)

    if outcome == "tie":
        result_text.set(f"It's a tie! Both chose {player_choice}.")
    elif outcome == "player":
        result_text.set(f"You win! {player_choice} beats {computer_choice}.")
        player_score += 1
    else:
        result_text.set(f"Computer wins! {computer_choice} beats {player_choice}.")
        computer_score += 1

    score_text.set(f"Score: You {player_score} - Computer {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score, computer_score = 0, 0
    result_text.set("Make your choice to start the game.")
    score_text.set("Score: You 0 - Computer 0")

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")

player_score = 0
computer_score = 0

result_text = tk.StringVar()
result_text.set("Make your choice to start the game.")
score_text = tk.StringVar()
score_text.set("Score: You 0 - Computer 0")

tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 16)).pack(pady=10)
tk.Label(window, textvariable=result_text, font=("Arial", 12)).pack(pady=5)
tk.Label(window, textvariable=score_text, font=("Arial", 12)).pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play_round("rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play_round("paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play_round("scissors")).grid(row=0, column=2, padx=5)

tk.Button(window, text="Reset Game", font=("Arial", 12), command=reset_game).pack(pady=10)

window.mainloop()
