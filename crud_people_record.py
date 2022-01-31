from tkinter import *
import sqlite3
from tkinter import messagebox
import my_people

connection = sqlite3.connect("address_book.db")
cursor = connection.cursor()


class My_People_Record(Toplevel):

    def __init__(self, mode, user_iid=0):
        Toplevel.__init__(self)
        self.mode = mode
        self.user_id = user_iid

        if mode == 'C':
            # Create
            title = "Add People"
            icon = 'Icons/addperson.png'
            first_nametxt = ""
            last_nametxt = ""
            emailtxt = ""
            phonetxt = ""
            addresstxt = ""
            statetxt= NORMAL

        else:
            sqltext = "SELECT * FROM 'people' WHERE people_id = ?"
            _, first_nametxt, last_nametxt, emailtxt, phonetxt, addresstxt  = cursor.execute(sqltext,(self.user_id,)).fetchone()

            if mode == "R":
                # Remove
                title = "Remove People"
                icon = 'Icons/update.png'
                statetxt= DISABLED

            elif mode == 'U':
                # Update
                title = "Update People"
                icon = 'Icons/update.png'
                statetxt= NORMAL

            else:
                # Display
                title = "Display People"
                icon = 'Icons/about.png'
                statetxt= DISABLED

        self.geometry("600x500+400+100")
        self.resizable(False, False)
        self.title("Add People")
        # Frames
        self.top_frame = Frame(self, height=150, bg='white')
        self.bottom_frame = Frame(self, height=350, bg='orange')
        self.top_frame.pack(fill=X)
        self.bottom_frame.pack(fill=BOTH)

        # Labels & Icons TOP
        self.top_title_lbl = Label(self.top_frame, text=title,
                                   font='Arial 15 bold', bg='white', fg='orange')
        self.top_title_lbl.place(x=300, y=50)
        self.top_icon = PhotoImage(file=icon)
        self.top_title_icon = Label(self.top_frame, image=self.top_icon, bg='white')
        self.top_title_icon.place(x=150, y=10)

        # Labels & Entries Bottom first name, last name, email, phone, address
        # First Name
        self.bot_first_name_lbl = Label(self.bottom_frame, text="First Name: ",
                                        font='Arial 12', width=15, bg='orange', anchor=W)
        self.bot_first_name_entry = Entry(self.bottom_frame, font='Arial 12', width=40)
        self.bot_first_name_entry.insert(0, first_nametxt)
        self.bot_first_name_entry.config(state=statetxt)

        # Last Name
        self.bot_last_name_lbl = Label(self.bottom_frame, text="Last Name: ",
                                        font='Arial 12', width=15, bg='orange', anchor=W)

        self.bot_last_name_entry = Entry(self.bottom_frame, font='Arial 12', width=40)
        self.bot_last_name_entry.insert(0, last_nametxt)
        self.bot_last_name_entry.config(state=statetxt)

        # Email
        self.bot_email_lbl = Label(self.bottom_frame, text="Email: ",
                                       font='Arial 12', width=15, bg='orange', anchor=W)

        self.bot_email_entry = Entry(self.bottom_frame, font='Arial 12', width=40 )
        self.bot_email_entry.insert(0, emailtxt)
        self.bot_email_entry.config(state=statetxt)
        # Phone

        self.bot_phone_lbl = Label(self.bottom_frame, text="Phone: ",
                                   font='Arial 12', width=15, bg='orange', anchor=W)

        self.bot_phone_entry = Entry(self.bottom_frame, font='Arial 12', width=40)
        self.bot_phone_entry.insert(0, phonetxt)
        self.bot_phone_entry.config(state=statetxt)
        # Address
        self.bot_address_lbl = Label(self.bottom_frame, text="Address: ",
                                   font='Arial 12', width=15, bg='orange', anchor=W)

        self.bot_address_entry = Text(self.bottom_frame, font='Arial 12', width=40,
                                       height=5, wrap=WORD)
        self.bot_address_entry.insert(END, addresstxt)
        self.bot_address_entry.config(state=statetxt)
        # Button Add People
        if self.mode=='D':
            title = "CLOSE"

        self.bot_add_but = Button(self.bottom_frame, text=title, font='sans 15 bold',
                                  command=self.confirm_action)


        self.bot_first_name_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.bot_first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.bot_last_name_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.bot_last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.bot_email_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.bot_email_entry.grid(row=2, column=1, padx=10, pady=10)
        self.bot_phone_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.bot_phone_entry.grid(row=3, column=1, padx=10, pady=10)
        self.bot_address_lbl.grid(row=4, column=0, padx=10, pady=10)
        self.bot_address_entry.grid(row=4, column=1, padx=10, pady=10)
        self.bot_add_but.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

    def confirm_action(self):
        first_name = self.bot_first_name_entry.get()
        last_name = self.bot_last_name_entry.get()
        email = self.bot_email_entry.get()
        phone = self.bot_phone_entry.get()
        address = self.bot_address_entry.get(0.0,'end')
        success = False


        if self.mode == 'C':
            sqlquery = "INSERT INTO 'people' (people_first_name, people_last_name, " \
                        "people_email, people_phone, people_address) VALUES (?,?,?,?,?)"
            if first_name and last_name and email and phone and address != "":
                try:
                    cursor.execute(sqlquery, (first_name, last_name, email, phone, address))
                except Exception:
                    messagebox.showerror("Error", "There is something wrong")
                else:
                    messagebox.showinfo("Success", "Successful addition")
                    success = True
            else:
                messagebox.showerror("Error", "Fields cannot be empty")
        elif self.mode == 'D':
            # DISPLAY
            self.destroy()
            my_people_wd = my_people.My_People()
        elif self.mode == 'R':
            # DELETE
            sqlquery = "DELETE FROM 'people' WHERE people_id= ?"
            try:
                cursor.execute(sqlquery,(self.user_id,))
            except Exception:
                messagebox.showerror("Error", "There is something wrong")
            else:
                messagebox.showinfo("Success", "Successful removal")
                success = True
        elif self.mode == 'U':
            sqlquery = "UPDATE 'people' SET people_first_name = ?, people_last_name = ?, " \
                       "people_email=?, people_phone=?, people_address=? WHERE people_id=?"
            if first_name and last_name and email and phone and address != "":
                try:
                    cursor.execute(sqlquery, (first_name, last_name, email, phone, address,self.user_id))
                except Exception:
                    messagebox.showerror("Error", "There is something wrong")
                else:
                    messagebox.showinfo("Success", "Successful update")
                    success = True
            else:
                messagebox.showerror("Error", "Fields cannot be empty")
        if success:
            connection.commit()
            my_people_wd = my_people.My_People()
            self.destroy()