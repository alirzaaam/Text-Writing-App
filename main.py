import keyboard
import time
import tkinter as tk 
from tkinter import END
import threading

LABEL = "If you don't type for more than 5 seconds, your text will disappear"
LAST_KEY_TIME = time.time()


window = tk.Tk()
window.geometry("500x400")
window.title("TEST")
font=('Times', 12, "bold")


txt_box = tk.Entry(window, bg='white', font=font, width=50)
txt_box.grid(row=1, column=1, padx=20, pady=20)

lbl = tk.Label(window, text=f"{LABEL}", font=font)
lbl.grid(row=3, column=1, padx=20, pady=20)





def on_key_event(e):
    global LAST_KEY_TIME
    LAST_KEY_TIME = time.time()

keyboard.on_press(on_key_event)

def check_idle():
    global LAST_KEY_TIME
    while True:
        if time.time() - LAST_KEY_TIME > 5:
            # print("⏰ More than 5")
            txt_box.delete(0, END)
            LAST_KEY_TIME = time.time()
        time.sleep(1)

# print("Listening")


threading.Thread(target=check_idle, daemon=True).start()
# keyboard.wait()  # Keeps the program running



window.mainloop()