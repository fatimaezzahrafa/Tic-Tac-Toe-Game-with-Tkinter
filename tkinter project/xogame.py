from random import randint
from tkinter import *
root = Tk()
root.title("XO Game")
root.configure()
player_character = ""
ai_character = ""
positions = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
turn = 1
turns = 0
game_over = False


Grid.rowconfigure(root, 2, weight=2)
Grid.rowconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)
Grid.rowconfigure(root, 7, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)


def check_game_over(positions):
    global game_over
    if positions[0] + positions[1] + positions[2] == "xxx" or \
       positions[3] + positions[4] + positions[5] == "xxx" or \
       positions[6] + positions[7] + positions[8] == "xxx" or \
       positions[0] + positions[3] + positions[6] == "xxx" or \
       positions[1] + positions[4] + positions[7] == "xxx" or \
       positions[2] + positions[5] + positions[8] == "xxx" or \
       positions[0] + positions[4] + positions[8] == "xxx" or \
       positions[2] + positions[4] + positions[6] == "xxx":
       game_over = True
       win_label = Label(root, text="x wins", bg="green").grid(row=8, column=0, columnspan=3)
    elif positions[0] + positions[1] + positions[2] == "ooo" or \
       positions[3] + positions[4] + positions[5] == "ooo" or \
       positions[6] + positions[7] + positions[8] == "ooo" or \
       positions[0] + positions[3] + positions[6] == "ooo" or \
       positions[1] + positions[4] + positions[7] == "ooo" or \
       positions[2] + positions[5] + positions[8] == "ooo" or \
       positions[0] + positions[4] + positions[8] == "ooo" or \
       positions[2] + positions[4] + positions[6] == "ooo":
       game_over = True
       win_label = Label(root, text="o wins", bg="green").grid(row=8, column=0, columnspan=3)
    else:
        game_over = False
    return game_over
       


def ai_turn():
    global turn
    global turns
    global game_over
    while turn == 0 and turns < 9 and game_over == False:
        ai_select = randint(0, 8)
        if positions[ai_select] == "-":
            positions[ai_select] = ai_character
            if 0 <= ai_select <= 2:
               r = 5
            elif 3 <= ai_select <= 5:
               r = 6
            else:
               r = 7
            if ai_select == 0 or ai_select == 3 or ai_select == 6:
               c = 0
            elif ai_select == 1 or ai_select == 4 or ai_select ==7:
               c = 1
            else:
               c = 2
            new_button = Button(root, text=positions[ai_select]).grid(row=r, column=c)
            game_over = check_game_over(positions)
            turn = 1
            turns += 1


def x_select():
    global player_character
    global ai_character
    player_character = "x"
    ai_character = "o"
    player_label = Label(root, text="you have selected " +player_character).grid(row=3, column=0, columnspan=3)
    start_button = Button(root, text="Start!", command=draw_board).grid(row=4, column=0, columnspan=3)


def o_select():
    global player_character
    global ai_character
    player_character = "o"
    ai_character = "x"
    player_label = Label(root, text="you have selected " +player_character).grid(row=3, column=0, columnspan=3)
    start_button = Button(root, text="Start!", command=draw_board).grid(row=4, column=0, columnspan=3)


def player_pos(position):
    global turn
    global turns
    global game_over
    if 0 <= position <= 2:
        r = 5
    elif 3 <= position <= 5:
        r = 6
    else:
        r = 7
    if position == 0 or position == 3 or position == 6:
        c = 0
    elif position == 1 or position == 4 or position ==7:
        c = 1
    else:
        c = 2
    
    if turn == 1 and turns < 9 and game_over == False:
        if positions[position] == "-":
           positions[position] = player_character
           new_button = Button(root, text=positions[position]).grid(row=r, column=c)
           game_over = check_game_over(positions)
           turn = 0
           turns += 1
           ai_turn()

def draw_board():
    global positions
    global turn
    global turns
    global game_over
    turn = 1
    turns = 0
    game_over = False
    positions = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    top_left = Button(root, text=positions[0], command=lambda:player_pos(0)).grid(row=5, column=0, sticky="nesw")
    top_middle = Button(root, text=positions[1], command=lambda:player_pos(1)).grid(row=5, column=1, sticky="nesw") 
    top_right = Button(root, text=positions[2], command=lambda:player_pos(2)).grid(row=5, column=2, sticky="nesw") 
    middle_left = Button(root, text=positions[3], command=lambda:player_pos(3)).grid(row=6, column=0, sticky="nesw")
    middle_middle = Button(root, text=positions[4], command=lambda:player_pos(4)).grid(row=6, column=1, sticky="nesw")
    middle_right = Button(root, text=positions[5], command=lambda:player_pos(5)).grid(row=6, column=2, sticky="nesw")
    bottom_left = Button(root, text=positions[6], command=lambda:player_pos(6)).grid(row=7, column=0, sticky="nesw")
    bottom_middle = Button(root, text=positions[7], command=lambda:player_pos(7)).grid(row=7, column=1, sticky="nesw")
    bottom_right = Button(root, text=positions[8], command=lambda:player_pos(8)).grid(row=7, column=2, sticky="nesw")
    win_label = Label(root, text="          ").grid(row=8, column=0, columnspan=3)  
  
  
  
  
  
 
 



main_label = Label(root, text ="Welcome to Tic Tac Toe")
main_label.config()
player_select_label = Label(root, text="select a character to play as")
x_button = Button(root, text="x", command=x_select, background="yellow")
o_button = Button(root, text="o", command=o_select, background="aqua")




main_label.grid(row=0, column=0, columnspan=3)
player_select_label.grid(row=1, column=0, columnspan=3)
x_button.grid(row=2, column=0, sticky="ew")
o_button.grid(row=2, column=2, sticky="ew")
root.mainloop()
