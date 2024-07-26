"""
Author: Juanita Granger
Assignment: M08 Final Project
Version 3.0 07/25/24
This program is suppose to help users calculate the
GPA based off their current grades.
"""

from tkinter import*
from PIL import Image, ImageTk



root = Tk()
root.title("GPA Calculator")
root.geometry("600x400")

def Calculate(grades):
    points = 0
    i = 0
    grading = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0}
    if grades != []:
        for grade in grades:
            if grade not in grading:
                return "invalid"
        points += grading[grade]
        gpa = points/len(grades)
        return gpa
    else:
        return None
totalGPA = Label(root, text="Your GPA is: ")
totalGPA.grid(row=5,column=0, sticky=NSEW)
            

def Reset():
    for widget in root.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0,"end")
   


    
courses = Label(root, text="Courses(Optional)").grid(row=0,column=0, sticky=NSEW)
grade = Label(root, text="Grade").grid(row=0, column=1, sticky=NSEW)
credit = Label(root,text="Credits").grid(row=0, column=2, sticky=NSEW)
gpa = Label(root, text="GPA Points").grid(row=0, column=3, sticky=NSEW)

course_entry = Entry(root).grid(row=1,column=0, sticky=NSEW)
grade_entry = Entry(root).grid(row=1, column=1, sticky=NSEW)
credit_entry = Entry(root).grid(row=1, column=2, sticky=NSEW)
gpa_entry = Entry(root).grid(row=1, column=3, sticky=NSEW)

cal_button = Button(root,text="Calculate Button", command= lambda:Calculate()).grid(row=2, column=0, sticky=NSEW)
Button(root, text="Exit", command=lambda:exit()).grid(row=3, column=0, sticky=NSEW)
Button(root, text="Reset", command=lambda:Reset()).grid(row=4, column=0, sticky=NSEW)

Photo = ImageTk.PhotoImage(Image.open("Happyface.png"))
label = Label(root, image=Photo).grid(row=6, column=0)


root.mainloop()

