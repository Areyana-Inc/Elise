import tkinter
from tkinter.scrolledtext import ScrolledText
from Elise.utils import TITLE, GEOMETRY


class Elise(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.menu = None
        self.file_menu = None

        self.regex_entry = None
        self.regex_error_text = None
        self.regex_check_error_text = None
        self.regex_check_text = None

        self.regex_entry_string = tkinter.StringVar()
        self.regex_check_string = tkinter.StringVar()

        self.title(TITLE)
        self.geometry(GEOMETRY)

        self.init_GUI()

    def init_GUI(self):

        self.init_menu()

        self.regex_entry_string.trace_add('write', self.regex_entry_callback)
        self.regex_entry = tkinter.Entry(textvariable=self.regex_entry_string)
        self.regex_entry.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)

        self.regex_error_text = tkinter.Label()
        self.regex_error_text.config(text='test')
        self.regex_error_text.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)

        self.regex_check_text = ScrolledText(width=40)
        self.regex_check_text.insert(tkinter.INSERT, 'Place text here ...')
        self.regex_check_text.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5)

        self.regex_check_error_text = tkinter.Label(text='Text check here')
        self.regex_check_error_text.grid(row=1, column=1)

        self.config(menu=self.menu)

    def init_menu(self):
        self.init_file_menu()

        self.menu = tkinter.Menu()
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.menu.add_cascade(label='Edit')
        self.menu.add_cascade(label='View')

    def init_file_menu(self):
        self.file_menu = tkinter.Menu()
        self.file_menu.add_command(label='New')
        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Open')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit')

    def regex_entry_callback(self, *args, **kwargs):
        pass

    def exit_command(self):
        pass

    def new_command(self):
        pass

    def open_command(self):
        pass


def main():
    elise = Elise()
    elise.mainloop()


if __name__ == '__main__':
    main()
