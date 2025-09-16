import tkinter as tki
import random

choices = ["rock", "paper", "scissors"]


def play(choice):
    computer_choice = random.choice(choices)
    result = ""

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "You Lose!"


    user_label.config(text="You chose: " + choice.capitalize())
    comp_label.config(text="Computer chose: " + computer_choice.capitalize())
    result_label.config(text=result)

root = tki.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

title_label = tki.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

user_label = tki.Label(root, text="You chose: ", font=("Arial", 12))
user_label.pack()

comp_label = tki.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_label.pack()

result_label = tki.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

button_frame = tki.Frame(root)
button_frame.pack()

rock_button = tki.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tki.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tki.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

exit_button = tki.Button(root, text="Exit", command=root.destroy, bg="red", fg="white")
exit_button.pack(pady=10)

root.mainloop()
