import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as font
import random
#variables


#importing database of text


#importing photo database


#generating window
window = tk.Tk()
window.minsize(window.winfo_screenwidth(),window.winfo_screenheight())
window.maxsize(window.winfo_screenwidth(),window.winfo_screenheight())
window.overrideredirect(1)
window.resizable(0, 0)
window.title("Animal Encyclopedia")
#scrolling
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


#frame
def main():
    animalDict = {}
    animals = []
    libraryFile = open('animalDatabaseStructure.txt', 'r')
    for i in libraryFile:
        line = i.split('thisistobereplaced')
        animalDict[line[0]] = line[1]
    animalsList = list(animalDict.keys())
    frame = VerticalScrolledFrame(window)
    frame.pack()
    bottomBar = tk.Frame()
    fontToUse= font.Font(family='Times New Roman', size=16, weight='bold')
    button = tk.Button(bottomBar, text='RANDOM', height=30, border=10, font=fontToUse,
                       command=lambda: randomAnimal(frame,animalDict, animalsList, bottomBar))
    button.pack(side='left')
    for i in range(len(animalDict)):
        newButton = (tk.Button(frame.interior, font=fontToUse, border='5', text=animalsList[i],
                               width=(window.winfo_screenwidth() - 50), bg='lightblue', fg='black',
                               command=lambda c=i: infoShower(frame,animals[c].cget("text"), animalsList[c], bottomBar,animalDict)))
        animals.append(newButton)
        animals[i].pack()
    bottomBar.pack()
    #searchText = tk.Text(bottomBar,width = 200,font = fontToUse, border = 10)
    #searchText.pack(side = 'right')
    window.mainloop()


def infoShower(frame,text,filepathstart,frameToDestroy,animalDict):
    fontToUse = font.Font(family='Times New Roman', size=16, weight='bold')
    frame.destroy()
    frameToDestroy.destroy()
    newFrame = VerticalScrolledFrame(window)
    newFrame.pack()
    label = tk.Label(newFrame.interior,text = animalDict[text],wraplength=(window.winfo_screenwidth()-50))
    img = ImageTk.PhotoImage(Image.open('pictures/'+filepathstart+('.jpeg')))
    imageLabel = tk.Label(newFrame.interior, image=img)
    imageLabel.img = img
    imageLabel.pack(side = 'top', fill = 'both',expand = 'yes')
    label.pack(side = 'bottom', fill = 'both',expand = 'yes')
    bottomBar = tk.Frame(window)
    button = tk.Button(bottomBar,font = fontToUse, text='BACK',height = 30,border = 10,command = lambda:restart(newFrame,bottomBar))
    button.pack(side='bottom')
    bottomBar.pack()

def randomAnimal(frame,animalDict,animalsList,bottomBar):
    randomAnimal = random.randint(0,len(animalsList))
    animalName = animalsList[randomAnimal]
    infoShower(frame,animalName,animalsList[randomAnimal],bottomBar,animalDict)

def restart(frame,bottombar):
    frame.destroy()
    bottombar.destroy()
    main()

main()