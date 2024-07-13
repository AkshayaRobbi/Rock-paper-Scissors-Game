from tkinter import *
from PIL import Image, ImageTk
import random
import sys
# Define the tkinter instance
win = Tk()
win.title("Rock Paper Scissors Game")
# Define the size of the tkinter frame
win.geometry("1000x600")

title = Label(win, text="Rock Paper Scissors Game", font=("Times", 20))
title.pack(pady=10)

comp_score = Label(win, text="Computer Score", font=("Times", 15))
comp_score.place(x=30, y=30)
comp_count=0
comp_entry=Entry(win,font=("Times", 15))
comp_entry.place(x=30,y=60)
comp_entry.insert(0,str(comp_count))

user_score = Label(win, text="User Score", font=("Times", 15))
user_score.place(x=800, y=30)
user_count=0
user_entry=Entry(win,font=("Times", 15))
user_entry.place(x=800,y=60)
user_entry.insert(0,str(user_count))

# Mapping numbers to image paths
image_paths = {
    0: 'C:/Users/user/OneDrive/Documents/Ak/r.jpg',
    1: 'C:/Users/user/OneDrive/Documents/Ak/p.jpg',
    2: 'C:/Users/user/OneDrive/Documents/Ak/s.jpg'
}

def play(user_choice):
    # Randomly choose a number for the computer (0, 1, or 2)
    comp_choice = random.choice([0, 1, 2])
    chosen_image = image_paths[comp_choice]
    
    # Load and display the computer's chosen image
    comp_img = Image.open(chosen_image)
    comp_img = comp_img.resize((200, 200))
    comp_img = ImageTk.PhotoImage(comp_img)
    comp_label.config(image='')
    win.update()  # Force update the window
    win.after(200)  # Delay for 200 milliseconds
    comp_label.config(image=comp_img)
    comp_label.image = comp_img  # Keep a reference to avoid garbage collectio

     
    # Load and display the player's chosen image
    user_img = Image.open(image_paths[user_choice])
    user_img = user_img.resize((200, 200))
    user_img = ImageTk.PhotoImage(user_img)
    user_label.config(image='')  # Hide the image
    win.update()  # Force update the window
    win.after(200)  # Delay for 200 milliseconds
    user_label.config(image=user_img) 
    user_label.image = user_img  # Keep a reference to avoid garbage collection

    #win determination
    global user_count,comp_count
    if(comp_choice == user_choice):
        user_count=user_count+1
        comp_count=comp_count+1
        update_comp_score(comp_count)
        update_user_score(user_count)
    elif(comp_choice == 0 and user_choice == 2):
        comp_count=comp_count+1
        update_comp_score(comp_count)
    elif(user_choice == 0 and comp_choice == 2):
        user_count=user_count+1
        update_user_score(user_count)
    elif(comp_choice>user_choice):
        comp_count=comp_count+1
        update_comp_score(comp_count)
    elif(comp_choice<user_choice):
        user_count=user_count+1
        update_user_score(user_count)

    if(user_count==10):
        print("Hurray! You Won")
        win.destroy()
    elif(comp_count==10):
        print("You Lose, Better luck next time!")
        win.destroy()

def update_comp_score(new_score):
    comp_entry.delete(0, "end")  # Remove existing value
    comp_entry.insert(0, str(new_score))  # Insert new value

def update_user_score(new_score):
    user_entry.delete(0, "end")  # Remove existing value
    user_entry.insert(0, str(new_score)) 

comp_label = Label(win)
comp_label.place(x=200, y=150)

versus_label=Label(win,text="Vs",font=("Times",50))
versus_label.place(x=470,y=250)

user_label = Label(win)
user_label.place(x=600, y=150)


choose = Label(win, text="Select any one option", font=("Times", 20))
choose.place(x=400,y=400)
# Load images for the buttons
rock_img = Image.open(image_paths[0])
rock_img = rock_img.resize((100, 100))
rock_img = ImageTk.PhotoImage(rock_img)

paper_img = Image.open(image_paths[1])
paper_img = paper_img.resize((100, 100))
paper_img = ImageTk.PhotoImage(paper_img)

scissors_img = Image.open(image_paths[2])
scissors_img = scissors_img.resize((100, 100))
scissors_img = ImageTk.PhotoImage(scissors_img)

# Create buttons for rock, paper, and scissors
rock_button = Button(win, image=rock_img, command=lambda: play(0))
rock_button.place(x=250, y=450)

paper_button = Button(win, image=paper_img, command=lambda: play(1))
paper_button.place(x=450, y=450)

scissors_button = Button(win, image=scissors_img, command=lambda: play(2))
scissors_button.place(x=650, y=450)


win.mainloop()
