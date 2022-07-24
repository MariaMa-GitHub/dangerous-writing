# DANGEROUS WRITING
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import datetime

# program settings
PROGRAM_NAME = "Dangerous Writing"
BG_COLOR = "#A9A9A9"
WINDOW_SIZE = "600x450"
TIME_LIMIT = 5


# program class
class Program:

    # initialize settings
    def __init__(self):

        self.text = ""
        self.elapsed_time = 0

        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.window.geometry(WINDOW_SIZE)
        self.window.resizable(width=0, height=0)

        self.title_label = Label(text=PROGRAM_NAME, font=("Arial", 16, "bold"), bg=BG_COLOR, justify="center")
        self.title_label.grid(row=0, column=0, pady=10, sticky='we')

        self.user_textbox = ScrolledText(self.window, wrap=WORD, width=50, height=10, font=("Arial", 12, "normal"), padx=10, pady=10)
        self.user_textbox.grid(row=1, column=0, padx=5, pady=(20, 0), sticky='we')
        self.user_textbox.focus()

        self.save_button = Button(text=" SAVE ", width=20, font=("Arial", 12, "bold"), command=self.save_work)
        self.save_button.grid(row=2, column=0, padx=10, pady=(30, 0))

        self.dangerous_writing()

        self.window.mainloop()

    # save work
    def save_work(self):

        with open("work.txt", "a") as file:

            file.write("TEXT - " + datetime.datetime.now().strftime("%x") + "\n\n" + self.user_textbox.get("1.0", END).strip() + "\n\n")

    # write text
    def dangerous_writing(self):

        if self.user_textbox.get("1.0", END).strip() == self.text:
            self.elapsed_time += 1
        else:
            self.elapsed_time = 0

        if self.elapsed_time >= TIME_LIMIT:
            self.user_textbox.delete('1.0', END)

        self.text = self.user_textbox.get("1.0", END).strip()
        self.window.after(1000, self.dangerous_writing)


# main program
program = Program()
