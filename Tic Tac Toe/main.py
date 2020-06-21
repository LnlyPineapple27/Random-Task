from tkinter import * # using "import tkinter" will bring up some errors
import pygame
import random
from PIL import ImageTk, Image
import PIL.Image
from tkinter import font as tkfont
from tkinter import messagebox
from pygame import mixer


class Window():
    def __init__(self, master):
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Tic Tac Toe")
        self.master.geometry("800x560") # set size of game window
        self.master.iconbitmap('logo.ico') # choose logo of game window
        self.master.resizable(0, 0)
        self.add_menu()
        self.showBackground()

    def add_menu(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.select1 = Menu(self.menu)
        self.menu.add_cascade(label='Options', menu=self.select1)
        self.select1.add_command(label='Credits', command=self.ShowCredit)
        self.select1.add_command(label='Exit', command=self.quit)

    def showBackground(self):
        self.canvas = Canvas(self.master, width=200, height=200)
        self.canvas.pack(fill=BOTH, expand=1)
        self.img = ImageTk.PhotoImage(PIL.Image.open("ok3.png"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.pvp_button = Button(self.master, text="Player vs Player",
                                 font=tkfont.Font(family="Comic Sans MS", size="13"),
                                 command=self.gotoPvP, width=23, height=1, bg="light pink")
        self.pvc_button = Button(self.master, text="Player vs Computer",
                                 font=tkfont.Font(family="Comic Sans MS", size="13"),
                                 command=self.gotoPvC, width=23, height=1, bg="light pink")
        self.load_PVP_button = Button(self.master, text="Continue PvP Match",
                                      font=tkfont.Font(family="Comic Sans MS", size="13"),
                                      command=self.LoadPvP, width=23, height=1, bg="light pink")
        self.load_PVC_button = Button(self.master, text="Continue PvC  Match",
                                      font=tkfont.Font(family="Comic Sans MS", size="13"),
                                      command=self.LoadPvC, width=23, height=1, bg="light pink")
        self.quit_button = Button(self.master, text="Quit", font=tkfont.Font(family="Comic Sans MS", size="13"),
                                  command=self.quit, width=23, height=1, bg="light pink")

        pvp_button_window = self.canvas.create_window(275, 250, anchor='nw', window=self.pvp_button)
        pvc_button_window = self.canvas.create_window(295, 295, anchor='nw', window=self.pvc_button)
        load_pvp_button_window = self.canvas.create_window(275, 340, anchor='nw', window=self.load_PVP_button)
        load_pvc_button_window = self.canvas.create_window(295, 385, anchor='nw', window=self.load_PVC_button)
        quit_button_window = self.canvas.create_window(275, 430, anchor='nw', window=self.quit_button)

    def quit(self):
        # global root
        self.master.destroy()

    def gotoPvP(self):
        root2 = Toplevel(self.master)
        myGUI = GAME(root2, False, 1)

    def LoadPvP(self):
        root2 = Toplevel(self.master)
        myGUI = GAME(root2, True, 1)

    def gotoPvC(self):
        root3 = Toplevel(self.master)
        myGUI = GAME(root3, False, 2)

    def LoadPvC(self):
        root3 = Toplevel(self.master)
        myGUI = GAME(root3, True, 2)

    def ShowCredit(self):
        root4 = Toplevel(self.master)
        myGUI = CREDIT(root4)

class GAME():
    def __init__(self, master, CheckLoad, Kind):
        Colums = 15
        Rows = 15
        NameP1 = "Player 1"
        NameP2 = "Player 2"
        IconP1 = "X"
        IconP2 = "O"
        Rule = 1
        ColorBGP1 = "Yellow"
        ColorBGP2 = "Cyan"
        BroadColor = "Khaki"

        self.Kind = Kind
        self.checkLoad = CheckLoad
        self.master = master
        self.master.title("Game")
        self.master.geometry("1000x700")
        self.master.iconbitmap('logo.ico')

        if self.Kind == 3:
            self.Settings(Colums, Rows, Rule, NameP1, NameP2, IconP1, IconP2, ColorBGP1, ColorBGP2, BroadColor)

        if self.Kind == 1:
            self.PvP(Colums, Rows, Rule, NameP1, NameP2, IconP1, IconP2, ColorBGP1, ColorBGP2, BroadColor)
        elif self.Kind == 2:
            self.PvC(Colums, Rows, Rule, NameP1, NameP2, IconP1, IconP2, ColorBGP1, ColorBGP2, BroadColor)

    def quit(self):
        self.master.destroy()

    def Settings(self):

        self.master.geometry("905x615")
        self.master.config(bg="pink")

    def AskSave(self):
        result = messagebox.askyesno("Python", "Would you like to save the data?")
        if result == True:
            messagebox.showinfo("Anouncement", "Save successfully!")
            self.master.destroy()
        else:
            messagebox.showinfo("Anouncement", "This match is not saved!")
            self.master.destroy()

    def add_menu(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.select1 = Menu(self.menu)
        self.menu.add_cascade(label='Options', menu=self.select1)
        self.select1.add_command(label='Save game', command=self.quit)
        self.select1.add_separator()
        self.select1.add_command(label='Exit', command=self.quit)

    def Clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def PvP(self, Colums, Rows, Rule, NameP1, NameP2, IconP1, IconP2, ColorBGP1, ColorBGP2, BroadColor):

        self.master.geometry("905x615")
        self.master.config(bg="pink")

        self.Clear()
        self.add_menu()

        Button(self.master, text=NameP1, height=1, width=13, disabledforeground="purple",
               state=DISABLED, font=('Times', 16)).place(x=45 * Colums + 17, y=30)
        Button(self.master, text=IconP1, height=1, width=4, disabledforeground="red", font=('Brush Script MT', 62),
               state=DISABLED, bg=ColorBGP1).place(x=45 * Colums + 18, y=70)
        Button(self.master, text=NameP2, height=1, width=13, disabledforeground="purple",
               state=DISABLED, font=('Times', 16)).place(x=45 * Colums + 17, y=280)
        Button(self.master, text=IconP2, height=1, width=4, disabledforeground="green", font=('Brush Script MT', 62),
               state=DISABLED).place(x=45 * Colums + 18, y=320)

        Button(self.master, text="Quit Game", height=1, width=10, command=self.AskSave, fg="Red",
               font=('Times', 22)).place(x=45 * Colums + 17, y=520)

        self.turn = 1
        self.button_table = [[0 for i in range(Colums)] for i in range(Rows)]
        self.matrix_table = [[0 for i in range(Colums)] for i in range(Rows)]

        def write_XO(x, y):
            if self.turn % 2 != 0:
                self.button_table[x][y].config(text=IconP1, disabledforeground="red", state=DISABLED, bg=ColorBGP1)
                self.matrix_table[x][y] = 1
                #play_click_sound()  # play sound
                Button(self.master, text=IconP2, height=1, width=4, disabledforeground="green", bg=ColorBGP2,
                       font=('Brush Script MT', 62), state=DISABLED).place(x=45 * Colums + 18, y=320)
                Button(self.master, text="X", height=1, width=4, disabledforeground="black",
                       font=('Brush Script MT', 62), state=DISABLED, bg="white").place(x=45 * Colums + 18, y=70)

                if is_win(x, y) == 1:
                    messagebox.showinfo("Match END", NameP1 + "-" + IconP1 + " WIN")
                    self.master.destroy()
            else:
                self.button_table[x][y].config(text=IconP2, disabledforeground="green", state=DISABLED, bg=ColorBGP2)
                self.matrix_table[x][y] = 2
                #play_click_sound()  # play sound
                Button(self.master, text=IconP1, height=1, width=4, disabledforeground="red",
                       font=('Brush Script MT', 62),
                       state=DISABLED, bg=ColorBGP1).place(x=45 * Colums + 18, y=70)
                Button(self.master, text=IconP2, height=1, width=4, disabledforeground="black",
                       font=('Brush Script MT', 62),
                       state=DISABLED).place(x=45 * Colums + 18, y=320)
                if is_win(x, y) == 2:
                    messagebox.showinfo("Match END", NameP2 + "-" + IconP2 + " WIN")
                    self.master.destroy()
            if is_win(x, y) == 3:
                messagebox.showinfo("Match END", "No player win, DRAW Match")

            save_game = open("SavePvP.txt", "w")
            for i in range(Colums):
                for j in range(Rows):
                    save_game.write('%d' % self.matrix_table[i][j])
            save_game.close()

            self.turn += 1

        for i in range(Colums):
            for j in range(Rows):
                self.button_table[i][j] = Button(self.master, text=" ", width=5, heigh=2, bg=BroadColor,
                                                 command=lambda t=i, k=j: write_XO(t, k))
                self.button_table[i][j].grid(row=i, column=j)

        if self.checkLoad == True:
            file = open("SavePvP.txt", "r")
            for i in range(Colums):
                for j in range(Rows):
                    x = file.read(1)
                    if x == '1':
                        self.matrix_table[i][j] = int(1)
                    elif x == '2':
                        self.matrix_table[i][j] = int(2)
            file.close()

            for i in range(Colums):
                for j in range(Rows):
                    if self.matrix_table[i][j] == 1:
                        self.button_table[i][j].config(text=IconP1, disabledforeground="red", state=DISABLED,
                                                       bg=ColorBGP1)
                        self.turn = self.turn + 1
                    elif self.matrix_table[i][j] == 2:
                        self.button_table[i][j].config(text=IconP2, disabledforeground="green", state=DISABLED,
                                                       bg=ColorBGP2)
                        self.turn = self.turn + 1

        def is_win(x, y):
            print(x, y)
            # check Draw

            if self.turn == Rows * Colums:
                return 3
            if self.turn % 2 == 0:
                winner = 2
                loser = 1
            else:
                winner = 1
                loser = 2

            # Check Rows
            for i in range(0, Colums):
                count = 0
                if self.matrix_table[i][y] == winner and winner != 0:
                    for j in range(i, Colums):
                        if self.matrix_table[j][y] == winner and count < 5:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if j + 1 >= Colums or j - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[j + 1][y] != loser or self.matrix_table[j - 5][y] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break

            # check Cols
            for i in range(0, Rows):
                count = 0
                if self.matrix_table[x][i] == winner and winner != 0:
                    for j in range(i, Rows):
                        if self.matrix_table[x][j] == winner and count < 5:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if j + 1 >= Rows or j - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[x][j + 1] != loser or self.matrix_table[x][j - 5] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break

            # check /
            dx = x
            dy = y
            while dx > 0 and dy < Rows - 1:
                dx -= 1
                dy += 1
            while dx < Colums and dy >= 0:
                if self.matrix_table[dx][dy] == winner:
                    count = 0
                    while dx < Colums and dy >= 0:
                        if self.matrix_table[dx][dy] == winner:
                            count += 1
                            if count == 5:
                                print("ok")
                                if Rule == 1:
                                    return winner
                                else:
                                    if dy - 1 < 0 or dx + 1 >= Colums or dy + 5 >= Rows or dx - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[dx + 1][dy - 1] != loser or self.matrix_table[dx - 5][
                                                dy + 5] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break
                        dx += 1
                        dy -= 1
                dx += 1
                dy -= 1

            # check \
            dx = x
            dy = y
            while dx > 0 and dy > 0:
                dx -= 1
                dy -= 1
            while dx < Colums and dy < Rows:
                if self.matrix_table[dx][dy] == winner:
                    count = 0
                    while dx < Colums and dy < Rows:
                        if self.matrix_table[dx][dy] == winner:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if dx + 1 >= Colums or dy + 1 >= Rows or dx - 5 < 0 or dy - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[dx + 1][dy + 1] != loser or self.matrix_table[dx - 5][
                                                dy - 5] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break
                        dx += 1
                        dy += 1

                dx += 1
                dy += 1

        return 0

    def PvC(self, Colums, Rows, Rule, NameP1, NameP2, IconP1, IconP2, ColorBGP1, ColorBGP2, BroadColor):
        self.Clear()
        self.add_menu()

        self.master.geometry("905x615")
        self.master.config(bg="pink")

        self.Clear()
        self.add_menu()

        Button(self.master, text=NameP1, height=1, width=13, disabledforeground="purple",
               state=DISABLED, font=('Times', 16)).place(x=45 * Colums + 17, y=30)
        A = Button(self.master, text=IconP1, height=1, width=4, disabledforeground="black",
                   font=('Brush Script MT', 62),
                   state=DISABLED, bg="white").place(x=45 * Colums + 18, y=70)
        Button(self.master, text=NameP2, height=1, width=13, disabledforeground="purple",
               state=DISABLED, font=('Times', 16)).place(x=45 * Colums + 17, y=280)
        B = Button(self.master, text=IconP2, height=1, width=4, disabledforeground="green",
                   font=('Brush Script MT', 62),
                   state=DISABLED).place(x=45 * Colums + 18, y=320)

        Button(self.master, text="Quit Game", height=1, width=10, command=self.AskSave, fg="Red",
               font=('Times', 22)).place(x=45 * Colums + 17, y=520)

        self.turn = 1
        self.button_table = [[0 for i in range(Colums)] for i in range(Rows)]
        self.matrix_table = [[0 for i in range(Colums)] for i in range(Rows)]

        self.pre_XY = [0, 0]
        self.X_max_pts = 0

        def write_XO(x, y):
            self.button_table[x][y].config(text=IconP1, disabledforeground="red", state=DISABLED, bg=ColorBGP1)
            self.matrix_table[x][y] = 1
            Button(self.master, text=IconP2, height=1, width=4, disabledforeground="green", bg=ColorBGP2,
                   font=('Brush Script MT', 62), state=DISABLED).place(x=45 * Colums + 18, y=320)
            Button(self.master, text="X", height=1, width=4, disabledforeground="black",
                   font=('Brush Script MT', 62), state=DISABLED, bg="white").place(x=45 * Colums + 18, y=70)
            #play_click_sound()

            if is_win(x, y) == 1:
                messagebox.showinfo("Match END", NameP1 + "-" + IconP1 + " WIN")
            if is_win(x, y) == 3:
                messagebox.showinfo("Match END", "No player win, DRAW Match")

            save_game = open("SavePvC.txt", "w")
            for i in range(Colums):
                for j in range(Rows):
                    save_game.write('%d' % self.matrix_table[i][j])
            save_game.close()

            self.turn += 1
            computer(x, y)
            if is_win(x, y) == 2:
                messagebox.showinfo("Match END", NameP2 + "-" + IconP2, " WIN")
            if is_win(x, y) == 3:
                messagebox.showinfo("Match END", "No player win, DRAW Match")

            save_game = open("SavePvC.txt", "w")
            for i in range(Colums):
                for j in range(Rows):
                    save_game.write('%d' % self.matrix_table[i][j])
            save_game.close()

            self.turn += 1

        for i in range(Colums):
            for j in range(Rows):
                self.button_table[i][j] = Button(self.master, text=" ", width=5, heigh=2, bg=BroadColor,
                                                 command=lambda t=i, k=j: write_XO(t, k))
                self.button_table[i][j].grid(row=i, column=j)

        if self.checkLoad == True:
            file = open("SavePvC.txt", "r")
            for i in range(Colums):
                for j in range(Rows):
                    x = file.read(1)
                    if x == '1':
                        self.matrix_table[i][j] = int(1)
                    elif x == '2':
                        self.matrix_table[i][j] = int(2)
            file.close()

            for i in range(Colums):
                for j in range(Rows):
                    if self.matrix_table[i][j] == 1:
                        self.button_table[i][j].config(text=IconP1, disabledforeground="red", state=DISABLED,
                                                       bg=ColorBGP1)
                        self.turn = self.turn + 1
                    elif self.matrix_table[i][j] == 2:
                        self.button_table[i][j].config(text=IconP2, disabledforeground="green", state=DISABLED,
                                                       bg=ColorBGP2)
                        self.turn = self.turn + 1

        def computer(x, y):
            C_x = random.randint(0, Colums - 1)
            C_y = random.randint(0, Rows - 1)
            while self.matrix_table[C_x][C_y] != 0:
                C_x = random.randint(0, Colums - 1)
                C_y = random.randint(0, Rows - 1)
            self.button_table[C_x][C_y].config(text=IconP2, disabledforeground="green", state=DISABLED, bg=ColorBGP2)
            self.matrix_table[C_x][C_y] = 2
            Button(self.master, text=IconP1, height=1, width=4, disabledforeground="red",
                   font=('Brush Script MT', 62),
                   state=DISABLED, bg=ColorBGP1).place(x=45 * Colums + 18, y=70)
            Button(self.master, text=IconP2, height=1, width=4, disabledforeground="black",
                   font=('Brush Script MT', 62),
                   state=DISABLED).place(x=45 * Colums + 18, y=320)

        def is_win(x, y):
            # check Draw

            if self.turn == Rows * Colums:
                return 3

            if self.turn % 2 == 0:
                winner = 2
                loser = 1
            else:
                winner = 1
                loser = 2

            # Check Rows
            for i in range(0, Colums):
                count = 0
                if self.matrix_table[i][y] == winner and winner != 0:
                    for j in range(i, Colums):
                        if self.matrix_table[j][y] == winner and count < 5:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if j + 1 >= Colums or j - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[j + 1][y] != loser or self.matrix_table[j - 5][y] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break

            # check Cols
            for i in range(0, Rows):
                count = 0
                if self.matrix_table[x][i] == winner and winner != 0:
                    for j in range(i, Rows):
                        if self.matrix_table[x][j] == winner and count < 5:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if j + 1 >= Rows or j - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[x][j + 1] != loser or self.matrix_table[x][j - 5] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break

            # check /
            dx = x
            dy = y
            while dx > 0 and dy < Rows - 1:
                dx -= 1
                dy += 1
            while dx < Colums and dy >= 0:
                if self.matrix_table[dx][dy] == winner:
                    count = 0
                    while dx < Colums and dy >= 0:
                        if self.matrix_table[dx][dy] == winner:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if dy - 1 < 0 or dx + 1 >= Colums or dy + 5 >= Rows or dx - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[dx + 1][dy - 1] != loser or self.matrix_table[dx - 5][
                                                dy + 5] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break
                        dx += 1
                        dy -= 1
                dx += 1
                dy -= 1

            # check \
            dx = x
            dy = y
            while dx > 0 and dy > 0:
                dx -= 1
                dy -= 1
            while dx < Colums and dy < Rows:
                if self.matrix_table[dx][dy] == winner:
                    count = 0
                    while dx < Colums and dy < Rows:
                        if self.matrix_table[dx][dy] == winner:
                            count += 1
                            if count == 5:
                                if Rule == 1:
                                    return winner
                                else:
                                    if dx + 1 >= Colums or dy + 1 >= Rows or dx - 5 < 0 or dy - 5 < 0:
                                        return winner
                                    else:
                                        if self.matrix_table[dx + 1][dy + 1] != loser or self.matrix_table[dx - 5][
                                                dy - 5] != loser:
                                            return winner
                                        else:
                                            break
                        else:
                            break
                        dx += 1
                        dy += 1

                dx += 1
                dy += 1

        return 0


# ========================================================================

# mainloop
def main():
    #play_bgmusic()
    root = Tk()
    # root.geometry("800x600")
    startGUI = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
