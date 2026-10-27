from database import create_tables
from seed_data import create_default_data
from login_gui import LoginWindow
from tkinter import Tk

create_tables()
create_default_data()

root = Tk()
app = LoginWindow(root)
root.mainloop()
