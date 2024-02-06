import ascii_magic
import tkinter as tk
from PIL import Image,ImageTk

win=tk.Tk()

win.configure(background="black")
L1=tk.Label()
L1.pack()
output = ascii_magic.from_image("D:\\python 3.8\\projects\\static\\apj3.png")
output.to_terminal()
photo = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Pictures\\Screenshots\\apja.png"))



L1.configure(image=photo)

win.mainloop()

