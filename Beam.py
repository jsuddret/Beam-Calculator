from tkinter import *
from pandas import DataFrame


class PositiveVerticalPointLoad:
    force = 0
    distance = 0

    def __init__(self, count):
        c = Canvas(window, height=100, width=51)
        c.pack(expand=1, fill=BOTH)
        c.place(x=925, y=50)
        c.create_line(27, 10, 27, 90, width=4)
        c.create_line(17, 30, 27, 11, width=4)
        c.create_line(37, 30, 27, 11, width=4)
        id_num = count
        c.bind('<Double-Button-1>', on_double_click_positive_point_load(id_num))
        c.bind(w, drag)

    def getForce(self):
        return self.force

    def setForce(self, F):
        self.force = F

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d


class NegativeVerticalPointLoad:
    force = 0
    distance = 0

    def __init__(self):
        c = Canvas(window, height=100, width=51)
        c.pack(expand=1, fill=BOTH)
        c.place(x=925, y=50)
        c.create_line(27, 10, 27, 95, width=4)
        c.create_line(17, 75, 27, 96, width=4)
        c.create_line(37, 75, 27, 96, width=4)
        c.bind(w, drag)

    def getForce(self):
        return self.force

    def setForce(self, F):
        self.force = F

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d


class PositivePointMomentLoad:
    magnitude = 0
    distance = 0

    def __init__(self):
        c = Canvas(window, height=100, width=51)
        c.pack(expand=1, fill=BOTH)
        c.place(x=925, y=50)
        c.create_arc(35, 90, 10, 20, start=-95, extent=180, width=4)
        c.create_line(21, 90, 24, 20, fill='SystemButtonFace', width=4)
        c.create_line(26, 20, 44, 34, width=4)
        c.create_line(26, 20, 22, 44, width=4)
        c.create_oval(20, 52, 25, 57, fill='black')
        c.bind(w, drag)

    def getForce(self):
        return self.magnitude

    def setForce(self, F):
        self.magnitude = F

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d


class NegativePointMomentLoad:
    magnitude = 0
    distance = 0

    def __init__(self):
        c = Canvas(window, height=100, width=51)
        c.pack(expand=1, fill=BOTH)
        c.place(x=925, y=50)
        c.create_arc(40, 90, 15, 20, start=95, extent=180, width=4)
        c.create_line(26, 21, 29, 95, fill='SystemButtonFace', width=4)
        c.create_line(25, 19, 28, 42, width=4)
        c.create_line(25, 19, 8, 30, width=4)
        c.create_oval(25, 52, 30, 57, fill='black')
        c.bind(w, drag)

    def getForce(self):
        return self.magnitude

    def setForce(self, F):
        self.magnitude = F

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d


def on_double_click_positive_point_load(identification_number):
    data_window = Tk()
    data_window.geometry('360x240+560+240')
    data_window.configure(bg='light grey')
    c = Canvas(data_window, height=240, width=360)
    c.pack()
    c.create_text(120, 60, text='Force: ')
    force_input = Entry(c, width=12)
    force_input.place(x=150, y=50)
    c.create_text(245, 60, text='N')
    c.create_text(127, 90, text='Distance: ')
    distance_input = Entry(c, width=12)
    distance_input.place(x=160, y=80)
    c.create_text(254, 90, text='m')
    enter_button = Button(c, text='Enter', command=lambda: enter_pressed(identification_number, force_input,
                                                                         distance_input))
    enter_button.place(x=180, y=125, anchor=CENTER)
    data_window.mainloop()


def drag(event):
    event.widget.place(x=event.x_root - 360, y=event.y_root - 110, anchor=CENTER)


def enter_pressed(identification_number, f_in, d_in):
    try:
        print(loads_list)
        loads_list[0][identification_number-1].setForce(f_in.get())
        loads_list[0][identification_number-1].setDistance(d_in.get())
    except ValueError:
        pass


def positive_vertical_point_load_pushed():
    global positive_vertical_point_count
    positive_vertical_point_count += 1
    pvpl = PositiveVerticalPointLoad(positive_vertical_point_count)
    positive_vertical_point_load_list.append(pvpl)


def negative_vertical_point_load_pushed():
    nvpl = NegativeVerticalPointLoad()
    negative_vertical_point_load_list.append(nvpl)


def positive_point_moment_pushed():
    ppml = PositivePointMomentLoad()
    positive_point_moment_list.append(ppml)


def negative_point_moment_pushed():
    npml = NegativePointMomentLoad()
    negative_point_moment_list.append(npml)


def calculate_pressed():
    print(loads_list[0][0].getForce())


window = Tk()
window.geometry('1220x720+360+90')
canvas = Canvas(window, bg='light grey', height=720, width=1220)
canvas.pack()
canvas.create_rectangle(120, 300, 810, 360, fill='black')
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
positive_vertical_point_load_list = []
positive_vertical_point_count = 0
negative_vertical_point_load_list = []
positive_point_moment_list = []
negative_point_moment_list = []
loads_list = [positive_vertical_point_load_list, negative_vertical_point_load_list,
              positive_point_moment_list, negative_point_moment_list]
positive_point_load_button = Button(window, bg='light grey', text='Point Load (+)', fg='black', width=15,
                                    command=positive_vertical_point_load_pushed).place(x=1070, y=50)
negative_point_load_button = Button(window, bg='light grey', text='Point Load (-)', fg='black', width=15,
                                    command=negative_vertical_point_load_pushed).place(x=1070, y=85)
positive_point_moment_button = Button(window, bg='light grey', text='Point Moment (+)', fg='black', width=15,
                                      command=positive_point_moment_pushed).place(x=1070, y=120)
negative_point_moment_button = Button(window, bg='light grey', text='Point Moment (-)', fg='black', width=15,
                                      command=negative_point_moment_pushed).place(x=1070, y=155)
calculate_button = Button(window, bg='light grey', text='Calculate', fg='black', width=15,
                          command=calculate_pressed).place(x=1070, y=190)
window.mainloop()
