import tkinter

main_window = tkinter.Tk()
main_window.title("Starting to understand")
main_window.geometry("1080x720+650+8")

my_frame = tkinter.Frame(main_window, relief="groove", borderwidth="5")
my_frame.grid(row=0, column=0, sticky="nsew")

label = tkinter.Label(my_frame, text="Hello World")
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window, relief="groove", borderwidth=2)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief="groove", borderwidth=4)
canvas.grid(row=1, column=0)  # todo--> left_frame'e koyduktan sonra bu satırda yaptığın oynamaların
# önemi kalmıyor aslında

right_frame = tkinter.Frame(main_window, relief="groove", borderwidth=6)
right_frame.grid(row=1, column=2, sticky="nsew")

button1 = tkinter.Button(right_frame, text="Button1")
button2 = tkinter.Button(right_frame, text="Button2")
button3 = tkinter.Button(right_frame, text="Button3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

main_window.columnconfigure(0, weight=0)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)


# todo: columnconfigure = grid_columnconfigure
main_window.mainloop()

