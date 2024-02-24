"""Author: Alivia sutherland
Date Written: 2/24/24
Assignemnt: final project
Short description: import gui to create housekeeping schedule ."""



#type yes or no to schedule an appointment
print ("Would you like to schedule an appointment with housekeeping?")
valid_response = False
while not valid_response:
    response = input("Enter 'yes' or 'no': ")
    if response.lower() == 'yes' or response.lower() == 'no':
        valid_response = True
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
 
from tkinter import *
 
#import tkinter
#import calendar from python
import calendar
 
def showCal() :
 
   #create new gui
    new_gui = Tk()
 #create size of gui calendar
    new_gui.geometry("600x600")
     # create background color
    new_gui.config(background = "black")
    #title calendar
    new_gui.title("HOUSEKEEPING CALENDAR")
 
    #insert year 
    fetch_year = int(year_field.get())
 
    #create calendar with year
    cal_content = calendar.calendar(fetch_year)
      #create calendar with font
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
 
   #create grid
    cal_year.grid(row = 5, column = 1, padx = 20)
     
  #loop
    new_gui.mainloop()
 
     

if __name__ == "__main__" :
 
    
    gui = Tk()
     
    gui.config(background = "black")
 
    gui.title(" HOUSEKEEPING CALENDAR")
 
   
    gui.geometry("250x140")
    
    #colors and fonts
 
    cal = Label(gui, text = "CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))
 
    year = Label(gui, text = "Enter Year", bg = "light blue")
     
    year_field = Entry(gui)
 
  
    Show = Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = showCal)
 
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
     
     #size of grids
   
    cal.grid(row = 1, column = 1)
 
    year.grid(row = 2, column = 1)
 
    year_field.grid(row = 3, column = 1)
 
    Show.grid(row = 4, column = 1)
 
    Exit.grid(row = 6, column = 1)
     
   
    gui.mainloop()

    #this is where they will choose the actual date. working on this portion

    print ("Now choose a date that is suitable for you")
    valid_response = False
while not valid_response:
    response = input("Enter 'yes' or 'no': ")
    if response.lower() == 'yes' or response.lower() == 'no':
        valid_response = True
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")