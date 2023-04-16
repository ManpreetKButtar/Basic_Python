from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=500, height=500, bg="Skyblue")
        self.myCanvas.grid()
      
        my_arc_id = self.myCanvas.create_arc(200, 200, 360, 360, outline="blue",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(180, 180, 380, 380, outline="lightgreen",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(160, 160, 400, 400, outline="yellow",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(140, 140, 420, 420, outline="orange",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(120, 120, 440, 440, outline="red",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_rect_id = self.myCanvas.create_rectangle(0, 500, 500, 280,outline="green", fill="green")
        self.myCanvas.update()
        sleep(1)
        my_circle_id = self.myCanvas.create_oval(0, 180, 40, 220,outline="orange", fill="orange")


frame02 = MyFrame()
frame02.mainloop()
