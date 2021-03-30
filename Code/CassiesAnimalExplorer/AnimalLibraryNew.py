import os
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as font
import random

window = tk.Tk()
#class
class VerticalScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL,width = 50)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,yscrollcommand=vscrollbar.set,height = (window.winfo_screenheight()-50))
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
        # This is what enables scrolling with the mouse:

#variables
#importing list of animals for buttons
def importAnimalNames(filepath):
    files = os.walk(filepath)
    animalNames = []
    for i in files:
        animalNames.append(i[2])
    return animalNames[0]

def upOrDownPressedFunc(int,upOrDownPressed,animals,animalNames):
    if((int == -1) and upOrDownPressed[0]>0):
        upOrDownPressed[0] += int
        print(upOrDownPressed[0])
    elif(int == 1):
        upOrDownPressed[0] += int
        print(upOrDownPressed[0])
    for i in range(len(animals)):
        animals[i]['text'] = animalNames[i+upOrDownPressed[0]]

def jumpToLetter(animals,animalNames):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def infoShower(frame,title,frameToDestroy,window,font):
    print(title)
    file = open('Summaries/'+title,'r',encoding='utf8')
    string = title + '\n'
    for i in file:
        string += i
    fontToUse = font
    frame.destroy()
    frameToDestroy.destroy()
    newFrame = VerticalScrolledFrame(window)
    newFrame.pack()
    label = tk.Label(newFrame.interior, text=string,font=fontToUse, wraplength=(window.winfo_screenwidth() - 50))
    label.pack(side='top', fill='both', expand='yes')
    bottomBar = tk.Frame(window)
    button = tk.Button(bottomBar, font=fontToUse, text='BACK', height=30, border=10,
                       command=lambda: restart(newFrame, bottomBar))
    button.pack(side='bottom')
    for i in os.walk("Images/"+title):
        for a in i[2]:
            img = ImageTk.PhotoImage(Image.open('Images/'+title+'/'+a))
            imageLabel = tk.Label(master = newFrame.interior, image=img)
            imageLabel.img = img
            imageLabel.pack(side='bottom', fill='both', expand='yes')
    bottomBar.pack()

def restart(frame,bottombar):
    frame.destroy()
    bottombar.destroy()
    main()

def randomAnimal(frame,animalNames,bottomBar):
    print('random')

#importing photo database


#generating window


#frame

def main():
    window.minsize(window.winfo_screenwidth(), window.winfo_screenheight())
    window.maxsize(window.winfo_screenwidth(), window.winfo_screenheight())
    window.overrideredirect(1)
    window.resizable(0, 0)
    window.title("Animal Encyclopedia")
    animalNames = importAnimalNames('Summaries')
    fontToUse = font.Font(family='Times New Roman', size=16, weight='bold')
    upOrDownPressed = [0]
    animalButtons = []
    frame = tk.Frame()
    bottomBar = tk.Frame()
    randomButton = tk.Button(bottomBar, text='RANDOM', height=1, border=10, font=fontToUse,
                             command=lambda: randomAnimal(frame, animalNames, bottomBar))
    downButton = tk.Button(bottomBar, text='DOWN', height=1, border=10, font=fontToUse,
                           command=lambda: upOrDownPressedFunc(1, upOrDownPressed, animalButtons,animalNames))
    upButton = tk.Button(bottomBar, text='UP', height=1, border=10, font=fontToUse,
                         command=lambda: upOrDownPressedFunc(-1, upOrDownPressed, animalButtons,animalNames))
    for i in range(21):
        newButton = (tk.Button(master = frame,font=fontToUse, border='5', text=animalNames[i], width=(window.winfo_screenwidth()),
                               bg='lightblue', fg='black',
                               command=lambda c=i: infoShower(frame, animalButtons[c].cget("text"), bottomBar,window,fontToUse)))
        animalButtons.append(newButton)
        animalButtons[i].pack()
    upButton.pack(side=tk.LEFT)
    randomButton.pack(side=tk.LEFT)
    downButton.pack(side=tk.RIGHT)
    frame.pack()
    bottomBar.pack()
    window.mainloop()

if __name__ == '__main__':
    main()