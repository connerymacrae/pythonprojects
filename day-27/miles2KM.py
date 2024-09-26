from tkinter import *


def button_clicked():
    km = int(miles_input.get())*1.61
    converted_km_label.config(text=str(km))


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.config(justify='right')

miles_label = Label(text="Miles", font=('Courier', 18))
miles_label.grid(column=2, row=0)
miles_label.config(justify='left', padx=10)

is_equal_label = Label(text="is equal to", font=('Courier', 18))
is_equal_label.grid(column=0, row=1)

km_label = Label(text="KM", font=('Courier', 18))
km_label.grid(column=2, row=1)
km_label.config(justify='left')

converted_km_label = Label(text=str(0), font=('Courier', 18))
converted_km_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
