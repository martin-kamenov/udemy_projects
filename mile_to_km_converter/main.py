from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=25, pady=25)
# window.minsize(width=300, height=150)


def calculate_result():
    miles = float(miles_input.get())
    result = miles * 1.609
    result_label.config(text=f"{result:.2f}")

#Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Result_label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

#Button
calculate_button = Button(text="Calculate", command=calculate_result)
calculate_button.grid(column=1, row=2)


window.mainloop()

