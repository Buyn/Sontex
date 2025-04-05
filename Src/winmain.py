# ----------------------------------------------
# * imports : 
# ----------------------------------------------
import sys
import eel  
from tkinter import filedialog
from tkinter import *
from global_values import *
import main as m
import datetime


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
    m.gui_calc(exel_path, csv_path, output_path, home_counter)
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
# ** def btn_ask_open_exel_file() : 
# ----------------------------------------------
@eel.expose
def btn_ask_open_exel_file(path,
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
    if isinstance( _filetypes[0], tuple) or isinstance( _filetypes[0], list):
        for text in _filetypes:
          _type.append(text)
    else:
      _type.append(_filetypes)
    _type.reverse()
    folder = filedialog.askopenfilename(initialdir = initialdir,
                                        title = _title,
                                        filetypes = tuple(_type))
    print("path = ", folder)
    if folder:
        print_to_log("шлях до файлу " + _filetypes[1]
                     + " задано = " + folder)
    return folder


# ----------------------------------------------
# ** def btn_ask_open_DBfiles():
# ----------------------------------------------
@eel.expose
def btn_ask_open_DBfiles(path,
                       _filetypes=(("rlv files","*.rvl"), ("csv files","*.csv")),
                       _title = "Select datebase files .csv or .rlv "):
    print("ptah = ", path,)
    print("_filetypes = ",      _filetypes,)
    print("_title = ",      _title)
    initialdir = "/" if not path or path == "" else path
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    _type = [("all files","*.*")]
    if isinstance( _filetypes[0], tuple) or isinstance( _filetypes[0], list):
        for text in _filetypes:
          _type.append(text)
    else:
      _type.append(_filetypes)
    _type.reverse()
    filepaths = filedialog.askopenfilenames( initialdir = initialdir,
                                          title = _title,
                                          filetypes = tuple(_type))
    print("path = ", filepaths)
    r = ""
    for path in filepaths:
      r = r + path +";"
    if r:
        print_to_log("шлях до файлу база даних задано = " + r)
    return r


# ----------------------------------------------
# ** def btn_asksaveasfile():
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
        print_to_log("Результуючий файл звіту обрано")
        print_to_log("шлях до файлу звіту = " + folder)
    return folder


# ----------------------------------------------
# ** -------------------------------------------
# * not expose : 
# ----------------------------------------------
# ** def print_to_log(string):
# ----------------------------------------------
def print_to_log(string):
    gui_log.append(datetime.datetime.now().strftime("%H:%M:%S.%f")+": "+ string)


# ** -------------------------------------------
# * if __name__ : 
# ----------------------------------------------
if __name__ == "__main__": 
    # sys.argv = ['', 'Test.testName']
    winmain(sys.argv)


# ----------------------------------------------
# * -------------------------------------------:
