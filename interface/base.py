from tkinter import Tk


class Tkinter(Tk):

    def center(self, width, height):
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        pos_x = screen_width / 2 - width / 2
        pos_y = screen_height / 2 - height / 2
        self.geometry("%dx%d+%d+%d" % (width, height, pos_x, pos_y))
