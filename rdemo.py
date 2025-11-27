import tkinter as tk
from tkinter import messagebox
import pymysql

# Connect to the MySQL database
db = pymysql.connect(host="localhost", user="root", password="root", database="agrodec",charset='utf8')
cursor = db.cursor()

def register():
    # Get the form fields
    user = entry_user.get()
    psw = entry_psw.get()
    repsw = entry_repsw.get()

    if user and psw and repsw:
            # Check if the user already exists
            query = "SELECT * FROM register WHERE username=%s"
            cursor.execute(query, (user,))
            result = cursor.fetchone()
            
            if result:
                messagebox.showinfo("User Already Exixst", "You already Register Please Login to your Account")
                window.destroy()
                os.system("Login.py")
                entry_user.delete(0, tk.END)
                entry_psw.delete(0, tk.END)
                entry_repsw.delete(0, tk.END)
                
            else:
                # Insert the new user into the database
                query = "INSERT INTO register (username, password, repassword) VALUES (%s, %s, %s)"
                cursor.execute(query, (user, psw, repsw))
                db.commit()
                # Show a success message
                messagebox.showinfo("Registration successful", "You have successfully registered.")

                # Clear the form fields
                entry_user.delete(0, tk.END)
                entry_psw.delete(0, tk.END)
                entry_repsw.delete(0, tk.END)

    else:
        # Show an error message
        messagebox.showerror("Error", "Please fill in all fields.")


# Create the registration window
window = tk.Tk()
window.title("Register")

# Create the form fields
entry_user = tk.Entry(window, font=("comic sans ms", 18, "bold"))
entry_psw = tk.Entry(window, font=("comic sans ms", 18, "bold"), show="*")
entry_repsw = tk.Entry(window, font=("comic sans ms", 18, "bold"), show="*")

# Create the form labels
label_user = tk.Label(window, text="Username:", font=("comic sans ms", 20, "bold"))
label_psw = tk.Label(window, text="Password:", font=("comic sans ms", 20, "bold"))
label_repsw = tk.Label(window, text="Re-Password:", font=("comic sans ms", 20, "bold"))

# Create the register button
button_register = tk.Button(window, text="Register", font=("comic sans ms", 15, "bold"), command=register)

# Place the form fields and labels on the window
label_user.grid(row=0, column=0, padx=10, pady=10)
entry_user.grid(row=0, column=1, padx=10, pady=10)

label_psw.grid(row=1, column=0, padx=10, pady=10)
entry_psw.grid(row=1, column=1, padx=10, pady=10)

label_repsw.grid(row=2, column=0, padx=10, pady=10)
entry_repsw.grid(row=2, column=1, padx=10, pady=10)


button_register.grid(row=4, column=1, padx=10, pady=10)

# Run the window's main loop
window.mainloop()

# Close the database connection
cursor.close()
db.close()
