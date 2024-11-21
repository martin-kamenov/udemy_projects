import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

#Label
my_label = tkinter.Label(text="Here is the label", font=("new times roman", 22, "bold"))
my_label["text"] = "New text"
# my_label.config(text="Here is the new new text")
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = tkinter.Entry(width=10)
# print(input.get())
input.grid(column=3, row=2)

#New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

window.mainloop()