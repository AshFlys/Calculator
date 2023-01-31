import tkinter as tk
field_text=""
def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
def calculate():
    global field_text
    result=str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0", "end")

window=tk.Tk()
window.title("Calculator")
window.geometry("280x275")
window.configure(bg='grey')
field=tk.Text(window,height=2,width=18,font=("Arial",20))
field.grid(row=1,column=1,columnspan=4)
field.configure(bg="blue")

# Number Buttons

button_1=tk.Button(window,text="1",bg="#3efffc", fg="black",command=lambda: add_to_field(1),width=5,font=("Arial",14))
button_1.grid(row=2,column=1)

button_2=tk.Button(window,text="2",bg="#3efffc", fg="black",command=lambda: add_to_field(2),width=5,font=("Arial",14))
button_2.grid(row=2,column=2)

button_3=tk.Button(window,text="3",bg="#3efffc", fg="black",command=lambda: add_to_field(3),width=5,font=("Arial",14))
button_3.grid(row=2,column=3)

button_4=tk.Button(window,text="4",bg="#3efffc", fg="black",command=lambda: add_to_field(4),width=5,font=("Arial",14))
button_4.grid(row=3,column=1)

button_5=tk.Button(window,text="5",bg="#3efffc", fg="black",command=lambda: add_to_field(5),width=5,font=("Arial",14))
button_5.grid(row=3,column=2)

button_6=tk.Button(window,text="6",bg="#3efffc", fg="black",command=lambda: add_to_field(6),width=5,font=("Arial",14))
button_6.grid(row=3,column=3)

button_7=tk.Button(window,text="7",bg="#3efffc", fg="black",command=lambda: add_to_field(7),width=5,font=("Arial",14))
button_7.grid(row=4,column=1)

button_8=tk.Button(window,text="8",bg="#3efffc", fg="black",command=lambda: add_to_field(8),width=5,font=("Arial",14))
button_8.grid(row=4,column=2)

button_9=tk.Button(window,text="9",bg="#3efffc", fg="black",command=lambda: add_to_field(9),width=5,font=("Arial",14))
button_9.grid(row=4,column=3)

button_0=tk.Button(window,text="0",bg="#3efffc", fg="black",command=lambda: add_to_field(0),width=5,font=("Arial",14))
button_0.grid(row=5,column=2)

# Operation Buttons

button_plus=tk.Button(window,text="+",bg="#76b314", fg="black",command=lambda: add_to_field("+"),width=5,font=("Arial",14))
button_plus.grid(row=4,column=4)

button_minus=tk.Button(window,text="-",bg="#76b314", fg="black",command=lambda: add_to_field("-"),width=5,font=("Arial",14))
button_minus.grid(row=5,column=4)

button_times=tk.Button(window,text="*",bg="#76b314", fg="black",command=lambda: add_to_field("*"),width=5,font=("Arial",14))
button_times.grid(row=3,column=4)

button_division=tk.Button(window,text="/",bg="#76b314", fg="black",command=lambda: add_to_field("/"),width=5,font=("Arial",14))
button_division.grid(row=2,column=4)

button_clear=tk.Button(window,text="clear",bg="#730011", fg="black",command=lambda: clear(),width=5,font=("Arial",14))
button_clear.grid(row=7,column=1)

button_equal=tk.Button(window,text="=",bg="#c4edf5", fg="black",command=lambda: calculate(),width=13,font=("Arial",14))
button_equal.grid(row=7,column=3,columnspan=2)

window.mainloop()