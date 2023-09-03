from tkinter import *
import datetime
import my_people
import crud_people_record

class Application(object):

    def __init__(self, master):
        self.master = master

        # Frames
        self.top = Frame(master, height=200, bg='white')
        self.bottom = Frame(master, height=300, bg='green')
        self.top.pack(fill=X)
        self.bottom.pack(fill=X)

        # Labels & Icons
        self.top_title_lbl = Label(self.top, text='My Address Book App',
                                   font='Arial 15 bold', bg='white', fg='orange')
        self.top_title_lbl.place(x=300, y=80)
        self.top_icon = PhotoImage(file='Icons/book.png')
        self.top_title_icon = Label(self.top, image=self.top_icon, bg='white')
        self.top_title_icon.place(x=150, y=30)
        date = datetime.datetime.now().date()
        self.top_left_time_lbl = Label(self.top, text="Today's date: " + str(date), font='Arial 10 bold',
                                       bg='white', fg='orange')
        self.top_left_time_lbl.place(x=400, y=5)

        self.man_icon = PhotoImage(file='Icons/man.png')
        self.add_icon = PhotoImage(file='Icons/add.png')
        self.info_icon = PhotoImage(file='Icons/info.png')

        self.my_people_btn = Button(self.bottom, text="   My People ", image=self.man_icon,
                                    compound=LEFT, font='arial 15 bold', fg='black',
                                    width=200, command=self.open_my_people)
        self.my_people_btn.place(x=200,y=20)

        self.add_btn = Button(self.bottom, text="   Add People", image=self.add_icon,
                            compound=LEFT, font='arial 15 bold', fg='black', width=200,
                              command=self.open_add_people)
        self.add_btn.place(x=200,y=70)

        self.info_btn = Button(self.bottom, text="   Info           ", image=self.info_icon,
                          compound=LEFT, font='arial 15 bold', fg='black', width=200,
                               command=self.open_info)
        self.info_btn.place(x=200, y=120)


    def open_my_people(self):
        my_people_wd = my_people.My_People()


    def open_add_people(self):
        my_people_add = crud_people_record.My_People_Record('C')


    def open_info(self):
        about = About()


class About(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x500+400+100")
        self.resizable(False, False)
        self.title("About")
        # Frames
        self.frame = Frame(self, height=500, bg='blue')
        self.frame.pack(fill=X)
        text = "This application is for Educational Purposes"
        self.title_lbl = Label(self.frame, text=text, bg='blue',
                               font='Arial 12 bold', fg='white')
        self.title_lbl.place(x=100,y=100)
        text2 = "Technology stack used: "
        self.title_lbl = Label(self.frame, text=text2, bg='blue',
                               font='Arial 12 bold', fg='white')
        self.title_lbl.place(x=100, y=150)
        text3 = "* Front: Python Lybrary: Tkinter"
        self.title_lbl = Label(self.frame, text=text3, bg='blue',
                               font='Arial 12 bold', fg='white')
        self.title_lbl.place(x=200, y=200)
        text4 = "* Back: Python"
        self.title_lbl = Label(self.frame, text=text4, bg='blue',
                               font='Arial 12 bold', fg='white')
        self.title_lbl.place(x=200, y=250)
        text5 = "* Database: Sqlite"
        self.title_lbl = Label(self.frame, text=text5, bg='blue',
                               font='Arial 12 bold', fg='white')
        self.title_lbl.place(x=200, y=300)
        text6 = "* Dev IDE: Pycharm"
        self.title_lbl = Label(self.frame, text=text6, bg='blue',
                               font='Arial 12 bold', fg='white')
        self.title_lbl.place(x=200, y=350)

def main():
    root = Tk()
    root.title("Address Book Application")
    root.geometry("600x500+400+100")
    root.resizable(False, False)
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
