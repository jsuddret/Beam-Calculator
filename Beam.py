from tkinter import *
from pandas import DataFrame


class PositiveVerticalPointLoad:

    def __init__(self):

        def enter_pressed():
            try:
                y_force_list.append(float(force_input.get()))
                y_force_distance_list.append(float(distance_input.get()))
                data_window.destroy()
            except ValueError:
                pass

        c = Canvas(window, height=90, width=9, bg='light grey', highlightthickness=0)
        c.pack(expand=1, fill=BOTH)
        c.place(x=910, y=125, anchor=CENTER)
        c.create_line(4, 90, 4, 0, fill='black', arrow=LAST, width=3)
        c.bind(w, drag)
        data_window = Tk()
        data_window.geometry('360x240')
        data_window.configure(bg='light grey')
        force_input_label = Label(data_window, text='Force:\t\t\tN', bg='light grey')
        force_input_label.place(x=155, y=60, anchor=CENTER)
        force_input = Entry(data_window, width=10)
        force_input.place(x=180, y=60, anchor=CENTER)
        distance_input_label = Label(data_window, text='Distance:\t\tm', bg='light grey')
        distance_input_label.place(x=156, y=90, anchor=CENTER)
        distance_input = Entry(data_window, width=10)
        distance_input.place(x=180, y=90, anchor=CENTER)
        enter_button = Button(data_window, text='Enter', bg='light grey', command=enter_pressed)
        enter_button.place(x=180, y=125, anchor=CENTER)
        data_window.mainloop()


class NegativeVerticalPointLoad:

    def __init__(self):
        def enter_pressed():
            try:
                y_force_list.append(int(force_input.get()) * -1)
                y_force_distance_list.append(int(distance_input.get()))
                data_window.destroy()
            except ValueError:
                pass

        c = Canvas(window, height=90, width=9, bg='light grey', highlightthickness=0)
        c.pack(expand=1, fill=BOTH)
        c.place(x=912, y=125, anchor=CENTER)
        c.create_line(4, 0, 4, 90, fill='black', arrow=LAST, width=3)
        c.bind(w, drag)
        data_window = Tk()
        data_window.geometry('360x240')
        data_window.configure(bg='light grey')
        force_input_label = Label(data_window, text='Force:\t\t\tN', bg='light grey')
        force_input_label.place(x=155, y=60, anchor=CENTER)
        force_input = Entry(data_window, width=10)
        force_input.place(x=180, y=60, anchor=CENTER)
        distance_input_label = Label(data_window, text='Distance:\t\tm', bg='light grey')
        distance_input_label.place(x=156, y=90, anchor=CENTER)
        distance_input = Entry(data_window, width=10)
        distance_input.place(x=180, y=90, anchor=CENTER)
        enter_button = Button(data_window, text='Enter', bg='light grey', command=enter_pressed)
        enter_button.place(x=180, y=125, anchor=CENTER)
        data_window.mainloop()


class PositivePointMomentLoad:

    def __init__(self):
        def enter_pressed():
            try:
                moment_list.append(int(force_input.get()))
                moment_distance_list.append(int(distance_input.get()))
                data_window.destroy()
            except ValueError:
                pass

        c = Canvas(window, height=45, width=45, bg='light grey', highlightthickness=0)
        c.pack(expand=1, fill=BOTH)
        c.place(x=912, y=125, anchor=CENTER)
        c.create_oval(5, 5, 40, 40, width=3)
        c.create_line(5, 30, 5, 31, fill='black', arrow=LAST, width=3)
        c.bind(w, drag)
        data_window = Tk()
        data_window.geometry('360x240')
        data_window.configure(bg='light grey')
        force_input_label = Label(data_window, text='Magnitude:\t\t\tN', bg='light grey')
        force_input_label.place(x=155, y=60, anchor=CENTER)
        force_input = Entry(data_window, width=10)
        force_input.place(x=180, y=60, anchor=CENTER)
        distance_input_label = Label(data_window, text='Distance:\t\tm', bg='light grey')
        distance_input_label.place(x=156, y=90, anchor=CENTER)
        distance_input = Entry(data_window, width=10)
        distance_input.place(x=180, y=90, anchor=CENTER)
        enter_button = Button(data_window, text='Enter', bg='light grey', command=enter_pressed)
        enter_button.place(x=180, y=125, anchor=CENTER)
        data_window.mainloop()


