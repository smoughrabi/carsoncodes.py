#code is inspired by the following article: Iwunor, C. (2022, April 24). A simple tip calculator application with Tkinter (python Gui). Medium. Retrieved September 18, 2022, from https://medium.com/@951985/a-simple-tip-calculator-application-with-tkinter-python-gui-eb822f704a1a

import tkinter as tk

#to ensure amount entered by a user is a number
def get_bill_total():
    entered_bill_total = user_input.get()
    #try and except block to handle exceptions and check if user entered a number
    try:
        bill_total = float(entered_bill_total)
    except ValueError:
        textbox.config(fg='#f40257',bg='#f7e2d1',padx=0,font=('Helvetica',12,'bold'))
        textbox['text'] = 'incorrect value entered'
        return
    final_tip = calculate_tip(bill_total)
    textbox.config(fg='#008037',bg='#f7e2d1',padx=0,font=('Helvetica',12,'bold'))
    textbox['text'] = 'QAR ' + str(final_tip)

#function to calculate tip
def calculate_tip(total):
    if total > 100:
        tip = float(total*20/100)
    elif total > 0 and total <= 100:
        tip = float(total*10/100)
    return tip

#creating a tkinter window
gui = tk.Tk()
gui.geometry("300x200")
gui.title('Tip Calculator')

#adding background color
gui['background']='#f7e2d1'

#adding labels
label= tk.Label(text = "Enter bill total:",bg='#f7e2d1',font=('Helvetica',12,'bold'))
label.place(x=10, y=20, height= 30)
#fg='#f40257'
#label.config(bg= '#f40257', padx=0)

#label2= tk.Label(text = "Enter %:",bg='#f7e2d1',font=('Helvetica',12,'bold'))
#label2.place(x=10, y=60, height= 30)

label3 = tk.Label(text = "Your tip is:")
label3.place(x= 10, y= 140)
label3.config(bg='#f7e2d1',padx=0)

#adding user input boxes
user_input = tk.Entry(text = "  ")
user_input.place(x=100, y= 20, width= 70, height = 30)

#user_input2 =tk.Entry(text = " ")
#user_input2.place(x=100, y= 60, width= 70, height = 30)


button = tk.Button(text = 'Calculate Tip', command = get_bill_total)
button.place(x =10, y=80, width=100, height=35)
button.configure(highlightbackground='#f7e2d1',font=('Helvetica',12,'bold'))

#adding a textbox to display output
textbox = tk.Message(text= 'QAR 0.00', width=200, font='21')
textbox.config(fg='#008037',bg='#f7e2d1',padx=0,font=('Helvetica',12,'bold'))
textbox.place(x=10, y= 165)

gui.mainloop()
