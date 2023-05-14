from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pathlib import Path
from PIL import Image

sourcefile = ""
targetfile = ""

#setting the window
window = Tk()
window.title("Claudiu's image to icon converter")
window_width = 400
window_height = 250
#window.resizable(False, False)
window.minsize(width= window_width, height= window_height)
window.iconbitmap("Image_to_icon_converter\punisher_logo.ico")

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


#window content 
source_label = Label(window,font=("arial",16, "bold"), text="File to convert:")
source_label.place(x=100,y=10)
selected_source_label = Label(window, font=("arial",12), text="")
selected_source_label.place(x=100,y=40)

target_label = Label(window,font=("arial",16, "bold"), text="Targetfile path:")
target_label.place(x=100,y=70)
selected_target_label = Label(window, font=("arial",12), text="")
selected_target_label.place(x=100,y=100)

def openfile():
    global sourcefile
    global targetfile
    filetypes = (('PNG', '*.png'),('JPEG', '*.jpg'),('Bitmap', '*.bmp'),('TIFF', '*.tif'),('GIF', '*.gif'))
    sourcefile = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    selected_source_label.config(text=sourcefile)
    targetfile = fd.askdirectory()
    selected_target_label.config(text=targetfile)
    


search_button = Button(window, width=10, font=("arial",12, "bold"), text="Search_File", command= openfile)
search_button.place(x=50, y=170)

def convert():
    global sourcefile
    global targetfile
    save = fd.asksaveasfilename(defaultextension=".ico", confirmoverwrite=True)
    Image.open(sourcefile).save(save, icon_sizes=16)
    selected_source_label.config(text="")
    selected_target_label.config(text="")

convert_button = Button(window, width=10, font=("arial",12, "bold"), text="Convert", command= convert)
convert_button.place(x=200, y=170)
window.mainloop()

