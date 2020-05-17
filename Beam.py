from tkinter import *
from pandas import DataFrame


class PositiveVerticalPointLoad:
    force = 0
    distance = 0

    def __init__(self, stage):
        c = Canvas(stage, height=100, width=51)
        force_input = Entry(c, width=5, bg='light gray')
        force_input.place(x=2, y=65)
        distance_input = Entry(c, width=3, bg='light gray')
        distance_input.place(x=16, y=85)
        c.pack(expand=1, fill=BOTH)
        c.place(x=950, y=50)
        c.create_line(27, 10, 27, 60, width=4)
        c.create_line(17, 30, 27, 11, width=4)
        c.create_line(37, 30, 27, 11, width=4)
        c.create_text(45, 76, text='N')
        c.create_text(8, 95, text='@')
        c.create_text(45, 95, text='m')
        c.bind(w, drag)

    def getForce(self):
        self.force = force_input.get()
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
        force_input = Entry(c, width=5, bg='light gray')
        force_input.place(x=2, y=3)
        distance_input = Entry(c, width=3, bg='light gray')
        distance_input.place(x=16, y=22)
        c.pack(expand=1, fill=BOTH)
        c.place(x=950, y=50)
        c.create_line(27, 45, 27, 95, width=4)
        c.create_line(17, 75, 27, 96, width=4)
        c.create_line(37, 75, 27, 96, width=4)
        c.create_text(45, 10, text='N')
        c.create_text(8, 30, text='@')
        c.create_text(45, 30, text='m')
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
        magnitude_input = Entry(c, width=3, bg='light gray')
        magnitude_input.place(x=2, y=65)
        distance_input = Entry(c, width=3, bg='light gray')
        distance_input.place(x=16, y=85)
        c.pack(expand=1, fill=BOTH)
        c.place(x=950, y=50)
        c.create_arc(35, 60, 10, 15, start=-65, extent=180, width=4)
        c.create_line(28, 59, 17, 17, fill='SystemButtonFace', width=4)
        c.create_line(13, 16, 28, 28, width=4)
        c.create_line(13, 17, 28, 6, width=4)
        c.create_oval(20, 35, 25, 40, fill='black')
        c.create_text(40, 76, text='N*m')
        c.create_text(8, 95, text='@')
        c.create_text(45, 95, text='m')
        c.bind(w, drag)

    def getMagnitude(self):
        return self.magnitude

    def setMagnitude(self, m):
        self.magnitude = m

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d


class NegativePointMomentLoad:
    magnitude = 0
    distance = 0

    def __init__(self):
        c = Canvas(window, height=100, width=51)
        magnitude_input = Entry(c, width=3, bg='light gray')
        magnitude_input.place(x=2, y=65)
        distance_input = Entry(c, width=3, bg='light gray')
        distance_input.place(x=16, y=85)
        c.pack(expand=1, fill=BOTH)
        c.place(x=950, y=50)
        c.create_arc(10, 15, 35, 60, start=65, extent=180, width=4)
        c.create_line(28, 17, 17, 59, fill='SystemButtonFace', width=4)
        c.create_line(28, 16, 17, 28, width=4)
        c.create_line(28, 17, 17, 6, width=4)
        c.create_oval(20, 35, 25, 40, fill='black')
        c.create_text(40, 76, text='N*m')
        c.create_text(8, 95, text='@')
        c.create_text(45, 95, text='m')
        c.bind(w, drag)

    def getMagnitude(self):
        return self.magnitude

    def setMagnitude(self, m):
        self.magnitude = m

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d


def drag(event):
    event.widget.place(x=event.x_root - 360, y=event.y_root - 110, anchor=CENTER)


def positive_vertical_point_load_pushed():
    pvpl = PositiveVerticalPointLoad(window)
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
negative_vertical_point_load_list = []
positive_point_moment_list = []
negative_point_moment_list = []
loads_list = [positive_vertical_point_load_list, negative_vertical_point_load_list,
              positive_point_moment_list, negative_point_moment_list]
positive_point_load_button = Button(window, bg='light gray', text='Point Load (+)', fg='black', width=15,
                                    command=positive_vertical_point_load_pushed).place(x=1070, y=50)
negative_point_load_button = Button(window, bg='light gray', text='Point Load (-)', fg='black', width=15,
                                    command=negative_vertical_point_load_pushed).place(x=1070, y=85)
positive_point_moment_button = Button(window, bg='light gray', text='Point Moment (+)', fg='black', width=15,
                                      command=positive_point_moment_pushed).place(x=1070, y=120)
negative_point_moment_button = Button(window, bg='light gray', text='Point Moment (-)', fg='black', width=15,
                                      command=negative_point_moment_pushed).place(x=1070, y=155)
calculate_button = Button(window, bg='light gray', text='Calculate', fg='black', width=15,
                          command=calculate_pressed).place(x=1070, y=190)
window.mainloop()
