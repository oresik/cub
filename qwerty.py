from customtkinter import *
from PIL import Image
from random import randint,choice
win = CTk()
win.geometry('250x300')
win.title('кубик кинь')
img = Image.open('1.jpg')
img_ctk = CTkImage(light_image=img, size=(250, 200))
# Мітка для тексту
label1 = CTkLabel(win, text='кубик кинь',font=("None",30,"bold"),text_color="red")
label1.grid(row=0, column=0,columnspan=3)
# Мітка для малюнка

label2 = CTkLabel(win, text='', image=img_ctk)
label2.grid(row=1, column=1)
image_paths = [
    "1.jpg",
    "2.lpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg"]

img = Image.open("1.jpg")
img_ctk = CTkImage(light_image=img, size=(250, 200))
label2.image=img_ctk
def button_click():
    random_image_path = choice(image_paths)
    img = Image.open(random_image_path)
    img_ctk.configure(light_image=img)
    label2.configure(image=img_ctk)
    


button1=CTkButton(win,text="Ok",command=button_click)
button1.grid(row=3,column=1)
win.mainloop()

