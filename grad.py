from algrebra import *
from window import window
from random import randint



def color_filter(color):
    result = []
    for el in color:
        if (el < 0):
            result.append(0)
        elif (el > 255):
            result.append(255)
        else:
            result.append(round(el))
    return tuple(result)


def rgb_to_hex(color):
    r, g, b = color
    return f'#{r:02x}{g:02x}{b:02x}'


def main(wind):
    wind.points = [(0, 0)] + wind.points + [(wind.width, wind.height)]
    
    [print(wind.points)]
    
    L = interpol(wind.points)
    dL = L.diff()
    N = len(wind.points)
    perp = []


    for p in wind.points:
        k = dL.value(p[0])
        if k==0:
            wind.canvas.create_line(p[0], 0, p[0], wind.height, fill=rgb_to_hex((0, 0, 0)))
        else:
            k = -1/k
            b = p[1] - k*p[0]
            perp.append(Poly([b, k]))

    colors = []
    for i in range(N):
        colors.append((wind.points[i][0], Vector(randint(0, 255), randint(0, 255), randint(0, 255))))
    #colors.append((width, Vector(255, 255, 255)))

    print(colors)
    
    #colors = [(0, Vector(0, 0, 0))] + colors + []
    
    color_func = interpol(colors).tuple()

    step = 0.1
    for dx in range(round(width/step)):
        x=dx*step
        color = color_filter(comp.value(x) for comp in color_func)
        """ 
        k = dL.value(x)
        if k == 0:
            wind.canvas.create_line(x, L.value(x), x+1, L.value(x+1), fill=rgb_to_hex(color))
        else:
            k = -1/k
            b = L.value(x) - k*x
            for y in range(width*2):
                wind.canvas.create_line(y/2, k*y/2+b, y/2+1, k*(y/2+1)+b, fill=rgb_to_hex(color)) 
        """
        wind.canvas.create_line(x, L.value(x), x+step, L.value(x+step), fill=rgb_to_hex((color)), width=10)

        wind.points = wind.points[1:-2]
        
    for i in range(N):
        wind.canvas.create_oval(colors[i][0] - 3, L.value(colors[i][0]) - 3, colors[i][0] + 3, L.value(colors[i][0]) + 3, fill=rgb_to_hex(colors[i][1].tuple()))




if __name__ == "__main__":
    title = 'Huy'
    width = 1200
    height = round(width*1080/1920)
    wind = window(title, width, height)

    def on_enter_pressed(event):
        main(wind)
    
    wind.bind("<Return>", on_enter_pressed)

    wind.mainloop()
