from customtkinter import *
from PIL import Image
from random import randint,choice
from tkinter import messagebox
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

label2.image=img_ctk
def button_click():
    global k1,k2,n,user1,user2,count_user1,count_user2

    random_image_path = choice(image_paths)
    img = Image.open(random_image_path)
    img_ctk.configure(light_image=img)
    label2.configure(image=img_ctk)

    if n%2==0:
        label1.configure(text=f"кубик кинь {user1} гравець")
        k1+=1
        count_user1=image_paths.index(random_image_path)+1
    else:
        label1.configure(text=f"кубик кинь {user2} гравець")
        k2+=1
        count_user2=image_paths.index(random_image_path)+1
    if n>0 and k1==k2:
        if count_user2>count_user1:
            messagebox.showinfo("Результат", f"Вирав  {user2}  гравець")
        elif count_user1>count_user2:
            messagebox.showinfo("Результат", f"Вирав {user1} гравець")
        else:
            messagebox.showinfo("Результат", "Рівна кількість очок")

    print(n,k1,k2,count_user1,count_user2)
    n=n+1
def button_click():
    random_image_path = choice(image_paths)
    img = Image.open(random_image_path)
    img_ctk.configure(light_image=img)
    label2.configure(image=img_ctk)
button1=CTkButton(win,text="Ok",command=button_click)

button1.grid(row=3,column=1)
count_user1=0
count_user2=0

k1=0
k2=0
n=0
dialog = CTkInputDialog(text="Введіть ім'я 1 гравця", title="Test")
user1 = dialog.get_input()
dialog = CTkInputDialog(text="Введіть ім'я 2 гравця", title="Test")
user2 = dialog.get_input()
label1.configure(text=f"кубик кинь {user1} гравець")



button1=CTkButton(win,text="Ok",command=button_click)
button1.grid(row=3,column=1)
win.mainloop()




