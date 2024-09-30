import customtkinter as ctk
import random

#Game logic
def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0 #reset attempts for each new game
    result_var.set("Guess a number between 1 and 100")
    entry_guess.delete(0, 'end')   #clears the text in the entry widget from any prev input
    attempts_var.set("Attempts: 0")  #resets attempts display

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        if guess < 1 or guess > 100:
            result_var.set("Please enter a number between 1 and 100.")
            return

        attempts += 1

        if guess < secret_number:
            result_var.set("Guess higher!")
        elif guess > secret_number:
            result_var.set("Guess lower!")
        else:
            result_var.set(f"You win! :D")
            attempts_var.set(f"Attempts: {attempts}")
    except:
        result_var.set("Please enter a valid number.")

#setting up main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Number Guessing Game")
app.geometry("400x350")

#variables
result_var = ctk.StringVar()
attempts_var = ctk.StringVar() #track attempts

#layout
frame = ctk.CTkFrame(app)
frame.pack(pady=20)

label_title = ctk.CTkLabel(frame, text="Number Guessing Game", font=("Arial", 24))
label_title.pack(pady=10)

label_instruction = ctk.CTkLabel(frame, textvariable=result_var, font=("Arial", 16))
label_instruction.pack(pady=10)

entry_guess = ctk.CTkEntry(frame, width=150)
entry_guess.pack(pady=10)

button_guess  = ctk.CTkButton(frame, text="Check guess", command=check_guess) #check_guess without () becz u want it to run when button is clicked not immediately when button is created
button_guess.pack(pady=10)

button_start = ctk.CTkButton(frame, text="Start New Game", command=start_game)
button_start.pack(pady=10)

label_attempts = ctk.CTkLabel(frame, textvariable=attempts_var, font=("Arial", 16))
label_attempts.pack(pady=10)

start_game()

app.mainloop()
