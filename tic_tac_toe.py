#│┌┐└┘ ── 
import tkinter as tk
import tic_tac_toe_utils as utils
main = tk.Tk()


print("WELCOME TO TIC TAK TOE\n")

print("Left Click For 'X' and Right Click For 'O'")


for row in range(3):
    row_buttons = []
    for col in range(3):
        
        button = tk.Button(main, bg="white", height=5, width=5, font=("Arial", 16))
        button.grid(row=row, column=col, padx=5, pady=5)
        row_buttons.append(button)

        button.bind("<Button-1>", utils.left_click) 
        button.bind("<Button-3>", utils.right_click)

    utils.grid_buttons.append(row_buttons) 


main.mainloop()
