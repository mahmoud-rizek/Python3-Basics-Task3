import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
window = tk.Canvas(root, width=180, height=80)
window.pack()

def take_ss():
    screen_shot = pyautogui.screenshot() 
    save_path = asksaveasfilename()
    screen_shot.save(save_path+"_screenshot.png")

ss_button = tk.Button(text="TAKE SCREENSHOT", command=take_ss, font=10)
window.create_window(90, 40, window=ss_button)

root.mainloop()
