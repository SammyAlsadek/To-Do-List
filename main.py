from app_class import *

# start application
if __name__ == "__main__":
    
    # set up window
    window = tkinter.Tk()
    window.title("To-Do List")

    # start application
    app = App(window)
    
    # loop through program 
    window.mainloop()
