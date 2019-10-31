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
    else:
        count_label['text'] = 'У вас {} очків, взяти ще?'.format(str(count))


def enough():
    global koloda, count
    if count == 21:
        results['text'] = 'Вітаємо з перемогою, у вас очко'
    else:
        results['text'] = 'Ви завершили гру з результатом  в {} очок'.format(count)


root = Tk()
root.geometry("300x140")

game_label = Label(root, text="Блекджек 4444", fg="red", bg="black")
game_label.place(x=100, y=0)
count_label = Label(root, text="У вас 0 очок")
count_label.place(x=110, y=30)
button1 = Button(root, width="15", text="Взяти карту", command=take)
button1.place(x=20, y=60)
button2 = Button(root, width="15", text="Хватить", command=enough)
button2.place(x=160, y=60)
results = Label(root, text="", fg="red")
results.place(x=50, y=100)
root.mainloop()
