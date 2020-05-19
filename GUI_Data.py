# Import module 
import tkinter
import os
import tkinter.messagebox
import pickle

# Create root window
root = tkinter.Tk()

# Change root window background
root.configure(bg = "white")

# Change the title  
root.title("Album Database") 

# Change the window size
root.geometry("700x300")

# Create an empty list
items = {}

# For testing purpose
items["Taylor Swift"] = "Love"
items["Jane Doe"] = "Friend"
items["Justin Bieber"] = "Crazy"

def beep():
    os.system("say beep")

def update_listbox():
    keys = list(items.keys())
    keys.sort()  
    
    for key in keys: 
        lb_items.insert("end", key) 

def clear_listbox(): 
    lb_items.delete(0, "end")

def show_all():
    update_listbox()

def show_one():
    item = lb_items.get("active")
    message = "{} : {}".format(item, items[item])
    lbl_display["text"] = message

def add_one():
    choice = txt_input.get()
    one = choice.split(":")
    items[one[0]] = one[1]
    show_all()
    txt_input.delete(0, "end")

def delete_one():
    item = lb_items.get("active")
    del items[item]
    items.update() 
    print(items)
    beep()

def load_file():
    items = pickle.load(open("items.dat", "rb"))
    messagebox.showinfo("Please Confirm", "Are you sure?")
    
def save_file():
    data = text_input
    data = pickle.dump(data, open("Computer Science.dat", "wb"))
    messagebox.showinfo("Please Confirm", "Are you sure?")

def exit():
    confirm = tkinter.messagebox.askyesno("Please confirm", "Do you want to quit?")
    if confirm == True:
        quit()
    else:
        print("Not confirmed")

# Start the main events loop
lbl_title = tkinter.Label(root, text = "Album Database", bg = "White")
lbl_title.grid(row = 0, column = 0)

lbl_display = tkinter.Label(root, text = "", bg = "White")
lbl_display.grid(row = 0, column = 1)

txt_input = tkinter.Entry(root, width = 15)
txt_input.grid(row = 1, column = 1) 

lbl_display = tkinter.Label(root, text = "", bg = "white")  
lbl_display.grid(row = 0, column = 1) 

btn_show_all= tkinter.Button(root, text = "Show All", fg = "black", width = 16, command = show_all) 
btn_show_all.grid(row = 1, column = 0)

btn_show_one = tkinter.Button(root, text = "Show One", fg = "black", width = 16, command = show_one) 
btn_show_one.grid(row = 2, column = 0)

btn_add_one = tkinter.Button(root, text = "Add One", fg = "black", width = 16, command = add_one) 
btn_add_one.grid(row = 3, column = 0)

btn_delete_one = tkinter.Button(root, text = "Delete One", fg = "black", width = 16, command = delete_one) 
btn_delete_one.grid(row = 4, column = 0)

btn_load_file = tkinter.Button(root, text = "Load File", fg = "black", width = 16, command = load_file) 
btn_load_file.grid(row = 5, column = 0)

btn_save_file = tkinter.Button(root, text = "Save File", fg = "black", width = 16, command = load_file) 
btn_save_file.grid(row = 6, column = 0)

btn_quit = tkinter.Button(root, text = "Exit", fg = "black", width = 16, command = exit) 
btn_quit.grid(row = 7, column = 0)

lb_items = tkinter.Listbox(root) 
lb_items.grid(row = 2, column = 1, rowspan = 5)

root.mainloop() 







