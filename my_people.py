from tkinter import *
from tkinter import ttk
import sqlite3
import crud_people_record


connection = sqlite3.connect("address_book.db")
cursor = connection.cursor()

class My_People(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x500+400+100")
        self.resizable(False, False)
        self.title("My People")

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.bottom_frame = Frame(self, height=350, bg='orange')
        self.top.pack(fill=X)
        self.bottom_frame.pack(fill=X)

        # Labels & Icons
        self.top_title_lbl = Label(self.top, text='My People',
                                   font='Arial 15 bold', bg='white', fg='orange')
        self.top_title_lbl.place(x=300, y=50)
        self.top_icon = PhotoImage(file='Icons/person_icon.png')
        self.top_title_icon = Label(self.top, image=self.top_icon, bg='white')
        self.top_title_icon.place(x=150, y=10)

        # Listbox

        columns = ("#1", "#2", "#3")

        self.tv_people = ttk.Treeview(self.bottom_frame, show="headings",
                                      height="20", columns=columns)
        self.tv_people.heading('#1', text='Id_No', anchor='center')
        self.tv_people.column('#1', width=50, anchor='center', stretch=False)
        self.tv_people.heading('#2', text='First Name', anchor='center')
        self.tv_people.column('#2', width=180, anchor='center', stretch=True)
        self.tv_people.heading('#3', text='Last Name', anchor='center')
        self.tv_people.column('#3',width=180, anchor='center', stretch=True)
        self.tv_people.grid(row=0, column=0, padx=10, rowspan=10)

        # Scrollbar
        # Botones ADD, UPDATE, DISPLAY, DELETE

        self.add_btn = Button(self.bottom_frame, text="ADD", width=12,
                              font="sans 12 bold", command=self.add_record)
        self.add_btn.grid(row=0, column=2, padx=10)

        self.update_btn = Button(self.bottom_frame, text="UPDATE", width=12,
                              font="sans 12 bold", command=self.update_record)
        self.update_btn.grid(row=1, column=2, padx=10)

        self.display_btn = Button(self.bottom_frame, text="DISPLAY", width=12,
                                 font="sans 12 bold", command=self.view_record)
        self.display_btn.grid(row=2, column=2, padx=10)

        self.delete_btn = Button(self.bottom_frame, text="DELETE", width=12,
                                  font="sans 12 bold", command=self.delete_record)
        self.delete_btn.grid(row=3, column=2, padx=10)

        # sqlquery = "SELECT  people_first_name, people_last_name, " \
        #           "people_email, people_phone, people_address from 'people'"

        sqlquery = 'SELECT * from people'
        people = cursor.execute(sqlquery).fetchall()

        for p in people:
            self.tv_people.insert('','end', values=(p[0], p[1], p[2]))

    def add_record(self):
        self.destroy()
        mpr = crud_people_record.My_People_Record('C')


    def update_record(self):

        seleccion = self.tv_people.item(self.tv_people.focus())
        if seleccion.get('values'):
            user_id = seleccion['values'][0]
            self.destroy()
            mpr = crud_people_record.My_People_Record('U', user_id)



    def view_record(self):
        seleccion = self.tv_people.item(self.tv_people.focus())
        if seleccion.get('values'):
            user_id = seleccion['values'][0]
            self.destroy()
            mpr = crud_people_record.My_People_Record('D', user_id)



    def delete_record(self):
        seleccion = self.tv_people.item(self.tv_people.focus())
        if seleccion.get('values'):
            user_id = seleccion['values'][0]
            self.destroy()
            mpr = crud_people_record.My_People_Record('R', user_id)


