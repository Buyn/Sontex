# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import sys
import eel  
from tkinter import filedialog
from tkinter import *
from global_values import *
# from main import gui_calc


# ----------------------------------------------
# * vars :
# ----------------------------------------------
gui_log =[]

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
# ** def start_calc() : 
# ----------------------------------------------
@eel.expose      
def start_calc(exel_path, csv_path, output_path, home_counter):  
    """ 
    start calculation of all values
    on geting exel and csv files
    """  
    print("start calc")  
    print(exel_path, csv_path, output_path, home_counter)
    gui_calc(exel_path, csv_path, output_path, home_counter)
    print("end calc")  


# ----------------------------------------------
# ** def pull_log() : 
# ----------------------------------------------
@eel.expose      
def pull_log():  
    """ 
    Pull values from log variable
    """  
    # print("log pull requst")  
    r = gui_log.copy()
    gui_log.clear()
    return r


# ----------------------------------------------
# ** def btn_ResimyoluClick() : 
# ----------------------------------------------
@eel.expose
def btn_ResimyoluClick(path,
                       _filetypes=("excel files","*.xlsx"),
                       _title = "Select file exel"):
    print("ptah = ", path,)
    print("_filetypes = ",      _filetypes,)
    print("_title = ",      _title)
    initialdir = "/" if not path or path == "" else path
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    _type = [("all files","*.*")]
    _type.append(_filetypes)
    _type.reverse()
    folder = filedialog.askopenfilename(initialdir = initialdir,
                                        title = _title,
                                        filetypes = tuple(_type))
    print("path = ", folder)
    if folder:
        print_to_log("путь к фаилу "+
                     _filetypes[1] +
                     " задан = "
                     + folder)
    return folder


# ----------------------------------------------
# ** def btn_asksaveasfile() : 
# ----------------------------------------------
@eel.expose
def btn_asksaveasfile(path,
                       _filetypes=("excel files","*.xlsx"),
                       _title = "Сохранить отчёт как"):
    print("ptah = ", path,)
    print("_filetypes = ",      _filetypes,)
    print("_title = ",      _title)
    initialdir = "/" if not path or path == "" else path
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    _type = [("all files","*.*")]
    _type.append(_filetypes)
    _type.reverse()
    folder = filedialog.asksaveasfilename(initialdir = initialdir,
                                          defaultextension="*.xlsx",
                                          title = _title,
                                          filetypes = tuple(_type))
    print("path = ", folder)
    if folder:
        print_to_log("Резултируюший фаил отчёта утсановлен")
        print_to_log("путь к фаилу отчёта = " + folder)
    return folder


# ----------------------------------------------
# ** -------------------------------------------
# * not expose : 
# ----------------------------------------------
# ** def print_to_log(string) : 
# ----------------------------------------------
def print_to_log(string):
    gui_log.append(string)


# ** -------------------------------------------
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    # sys.argv = ['', 'Test.testName']
    winmain(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
