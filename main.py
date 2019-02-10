from tkinter import *
from tkinter import ttk, font
from datetime import *


class Header (ttk.Frame):
    __btnLastYear = None
    __btnLastMonth = None
    __btnNextMonth = None
    __btnNextYear = None
    __lblMonth = None
    __month = "Enero"
    
    
    def __init__(self, parent, **args):
        
        ttk.Frame.__init__(self, parent, height=args['height'], width=args['width'])
    
        self.__lblMonth = ttk.Label(self, font = 'Arial', text = str(self.__month), anchor = 'center')
        self.__lblMonth.place(x=0, y=0)
        
        #Creamos un estilo común para los botones para luego aplicarlo a cada botón:
        s = ttk.Style()
        s.configure('my.Botton', width = 51, height = 30, font=('Arial', 24))
        
        self.__btnLastYear = ttk.Button (self, text="<<", style ='my.Botton')
        self.__btnLastYear.place(x=24, y=5)
        self.__btnLastMonth = ttk.Button (self, text="<", style ='my.Botton')
        self.__btnLastMonth.place(x=83, y=5)
        self.__btnNextMonth = ttk.Button (self, text=">", style ='my.Botton')
        self.__btnNextMown.place(x=398, y=5)
        self.__btnNextYear = ttk.Button (self, text=">>", style ='my.Botton')
        self.__btnNextYear.place(x=457, y=5)
        
'''        
class Calendar (ttk.Frame):
    
    def __init__(self, parent, **args):
        self.header = Header ()
        self.daysName = DaysName()
        self.month = Month ()
        self.activeYear
        self.activeMonth
        
    def backMonth ():
        
        
    def backYear ():
        
    
    def advMonth ():
        
    def advYear ():
        
'''

class DaysName (ttk.Frame):

    def __init__(self, parent, **args):
        
        ttk.Frame.__init__(self, parent)
        
        #Creamos un estilo común para las etiquetas de los días de la semana:
        s = ttk.Style()
        s.configure('my.DayName', width = 76, height = 20, font=('Arial', 11))
        self.__lblLunes = ttk.Label(self, text="Lunes", style = 'my.DayName')
        self.__lblLunes.place(x=0, y=38)
        self.__lblMartes = ttk.Label(self, text="Martes", style = 'my.DayName')
        self.__lblMartes.place(x=76, y=38)
        self.__lblMiercoles = ttk.Label(self, text="Miércoles", style = 'my.DayName')
        self.__lblMiercoles.place(x=152, y=38)
        self.__lblJueves = ttk.Label(self, text="Jueves", style = 'my.DayName')
        self.__lblJueves.place(x=228, y=38)
        self.__lblViernes = ttk.Label(self, text="Viernes", style = 'my.DayName')
        self.__lblViernes.place(x=304, y=38)
        self.__lblSabado = ttk.Label(self, text="Sábado", style = 'my.DayName')
        self.__lblSabado.place(x=380, y=38)
        self.__lblDomingo = ttk.Label(self, text="Domingo", style = 'my.DayName')
        self.__lblDomingo.place(x=456, y=38)

'''
class Month (ttk.Frame):
    
    def __init__(self, parent, **args):
        self.dates
        self.month
        self.year
        
    def setDates():
        

class Date(ttk.Frame):
    
    def __init__(self, parent, **args):
        self.date
        self.active
        self.weekend
        
    def setDate ():
    
    def setActive ():
        
    
'''

class MainApp (Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario Universal")
        self.geometry("532x422")
        self.header = Header(self, height=40, width=532)
        self.header.place(x=0, y=0)
        
    def start(self):
        self.mainloop()
        
if __name__ == '__main__':
    app = MainApp()
    app.start()
    
    
