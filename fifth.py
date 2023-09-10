import tkinter as tk 
from tkinter import *
import qrcode
from PIL import Image, ImageTk
root = tk.Tk()
global var2
root.geometry('600x600')
def create_qr():
    x = e1.get()
    y = qrcode.make(x)  
    y.save('myqr.jpg')
    photo = Image.open('myqr.jpg')
    ph = ImageTk.PhotoImage(photo)
    var2 = tk.Label(root, image=ph)
    var2.image = ph
    var2.pack()
var1 = tk.Label(root, text = 'Enter link to generate QR:')
var1.pack()
e1 = tk.Entry(root)
e1.pack()
b1 = tk.Button(root, text = 'Create QR Code', command = create_qr)
b1.pack()
var2 = tk.Label(root, image = '')
var1.pack()
root.mainloop()
