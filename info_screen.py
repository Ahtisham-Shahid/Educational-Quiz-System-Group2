import tkinter as tk

# Use style.py if available, otherwise fall back
try:
    from style import APP_FONT, BG_COLOR, BTN_COLOR, TEXT_COLOR
except ImportError:
    APP_FONT = ("Arial", 13)
    BG_COLOR = "#fff8e1"
    BTN_COLOR = "#ff9800"
    TEXT_COLOR = "#4e342e"

def info_screen(username,email, start_quiz_callback):
    win = tk.Toplevel()
    win.title("Quiz Instructions")
    win.geometry("500x350")
    win.configure(bg=BG_COLOR)

    instructions = (
        f"Welcome to the Quiz, {username}!\n\n"
        "Instructions:\n"
        "- The quiz has multiple-choice questions.\n"
        "- Select one option and click Next.\n"
        "- You will get your score at the end.\n"
        "- Try to answer all questions to the best of your knowledge.\n"
    )

    tk.Label(
        win,
        text=instructions,
        justify="left",
        wraplength=450,
        font=APP_FONT,
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=30)

    tk.Button(
        win,
        text="Start Quiz",
        command=lambda: [win.destroy(), start_quiz_callback(username,email)],
        bg=BTN_COLOR,
        fg="white",
        font=("Arial", 12, "bold"),
        padx=10,
        pady=5
    ).pack(pady=10)
