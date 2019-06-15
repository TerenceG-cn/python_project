if __name__ == '__main__':
    from tkinter import *

    root = Tk()
    # canvas = Canvas(width=300, height=300, bg='green')
    # canvas.pack(expand=YES, fill=BOTH)
    #
    # x0 = 263
    # y0 = 263
    # y1 = 275
    # x1 = 275
    # for i in range(19):
    #     canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
    #     x0 = x0 - 10
    #     y0 = y0 - 5
    #     x1 = x1 + 5
    #     y1 = y1 + 10
    # x0 = 263
    # y1 = 275
    # y0 = 263
    # for i in range(21):
    #     canvas.create_line(x0, y0, x0, y1, fill='red')
    #     x0 += 5
    #     y0 += 5
    #     y1 += 5
    #
    # canvas.create_rectangle(100, 1000, 1000, 100)

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    import math

    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')

    root.mainloop()
