import tkinter
import webbrowser
import re
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror
from Elise.utils import TITLE, GEOMETRY
from Elise.tooltip import ToolTip


class HighlightText(ScrolledText):
    """ A text widget with a new method, highlight_pattern()

    example:

    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    """

    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)
        self.match_count = 0
        self.index_list = list()

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        """Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        """

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tkinter.IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings
            self.match_count += 1
            self.index_list.append(index)
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

    def clear_highlight(self, tag):
        self.match_count = 0
        self.index_list.clear()
        self.tag_remove(tag, 1.0, tkinter.END)
        self.config(foreground='black')


class Elise(tkinter.Tk):
    """ Main class for the application

    example:

    elise = Elise()
    elise.mainloop()
    """

    def __init__(self):
        super().__init__()

        self.is_check_active = False

        self.menu = None
        self.file_menu = None

        self.regex_entry = None
        self.regex_entry_ttp = None

        self.regex_error_text = None
        self.regex_check_error_text = None
        self.regex_check_text = None

        self.check_button = None
        self.check_button_ttp = None

        self.regex_entry_string = tkinter.StringVar()

        self.title(TITLE)
        self.geometry(GEOMETRY)

        self.init_gui()

    def init_gui(self):
        self.init_menu()

        self.bind('<Return>', self.enter_callback)

        self.regex_entry_string.trace_add('write', self.regex_entry_callback)
        self.regex_entry = tkinter.Entry(textvariable=self.regex_entry_string, width=45)
        self.regex_entry_ttp = ToolTip(self.regex_entry, "Pattern for search")
        self.regex_entry.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)

        self.regex_error_text = tkinter.Label()
        self.regex_error_text.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)

        self.regex_check_text = HighlightText(width=40)
        self.regex_check_text.tag_configure('red', foreground="#ff0000")
        self.regex_check_text.insert(tkinter.INSERT, 'Place text here')
        self.regex_check_text.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5)

        self.regex_check_error_text = tkinter.Label(text='')
        self.regex_check_error_text.grid(row=1, column=1)

        self.check_button = tkinter.Button(text='Check text', width=40, command=self.check_text_command,
                                           state=tkinter.DISABLED)
        self.check_button_ttp = ToolTip(self.check_button, "Process text")
        self.check_button.grid(row=3, column=0, ipady=5)

        self.config(menu=self.menu)

    def init_menu(self):
        self.init_file_menu()

        self.menu = tkinter.Menu()
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.menu.add_cascade(label='FAQ', command=self.faq_command)

    def init_file_menu(self):
        self.file_menu = tkinter.Menu()
        self.file_menu.add_command(label='Save', command=self.save_command)
        self.file_menu.add_command(label='Open', command=self.open_command)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.exit_command)

    def enter_callback(self, *args, **kwargs):
        """ Enter keyboard key callback

        :param args:
        :param kwargs:
        :return:
        """
        if self.is_check_active:
            self.check_text_command()

    def regex_entry_callback(self, *args, **kwargs):
        """ Callback for every change of text in the entry widget

        :param args:
        :param kwargs:
        :return:
        """
        reg_entry = self.regex_entry_string.get()
        if reg_entry == '':
            self.regex_error_text.config(text='')
            self.regex_check_error_text.config(text='')
        else:
            try:
                re.compile(reg_entry)
                self.check_button.config(state=tkinter.ACTIVE)
                self.regex_error_text.config(text='Correct regular expression', fg='green')
                self.is_check_active = True
            except Exception:
                self.check_button.config(state=tkinter.DISABLED)
                self.regex_error_text.config(text='Wrong regular expression', fg='red')
                self.is_check_active = False

    def check_text_command(self):
        """ Button/Enter key command to check the whole text for matching regular expression

        :return:
        """
        self.regex_check_text.clear_highlight('red')
        self.regex_check_text.highlight_pattern(self.regex_entry_string.get(), 'red', regexp=True)

        if self.regex_check_text.match_count == 0:
            self.regex_check_error_text.config(text='No matches', foreground='red')
        else:
            self.regex_check_error_text.config(text='{0} matches'.format(self.regex_check_text.match_count),
                                               foreground='green')

    def exit_command(self):
        self.destroy()

    def open_command(self):
        file_name = askopenfilename(filetypes=(('Elise files', '*.elise'),))

        if file_name:
            try:
                with open(file_name, 'r') as f:
                    first_line = f.readline()
                    if first_line == '':
                        showerror('Open Source File', 'Failed to read file\n {0}'.format(file_name))
                    else:
                        self.regex_entry_string.set(first_line)
            except:
                showerror('Open Source File', 'Failed to read file\n {0}'.format(file_name))

    def save_command(self):
        file_name = asksaveasfilename(filetypes=(('Elise files', '*.elise'),), defaultextension='elise')
        reg_entry = self.regex_entry_string.get()
        if file_name is None:
            return
        if reg_entry == '':
            showerror('Save', 'Failed to save empty expression\n {0}'.format(file_name))
        else:
            with open(file_name, 'w') as f:
                f.write(reg_entry)

    @staticmethod
    def faq_command():
        webbrowser.open('https://en.wikipedia.org/wiki/Regular_expression')


def main():
    elise = Elise()
    elise.mainloop()


if __name__ == '__main__':
    main()
