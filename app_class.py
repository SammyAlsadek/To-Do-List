import tkinter
import tkinter.messagebox
import pickle
from datetime import datetime

# get current day
today = datetime.now()
current_day = today.strftime("%m/%d/%y")

# application class
class App:

    # initialize application
    def __init__(self, window):

        ###### application methods ######

        # adds a task to the listbox
        def add_task():
            
            # get textbar entry
            task = entry_textbar.get()

            # add the new task
            if task != "":
                listbox_entries.insert(tkinter.END, current_day + " - " + task)
                entry_textbar.delete(0, tkinter.END) # clear textbar

            # send warning if textbar is empty
            else:
                tkinter.messagebox.showwarning(title = "WARNING", message = "Must Enter Task!")

        # deletes a task from the listbox
        def delete_task():
            try:
                task = listbox_entries.curselection()[0] # grab selected task
                listbox_entries.delete(task) # delete selected task

            # send warning if no task is selected
            except:
                tkinter.messagebox.showwarning(title = "WARNING", message = "Must Select Task!")

        # loads prexisting tasks to the listbox
        def load_tasks():
            try:
                tasks = pickle.load(open("tasks.dat", "rb"))
                listbox_entries.delete(0, tkinter.END)

                # loop through tasks in .dat file and add them to the listbox
                for task in tasks:
                    listbox_entries.insert(tkinter.END, task)

            # send warning if there is no saves file
            except:
                tkinter.messagebox.showwarning(title = "WARNING", message = "No Saved File!")

        # saves prexisting tasks from the listbox
        def save_tasks():
            tasks = listbox_entries.get(0, listbox_entries.size())
            pickle.dump(tasks, open("tasks.dat", "wb"))

        ###### application GUI ######
        
        # set up top label
        label = tkinter.Label(window, text = "My To-Do List", font=("Arial", 26), width = 20, height = 2, fg = "#ffffff", bg = "#f7983e")
        label.pack()

        # set up add frame
        add_frame = tkinter.Frame(window)
        add_frame.pack()

        # set up text bar for entries
        entry_textbar = tkinter.Entry(add_frame, width = 24)
        entry_textbar.pack(side = tkinter.LEFT)

        # add button
        add_button = tkinter.Button(add_frame, text = "ADD", fg = "#d66f0d", width = 8, command = add_task)
        add_button.pack(side = tkinter.RIGHT)

        # set up task frame
        task_frame = tkinter.Frame(window)
        task_frame.pack()

        # set up scroll bar
        scrollbar = tkinter.Scrollbar(task_frame)
        scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

        # set up listbox
        listbox_entries = tkinter.Listbox(task_frame, width = 32, height = 10)
        listbox_entries.pack(side = tkinter.LEFT, fill = tkinter.Y)

        # conigure the scrollbar to the list box
        listbox_entries.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox_entries.yview)

        # delete button
        delete_button = tkinter.Button(window, text = "DELETE", fg = "#d66f0d", width = 33, height = 2, command = delete_task)
        delete_button.pack()

        # load tasks button
        load_tasks_button = tkinter.Button(window, text = "LOAD TASKS", fg = "#d66f0d", width = 33, height = 2, command = load_tasks)
        load_tasks_button.pack()

        # save tasks button
        save_tasks_button = tkinter.Button(window, text = "SAVE TASKS", fg = "#d66f0d", width = 33, height = 2, command = save_tasks)
        save_tasks_button.pack()
