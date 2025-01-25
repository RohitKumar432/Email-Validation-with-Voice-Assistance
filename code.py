import re
import tkinter as tk
from tkinter import ttk
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def validate_email():
    """Validate the email address and provide voice feedback."""
    email = email_entry.get()
    
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        result = "Valid Email Address"
        result_label.config(text=result, foreground="green")
        speak(result)
    else:
        result = "Invalid Email Address"
        result_label.config(text=result, foreground="red")
        speak(result)

root = tk.Tk()
root.title("Email Validator with Voice Assistance")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TLabel", font=("Helvetica", 12), padding=5)

header_label = tk.Label(
    root, text="Email Validator", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333"
)
header_label.pack(pady=20)

input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

email_label = ttk.Label(input_frame, text="Enter Email Address:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

email_entry = ttk.Entry(input_frame, width=40, font=("Helvetica", 12))
email_entry.grid(row=0, column=1, padx=5, pady=5)

validate_button = ttk.Button(root, text="Validate", command=validate_email)
validate_button.pack(pady=15)

result_label = tk.Label(
    root, text="", font=("Helvetica", 14, "italic"), bg="#f0f4f7"
)
result_label.pack(pady=20)

footer_label = tk.Label(
    root, text="Powered by Python | Voice Assistance Enabled", font=("Helvetica", 10), bg="#f0f4f7", fg="#555"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
