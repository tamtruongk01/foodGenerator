import tkinter as tk
import foodGenerator

window = tk.Tk()
def clicked():
    secondWindow = tk.Tk()
    text = tk.Text(secondWindow, bg="light blue", height = 10, font="Helvetica")
    text.insert(tk.INSERT, foodGenerator.foodGenerator())
    text.pack()

mainScreen = tk.Canvas(window, bg="bisque2", height=320, width=640)
generatingButton = tk.Button(window, bg="navajo white", text="Click here to generate a meal", command=clicked)
generatingButton.pack()
mainScreen.pack()
window.mainloop()