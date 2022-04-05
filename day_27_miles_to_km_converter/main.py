from tkinter import *


def button_clicked():
    miles = float(miles_input.get())
    km = round(miles*1.609, 2)
    km = int(km) if km.is_integer() else km
    result_label.config(text=km)


# Screen
screen = Tk()
screen.minsize(300, 150)
screen.title("Miles to Km Converter")
screen.grid_rowconfigure(0, weight=1)
screen.grid_rowconfigure(4, weight=1)
screen.grid_columnconfigure(0, weight=1)
screen.grid_columnconfigure(4, weight=1)
screen.eval('tk::PlaceWindow . center')

# Entry
miles_input = Entry()
miles_input.grid(row=1, column=2)
miles_input.config(justify="center", width=15)
miles_input.focus_set()

# Labels
miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

equal_label = Label(text="is equal to")
equal_label.grid(row=2, column=1)

result_label = Label(text="0")
result_label.grid(row=2, column=2)

km_label = Label(text="Km")
km_label.grid(row=2, column=3)

# Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=3, column=2)


screen.mainloop()
