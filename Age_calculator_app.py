from PIL import Image,ImageTk
import datetime
import Tkinter as tk

class Person:
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate
    def age(self):
        today=datetime.date.today()
        age = today.year-self.birthdate.year-1
        return age
    
def calculate_age():
    person=Person("Dev Sanghvi",datetime.date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get())))
    text_answer=tk.Text(master=window,height=20,width=30)
    text_answer.grid(column=1,row=5)
    answer_text = "{name} is {age} years old".format(name=person.name,age=person.age())
    text_answer.insert(tk.END,answer_text)

#create frame
window=tk.Tk()

#create frame geometry
window.geometry("400x400")

#set the title of the frame
window.title("Age calculator App")

image=Image.open("C:/Users/devsa/Desktop/age_calculator.png")
image.thumbnail((100,100), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)

#adding Labels
year_label=tk.Label(text="Year")
month_label=tk.Label(text="Month")
day_label=tk.Label(text="Date")

year_label.grid(column=0,row=1)
month_label.grid(column=0,row=2)
day_label.grid(column=0,row=3 )

year_entry=tk.Entry()
month_entry=tk.Entry()
day_entry=tk.Entry()

year_entry.grid(column=1,row=1)
month_entry.grid(column=1,row=2)
day_entry.grid(column=1,row=3)

calculate_button=tk.Button(text="Calculate your Age!!!",command=calculate_age)
calculate_button.grid(column=1,row=4)

window.mainloop()
                

#print dev.name
#print dev.birthdate
#print dev.age()
