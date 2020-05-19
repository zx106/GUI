# Import module 
import tkinter 
import random 
import tkinter.messagebox

# Create root window
root = tkinter.Tk()

# Change root window background
root.configure(bg = "white")

# Change the title  
root.title("My Super To Do List") 

# Change the window size
root.geometry("325x275")

# Create an empty list 
tasks = []

# For testing purpose
# tasks = ["Do homework"]

def update_listbox(): 
    clear_listbox()
    for task in tasks: 
        lbl_tasks.insert("end", task) 

def clear_listbox(): 
    lbl_tasks.delete(0, "end")

def add():
    # Get the task to add
    task = txt_input.get()
    # Make sure the task is not empty 
    if task != "": 
        # Append to the list
        tasks.append(task)
        # Update the task to add
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter a task.")
    txt_input.delete(0, "end")

def delete_all():
    confirmed = tkinter.messagebox.askyesno("Comfirm: Delete All", "Do you really want to delete all?")
    if confirmed == True: 
        global tasks 
        # Clear the tasks list 
        tasks = [] 
        # Upadte the list box 
        update_listbox() 
    
def delete():
    # Get the text of the currently selected task
    task = lbl_tasks.get("active")
    # Confirm it is in the list 
    if task in tasks:
        tasks.remove(task)
    update_listbox() 

def sort_a(): 
    tasks.sort()
    update_listbox()

def sort_d(): 
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose(): 
    # Choose random tasks 
    task = random.choice(tasks) 
    # Update the display label 
    lbl_display["text"] = task

def number(): 
    number_of_tasks = len(tasks) 
    message = "Number of tasks: {}".format(number_of_tasks)
    lbl_display["text"] = message

def quit(): 
    confirm = tkinter.messagebox.askyesno("Please confirm", "Do you want to quit?")
    if confirm == True:
        quit()
    else:
        print("Not confirmed")


# Start the main events loop
lbl_title = tkinter.Label(root, text = "To-Do-List", bg = "White")
lbl_title.grid(row = 0, column = 0)

lbl_display = tkinter.Label(root, text = "", bg = "White")
lbl_display.grid(row = 0, column = 1)

txt_input = tkinter.Entry(root, width = 15)
txt_input.grid(row = 1, column = 1) 

lbl_display = tkinter.Label(root, text = "", bg = "white")  
lbl_display.grid(row = 0, column = 1) 

btn_add = tkinter.Button(root, text = "Add Task", fg = "black", width = 16, command = add) 
btn_add.grid(row = 1, column = 0)

btn_delete_all = tkinter.Button(root, text = "Delete All", fg = "black", width = 16, command = delete_all) 
btn_delete_all.grid(row = 2, column = 0)

btn_delete = tkinter.Button(root, text = "Delete", fg = "black", width = 16, command = delete) 
btn_delete.grid(row = 3, column = 0)

btn_sort_a = tkinter.Button(root, text = "Sort (ASC)", fg = "black", width = 16, command = sort_a) 
btn_sort_a.grid(row = 4, column = 0)

btn_sort_a = tkinter.Button(root, text = "Sort (DESC)", fg = "black", width = 16, command = sort_d) 
btn_sort_a.grid(row = 5, column = 0)

btn_choose = tkinter.Button(root, text = "Choose Random", fg = "black", width = 16, command = choose) 
btn_choose.grid(row = 6, column = 0)

btn_number = tkinter.Button(root, text = "Number of Tasks", fg = "black", width = 16, command = number) 
btn_number.grid(row = 7, column = 0)

btn_exit = tkinter.Button(root, text = "Exit", fg = "black", width = 16, command = exit) 
btn_exit.grid(row = 8, column = 0)

lbl_tasks = tkinter.Listbox(root) 
lbl_tasks.grid(row = 2, column = 1, rowspan = 7)

root.mainloop() 














