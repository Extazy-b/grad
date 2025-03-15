import tkinter as tk
from grad import interpol

def rgb_to_hex(color):
    r, g, b = color
    return f'#{r:02x}{g:02x}{b:02x}'

# Создаем основное окно
root = tk.Tk()
root.title("Pixel Coloring")

# Устанавливаем размеры окна
width = 400
height = 400

# Создаем холст (Canvas) для рисования
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Массив для хранения координат точек
points = []

# Функция, которая будет вызвана при нажатии Enter
def on_enter_pressed(event):
    graph = interpol(points)
    for x, y in graph:
        canvas.create_line(x, y, x+1, y, fill=rgb_to_hex((0, 0, 0)))

# Функция, которая вызывается при нажатии мыши
def on_mouse_click(event):
    x, y = event.x, event.y
    points.append((x, y))  # Добавляем координаты в массив
    print(f"Point added: ({x}, {y})")
    # Рисуем точку на холсте
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red")

# Привязываем события
canvas.bind("<Button-1>", on_mouse_click)  # Левый клик мыши
root.bind("<Return>", on_enter_pressed)    # Клавиша Enter


# Запускаем главный цикл обработки событий
root.mainloop()