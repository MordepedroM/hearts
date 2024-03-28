import tkinter as tk
import pyperclip

def store_hearts():
    heart = "❤"

    message_length = 65535

    message = heart * message_length

    # Store the hearts message in the clipboard
    pyperclip.copy(message)
    status_label.config(text="Hearts message copied to clipboard.")

def paste_hearts():

    text = pyperclip.paste()
    print(text)  
    # You can now manually paste the hearts message into the chat using Ctrl+V


window = tk.Tk()
window.title("Hearts Sender")

status_label = tk.Label(window, text="")
status_label.pack()

store_button = tk.Button(window, text="Store Hearts", command=store_hearts)
store_button.pack()

paste_button = tk.Button(window, text="Paste Hearts", command=paste_hearts)
paste_button.pack()

window.mainloop()
