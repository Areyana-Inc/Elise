import tkinter
from Elise.utils import TITLE, GEOMETRY


class Elise(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(TITLE)
        self.root.geometry(GEOMETRY)



def main():
    elise = Elise()
    elise.root.mainloop()


if __name__ == '__main__':
    main()
