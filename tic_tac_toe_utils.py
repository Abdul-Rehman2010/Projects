import tkinter as tk
main = tk.Tk()
grid_buttons = []

def left_click(event):
    event.widget.config(text="X", font=("Arial", 16)) 
    event.widget.config(state="disabled")
    event.widget.unbind("<Button-1>")
    event.widget.unbind("<Button-3>") 
    check_button_text(event.widget)

def right_click(event):
    event.widget.config(text="O", font=("Arial", 16)) 
    event.widget.config(state="disabled")
    event.widget.unbind("<Button-3>") 
    event.widget.unbind("<Button-1>")
    check_button_text(event.widget)

def check_button_text(button):
    win = False

    for i in range(3):
        #check rows
        if grid_buttons[i][0].cget("text") == grid_buttons[i][1].cget("text") == grid_buttons[i][2].cget("text") and grid_buttons[i][0].cget("text") != "":
            print(f"{grid_buttons[i][0].cget('text')} wins")


        #check colums
        if grid_buttons[0][i].cget("text") == grid_buttons[1][i].cget("text") == grid_buttons[2][i].cget("text") and grid_buttons[0][i].cget("text") != "":
            print(f"{grid_buttons[0][i].cget('text')} wins")


    #check diagonal
    if grid_buttons[0][0].cget("text") == grid_buttons[1][1].cget("text") == grid_buttons[2][2].cget("text") and grid_buttons[0][0].cget("text") != "":
        print(f"{grid_buttons[0][0].cget('text')} wins")  
        
    if grid_buttons[0][2].cget("text") == grid_buttons[1][1].cget("text") == grid_buttons[2][0].cget("text") and grid_buttons[0][2].cget("text") != "":
        print(f"{grid_buttons[0][2].cget('text')} wins")
        
