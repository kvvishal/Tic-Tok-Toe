from tkinter import *
import random

def callback(row, column):

    global player

    if board[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            board[row][column].configure(text='X' ,fg='black', bg='red')

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            board[row][column].configure(text='O' , fg='orange', bg='blue')

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text']!="":
            board[row][0].config(bg="grey")
            board[row][1].config(bg="grey")
            board[row][2].config(bg="grey")
            return True

    for column in range(3):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != "":
            board[0][column].config(bg="grey")
            board[1][column].config(bg="grey")
            board[2][column].config(bg="grey")
            return True

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        board[0][0].config(bg="grey")
        board[1][1].config(bg="grey")
        board[2][2].config(bg="grey")
        return True

    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        board[0][2].config(bg="grey")
        board[1][1].config(bg="grey")
        board[2][0].config(bg="grey")
        return True
    else:
        return False

screen = Tk()
screen.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

frame = Frame(screen)
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="",font=('Comic Sans Ms',40), width=3, height=2 ,bg='cyan' ,
command= lambda row=row, column=column: callback(row,column))
        board[row][column].grid(row=row,column=column)

screen.mainloop()
