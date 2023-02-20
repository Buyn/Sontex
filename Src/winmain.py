# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import sys
import eel  
from tkinter import filedialog
from tkinter import *
from main import *


# ----------------------------------------------
# * vars :
# ----------------------------------------------


# ----------------------------------------------
# ** ------------------------------------------:
# * def winmain(argv):
# ----------------------------------------------
def winmain(argv):
    eel.init("web")    
    # Start the index.html file  
    eel.start("index.html"
              , mode=gg_eel_mode
              )  
    

# * expose : 
# ----------------------------------------------
# ** def random_python() : 
# ----------------------------------------------
# @eel.expose      
# def random_python():  
#     """ Exposing the random_python function 
#     to javascript"""  
#     print("Random function running")  
#     return randint(1,100)  


# ----------------------------------------------
# ** def start_calc() : 
# ----------------------------------------------
@eel.expose      
def start_calc(exel_path, csv_path):  
    """ 
    start calculation of all values
    on geting exel and csv files
    """  
    print("start calc")  
    gui_calc(exel_path, csv_path)
    print("end calc")  
    # return randint(1,100)  


# ----------------------------------------------
# ** def btn_ResimyoluClick() : 
# ----------------------------------------------
@eel.expose
def btn_ResimyoluClick(path):
    initialdir = "/" if not path or path == "" else path
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    # folder = filedialog.askdirectory()
    folder = filedialog.askopenfilename(initialdir = initialdir,
                                        title = "Select file exel",
                                        filetypes = (("jpeg files","*.jpg"),
                                                     ("all files","*.*")))
    print("path = ", folder)
    return folder


# ----------------------------------------------
# ** -------------------------------------------
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    # sys.argv = ['', 'Test.testName']
    winmain(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
