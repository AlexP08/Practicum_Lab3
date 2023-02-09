from tkinter import *
from tkinter import messagebox

clicked = True
count = 0

root = Tk()
root.title("Крестики-нолики")


def reset():
    global but1, but2, but3, but4, but5, but6, but7, but8, but9
    global clicked, count
    clicked = True
    count = 0

    but1 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but1))
    but2 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but2))
    but3 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but3))

    but4 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but4))
    but5 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but5))
    but6 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but6))

    but7 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but7))
    but8 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but8))
    but9 = Button(root, text=" ", font=("Verdana", 24), height=3, width=6,
                  command=lambda: b_click(but9))

    # Размещение на экране
    but1.grid(row=0, column=0)
    but2.grid(row=0, column=1)
    but3.grid(row=0, column=2)

    but4.grid(row=1, column=0)
    but5.grid(row=1, column=1)
    but6.grid(row=1, column=2)

    but7.grid(row=2, column=0)
    but8.grid(row=2, column=1)
    but9.grid(row=2, column=2)


# Создание меню
game_menu = Menu(root)
root.config(menu=game_menu)

# Содержание меню для перезапуска игры
options_menu = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Параметры", menu=options_menu)
options_menu.add_command(label="Перезапуск игры", command=reset)


# Блокировка кнопок для окончания игры
def disable_all_buttons():
    but1.config(state=DISABLED)
    but2.config(state=DISABLED)
    but3.config(state=DISABLED)
    but4.config(state=DISABLED)
    but5.config(state=DISABLED)
    but6.config(state=DISABLED)
    but7.config(state=DISABLED)
    but8.config(state=DISABLED)
    but9.config(state=DISABLED)


# Проверка на выигрыш
def check_won():
    global winner, count
    global row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2
    winner = False

    row_1 = but1["text"] == but2["text"] == but3["text"] != " "
    row_2 = but4["text"] == but5["text"] == but6["text"] != " "
    row_3 = but7["text"] == but8["text"] == but9["text"] != " "
    column_1 = but1["text"] == but4["text"] == but7["text"] != " "
    column_2 = but2["text"] == but5["text"] == but8["text"] != " "
    column_3 = but3["text"] == but6["text"] == but9["text"] != " "
    diagonal_1 = but1["text"] == but5["text"] == but9["text"] != " "
    diagonal_2 = but3["text"] == but5["text"] == but7["text"] != " "

    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2:
        if row_1:
            but1.config(bg="green")
            but2.config(bg="green")
            but3.config(bg="green")
            winner = True
            if but1["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but1["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif row_2:
            but4.config(bg="green")
            but5.config(bg="green")
            but6.config(bg="green")
            winner = True
            if but4["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but4["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif row_3:
            but7.config(bg="green")
            but8.config(bg="green")
            but9.config(bg="green")
            winner = True
            if but7["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but7["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif column_1:
            but1.config(bg="green")
            but4.config(bg="green")
            but7.config(bg="green")
            if but1["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but1["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif column_2:
            but2.config(bg="green")
            but5.config(bg="green")
            but8.config(bg="green")
            winner = True
            if but2["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but2["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif column_3:
            but3.config(bg="green")
            but6.config(bg="green")
            but9.config(bg="green")
            winner = True
            if but3["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but3["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif diagonal_1:
            but1.config(bg="green")
            but5.config(bg="green")
            but9.config(bg="green")
            winner = True
            if but1["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but1["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()
        elif diagonal_2:
            but3.config(bg="green")
            but5.config(bg="green")
            but7.config(bg="green")
            winner = True
            if but3["text"] == "X":
                messagebox.showinfo("Есть победитель!", "Крестики победили!")
            elif but3["text"] == "0":
                messagebox.showinfo("Есть победитель!", "Нолики победили!")
            disable_all_buttons()

    elif count == 9 and winner == False:
        messagebox.showinfo("Сообщение", "Победитель не выявлен\nНичья!!!")
        disable_all_buttons()


# Что происходит по клику
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_won()
    elif b["text"] == " " and clicked == False:
        b["text"] = "0"
        clicked = True
        count += 1
        check_won()
    else:
        messagebox.showerror("Сообщение игроку", "Эта клетка уже занята\nВыберете другую клетку")


reset()

root.mainloop()
