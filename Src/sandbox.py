# ----------------------------------------------
# * import : 
# ----------------------------------------------
from random import randint  
import eel  
# from main import *
from tkinter import filedialog
from tkinter import *

# ----------------------------------------------
# * vars : 
# ----------------------------------------------


# ----------------------------------------------
# * main :
# ----------------------------------------------
# gg_eel_mode = 'electron'
gg_eel_mode = 'chrome'
# gg_eel_mode = None
# gg_eel_mode = 'edge'
     
@eel.expose
def btn_ResimyoluClick():
	root = Tk()
	root.withdraw()
	root.wm_attributes('-topmost', 1)
	# folder = filedialog.askdirectory()
	folder = filedialog.askopenfilename(initialdir = "/",title = "Select file exel",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	return folder
# print (root.filename)
print("result path", btn_ResimyoluClick())


eel.init("web")    

# Exposing the random_python function to javascript  
@eel.expose      
def random_python():  
    print("Random function running")  
    return randint(1,100)  

# Start the index.html file  
eel.start("index.html"
          , mode=gg_eel_mode
          )  


# ----------------------------------------------
# * -------------------------------------------:
