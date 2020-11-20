from tkinter import *

root = Tk()
root.title('window')
root.overrideredirect(True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "gray")
canvas = Canvas(root, bg='gray', width=screen_width, height=screen_height)
canvas.place(x=-2, y=-2)
root.mainloop()
