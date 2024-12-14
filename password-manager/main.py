import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
        #                                                       f"\nPassword: {password} \nIs ok to save?")

        try:
            # Reading old data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            #Creaing the file with new data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "mkamenov01@abv.bg")
            password_entry.delete(0, END)



# ---------------------------- SEARCH FOR CREDENTIALS ------------------------------- #
def search_credentials():
    website = web_entry.get()

    if website == "show_me_all":
        with open("data.json", "r") as data_file:
            # Reading data
            data = json.load(data_file)

            final_result = []

            for web, credentials in data.items():
                final_result.append(
                    f"{web.title()} Credentials: \nuser: {credentials['email']} \npassword: {credentials['password']} \n\n {20 * '*'} \n")

            messagebox.showinfo(title="Show all saved credentials", message="\n".join(final_result))
            return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")
    else:
        try:
            credentials = data[website]
        except KeyError:
            messagebox.showerror("Search not found", "No details for the website exists")
        else:
            email = credentials["email"]
            password = credentials["password"]

            messagebox.showinfo(f"Credentials for {website}", f"Email: {email} \nPassword: {password}")
            pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "mkamenov01@abv.bg")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=14, command=search_credentials, highlightthickness=0)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password, highlightthickness=0)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_data, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()