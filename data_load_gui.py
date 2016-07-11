import Tkinter as tk
import tkMessageBox
from LWH_dataload import dataload
import Cocoa


'''
We want to collect the month, year, outputfile name, and build the script using this information.
We want to create the urls, then create the output file
we can do this in the constructor
'''
class data_gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #creating the graphic features
        self.month = tk.Entry(self)
        self.year = tk.Entry(self)
        self.filename = tk.Entry(self)
        self.button = tk.Button(self, text="Run", command=self.on_button)
        self.month_label = tk.Label(self,text="Month Number (ex. 1)")
        self.year_label = tk.Label(self,text="Year (ex. 2016)")
        self.filename_label = tk.Label(self,text="output filename no spaces (ex. output.csv)")

        #orienting the graphic features
        self.month_label.grid(row = 0)
        self.month.grid(row = 0, column = 1)
        self.year_label.grid(row=1)
        self.year.grid(row = 1, column = 1)
        self.filename_label.grid(row = 2)
        self.filename.grid(row=2, column = 1)
        self.button.grid(row=3, column = 1)

    def on_button(self):
        # validate the input here, if incorrect create a dialog box
        try:
            month = int(self.month.get())
            year = int(self.year.get())
            filename = self.filename.get()
            pathToApp = Cocoa.NSBundle.mainBundle().bundlePath()
            source_path = pathToApp.split('/')
            del source_path[-1]
            new_path = '/'.join(source_path)
            pass_file = new_path + '/' + filename
            data = dataload(month,year,pass_file)
            data.main()

        except ValueError:
                self.error_event()
                pass
    def error_event(self):
        tkMessageBox.showerror("Error", "Please only input whole numbers")


app = data_gui()
app.mainloop()
