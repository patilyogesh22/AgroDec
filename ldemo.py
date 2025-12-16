'''\import tkinter as tk
import mysql.connector
from tkinter import messagebox

def check_password():
    username = username_entry.get()
    password = password_entry.get()

    db = mysql.connector.connect(host="localhost", user="root", password="root", database="agrodec")
    cursor = db.cursor()

    query = f"SELECT * FROM register WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        tk.messagebox.showinfo("Success", "Login successful!")
    else:
        tk.messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.title("Login Form")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=check_password)
login_button.pack()

root.mainloop()

'''


import tkinter as tk
from Login import login

class Dashboard(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self, text=f"Welcome, {self.username}!")
        welcome_label.pack(padx=10, pady=10)

        profile_button = tk.Button(self, text="Profile", command=self.open_profile)
        profile_button.pack(padx=10, pady=10)

        logout_button = tk.Button(self, text="Logout", command=self.logout)
        logout_button.pack(padx=10, pady=10)

    def open_profile(self):
        # You can implement your own profile page here
        print("Opening profile page...")

    def logout(self):
        # Logout the user and redirect to the login page
        self.destroy()
        login()

if __name__ == "__main__":
    # Call the login function to get the username of the logged-in user
    username = login()

    # If the username is not None, create a Dashboard instance and start the main loop
    if username:
        dashboard = Dashboard(username)
        dashboard.mainloop()
