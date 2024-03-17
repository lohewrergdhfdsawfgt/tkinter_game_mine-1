import tkinter as tk


from start_text import hello_text
from shop_run import def_shop
from mine_run import def_main
from prison_run import def_prison
from tavern_run import def_tavern
from lumber_mill_run import def_lumber_mill

def def_killer():
    button1.grid_remove()
    button2.grid_remove()
    button3.grid_remove()
    button4.grid_remove()


def start_loc():
    global button1, button2, button3, button4
    button1 = tk.Button(text='шахта', bg='pink', command=lambda: [def_killer(), def_main])
    button1.grid(column=0, row=1)
    button1.bind("<Button-1>", def_main)

    button2 = tk.Button(text='магазин', bg='pink', command=lambda: [def_killer(), def_shop])
    button2.grid(column=0, row=2)
    button2.bind("<Button-1>", def_shop)

    button3 = tk.Button(text='таверна', bg='pink', command=lambda: [def_killer(), def_tavern])
    button3.grid(column=0, row=3)
    button3.bind("<Button-1>", def_tavern)

    button4 = tk.Button(text='лесопилка', bg='pink', command=lambda: [def_killer(), def_lumber_mill])
    button4.grid(column=0, row=4)
    button4.bind("<Button-1>", def_lumber_mill)