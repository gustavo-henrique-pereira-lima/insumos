
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Gusta\Área de Trabalho\Projeto Estágio\design\build\assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    356.0,
    171.0,
    anchor="nw",
    text="Seja bem vindo",
    fill="#000000",
    font=("Inter Bold", 96 * -1)
)

canvas.create_rectangle(
    276.0,
    405.0,
    1168.0,
    505.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    276.0,
    524.0,
    1168.0,
    624.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    505.0,
    656.2109375,
    934.0,
    781.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    674.0,
    295.0,
    765.0,
    386.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