class NegativePointMomentLoad:

    def __init__(self):
        def enter_pressed():
            try:
                moment_list.append(int(force_input.get()) * -1)
                moment_distance_list.append(int(distance_input.get()))
                data_window.destroy()
            except ValueError:
                pass

        c = Canvas(window, height=45, width=45, bg='light grey', highlightthickness=0)
        c.pack(expand=1, fill=BOTH)
        c.place(x=912, y=125, anchor=CENTER)
        c.create_oval(5, 5, 40, 40, width=3)
        c.create_line(5, 19, 5, 18, fill='black', arrow=LAST, width=3)
        c.bind(w, drag)
        data_window = Tk()
        data_window.geometry('360x240')
        data_window.configure(bg='light grey')
        force_input_label = Label(data_window, text='Magnitude:\t\t\tN', bg='light grey')
        force_input_label.place(x=155, y=60, anchor=CENTER)
        force_input = Entry(data_window, width=10)
        force_input.place(x=180, y=60, anchor=CENTER)
        distance_input_label = Label(data_window, text='Distance:\t\tm', bg='light grey')
        distance_input_label.place(x=156, y=90, anchor=CENTER)
        distance_input = Entry(data_window, width=10)
        distance_input.place(x=180, y=90, anchor=CENTER)
        enter_button = Button(data_window, text='Enter', bg='light grey', command=enter_pressed)
        enter_button.place(x=180, y=125, anchor=CENTER)
        data_window.mainloop()


def drag(event):
    event.widget.place(x=event.x_root - 360, y=event.y_root - 110, anchor=CENTER)


def positive_vertical_point_load_pushed():
    PositiveVerticalPointLoad()


def negative_vertical_point_load_pushed():
    NegativeVerticalPointLoad()


def positive_point_moment_pushed():
    PositivePointMomentLoad()


def negative_point_moment_pushed():
    NegativePointMomentLoad()


def calculate_pressed():
    global length
    try:
        length = length_input.get()
    except ValueError:
        pass
    print(force_list)


window = Tk()
window.geometry('1220x720+360+90')
canvas = Canvas(window, bg='light grey', height=720, width=1220)
canvas.pack()
canvas.create_rectangle(120, 300, 810, 360, fill='black')
canvas.create_rectangle(122, 302, 808, 358, fill='light blue')
canvas.create_rectangle(122, 302, 808, 312, fill='light gray')
canvas.create_rectangle(122, 348, 808, 358, fill='light gray')
canvas.create_rectangle(122, 312, 808, 313, fill='black')
canvas.create_rectangle(122, 347, 808, 348, fill='black')
canvas.create_line(120, 120, 120, 295, width=3)
canvas.create_line(810, 120, 810, 295, width=3)
canvas.create_line(120, 140, 810, 140, width=3)
canvas.create_text(415, 130, text='L = ')
canvas.create_text(500, 130, text='m')
canvas.create_line(155, 135, 160, 140, width=3)
canvas.create_line(155, 145, 160, 140, width=3)
canvas.create_text(140, 130, text='X')
length_input = Entry(window, bg='light grey', width=10)
length_input.place(x=425, y=120)
length = 0
w = "<B1-Motion>"
x_force_list = []
y_force_list = []
x_force_distance_list = []
y_force_distance_list = []
moment_list = []
moment_distance_list = []
positive_point_load_button = Button(window, bg='light grey', text='Vertical Point Load (+)', fg='black', width=20,
                                    command=positive_vertical_point_load_pushed).place(x=1000, y=50)
negative_point_load_button = Button(window, bg='light grey', text='Vertical Point Load (-)', fg='black', width=20,
                                    command=negative_vertical_point_load_pushed).place(x=1000, y=85)
positive_point_moment_button = Button(window, bg='light grey', text='Point Moment (+)', fg='black', width=20,
                                      command=positive_point_moment_pushed).place(x=1000, y=120)
negative_point_moment_button = Button(window, bg='light grey', text='Point Moment (-)', fg='black', width=20,
                                      command=negative_point_moment_pushed).place(x=1000, y=155)
calculate_button = Button(window, bg='light grey', text='Calculate', fg='black', width=20,
                          command=calculate_pressed).place(x=1000, y=190)
window.mainloop()
