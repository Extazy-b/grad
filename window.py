import tkinter as tk
from random import randint


def rgb_to_hex(color):
    r, g, b = color
    return f'#{r:02x}{g:02x}{b:02x}'

def window(title, width, height):
    # Создаем основное окно
    root = tk.Tk()
    root.title(title)

    # Устанавливаем размеры окна
    root.width = width
    root.height = height

    # Создаем холст (Canvas) для рисования
    root.canvas = tk.Canvas(root, width=width, height=height)
    root.canvas.pack()

    # Массив для хранения координат точек
    root.points = []

    # Функция, которая вызывается при нажатии мыши
    def on_mouse_click(event):
        x, y = event.x, event.y
        root.points.append((x, y))  # Добавляем координаты в массив
        print(f"Point added: ({x}, {y})")
        # Рисуем точку на холсте
        root.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")

    def on_esc_pressed(event):
        root.points = []
        root.canvas.delete("all")

    def on_space_pressed(event):
        on_esc_pressed(event)

        for i in range(5):
            x = randint(round(root.width * 0.2), round(root.width * 0.8))
            y = randint(round(root.height * 0.2), round(root.height * 0.8))
            root.points.append((x, y))
            root.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")


    # Привязываем события
    root.canvas.bind("<Button-1>", on_mouse_click)  # Левый клик мыши
    root.bind("<space>", on_space_pressed)
    root.bind("<Escape>", on_esc_pressed)

    return root