from tkinter import *
from wm import WM

font_list = ["Arial", "Verdana"]


def add_watermark():
    image_file_path = file_path_input.get()
    fnt_size = int(font_size.get()) * 10
    opacity = int(opacity_scale.get())
    text = watermark_text.get()
    positions = get_positions()
    font = font_choice()
    wm = WM(image_file_path, text, positions, font, fnt_size, opacity)
    wm.out.show()


def get_positions():
    positions = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    return positions


def font_choice():
    font = (font_spinbox.get() + ".ttf").lower()
    return font


window = Tk()
window.title("WaterMarkAdd")
window.minsize(width=300, height=200)
window.config(padx=5, pady=5)

# Labels
file_path_label = Label(text="Image file path", font=("Arial", 12, "bold"))
file_path_label.grid(column=0, row=0, columnspan=2)

watermark_text_label = Label(text="Watermark text", font=("Arial", 12, "bold"))
watermark_text_label.grid(column=0, row=2, columnspan=2)

placement_label = Label(text="Placement", font=("Arial", 12, "bold"))
placement_label.grid(column=0, row=4)

font_size_label = Label(text="Font size (px *10)", font=("Arial", 12, "bold"))
font_size_label.grid(column=1, row=4)

opacity_label = Label(text="Opacity", font=("Arial", 12, "bold"))
opacity_label.grid(column=1, row=6)

font_label = Label(text="Font", font=("Arial", 12, "bold"))
font_label.grid(column=1, row=8)


# Buttons
fp_button = Button(text="Add Watermark", command=add_watermark)
fp_button.grid(column=0, row=10, columnspan=2)
fp_button.config(bd=3)

# Entry
file_path_input = Entry(width=60)
file_path_input.grid(column=0, row=1, columnspan=2)

watermark_text = Entry(width=60)
watermark_text.grid(column=0, row=3, columnspan=2)

# Scale

font_size = Scale(orient=HORIZONTAL, from_=1, to=100)
font_size.grid(column=1, row=5)

opacity_scale = Scale(orient=HORIZONTAL, from_=0, to=255)
opacity_scale.grid(column=1, row=7)

# Spinbox
choices_var = StringVar(value=font_list)
font_spinbox = Spinbox(values=font_list, textvariable=choices_var)
font_spinbox.grid(column=1, row=9, pady=10)


# vars
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()


# positioning checkbuttons
lt = Checkbutton(text="Left Top", variable=var1, offvalue="", onvalue='lt')
lt.grid(column=0, row=6, sticky="w")
lb = Checkbutton(text="Left Bottom", variable=var2, offvalue="", onvalue='lb')
lb.grid(column=0, row=7, sticky="w")
rt = Checkbutton(text="Right Top", variable=var3, offvalue="", onvalue='rt')
rt.grid(column=0, row=8, sticky="w")
rb = Checkbutton(text="Right Bottom", variable=var4, offvalue="", onvalue='rb')
rb.grid(column=0, row=9, sticky="w")
ct = Checkbutton(text="Center", variable=var5, offvalue="", onvalue='ct')
ct.grid(column=0, row=5, sticky="w")

window.mainloop()
