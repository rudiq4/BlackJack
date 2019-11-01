from tkinter import *
from random import *

koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
shuffle(koloda)
count = 0
game_version = 0.1


def take():
    global count, koloda

    karta = koloda.pop()

    if karta == 'Валет' or karta == 'Дама' or karta == 'Король':
        karta = 10

    if karta == 'Туз':
        karta = 11

    count += karta

    if count > 21:
        results['text'] = 'Ви програли, набравши {} очок'.format(str(count))
        count_label['text'] = count
        button1.grid_forget()
        button2.grid_forget()
        button3.grid(row=2, column=0)
    else:
        count_label['text'] = 'У вас {} очків, взяти ще?'.format(str(count))


def enough():
    global koloda, count
    button1.grid_forget()
    button2.grid_forget()
    button3.grid(row=2, column=0)
    count_label.grid_forget()
    if count == 21:
        results['text'] = 'Вітаємо з перемогою, у вас очко'
    else:
        results['text'] = 'Ви завершили гру з результатом  в {} очок'.format(count)


def restart():
    global koloda, count
    count = 0
    shuffle(koloda)
    button1.grid(row=2, column=0)
    button2.grid(row=3, column=0)
    button3.grid_forget()
    results.grid_forget()


root = Tk()
root.title("The black-jack")
root.geometry("400x300")

game_label = Label(root, text="Блекджек 4444", font="ubuntu", fg="red", bg="black")
game_label.grid(row=0, columnspan=3)

count_label = Label(root, text="У вас 0 очок")
count_label.grid(row=1, column=0)

button1 = Button(root, width="15", font=("ubuntu", 30), text="Взяти карту", command=take)
button1.grid(row=2, column=0)
button2 = Button(root, width="15", font=("ubuntu", 30), text="Хватить", command=enough)
button2.grid(row=3, column=0)
button3 = Button(root, width="15", font=("ubuntu", 30), text="Спробувати ще", command=restart)

results = Label(root, text="", fg="red")
results.grid(row=4, column=0)
root.mainloop()
