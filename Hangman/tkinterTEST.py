import tkinter as tk 

rootWin = tk.Tk()

rootWin.geometry("600x600")
rootWin.title('Hangman')


label = tk.Label(rootWin, text="Welcome, you have 1 head, 1 torso, 2 arms, 2 legs.\n Which means you have 6 lives , you loose one at each wrong guess.", font=('Arial',18))
#pakc the label in the window
label.pack(padx=20,pady=20)
# text box 
textbox = tk.Text(rootWin, height=1, width=1, font=('Arial', 16), bg="grey").pack()


button = tk.Button(rootWin,text="send guess", font=('Arial',16,'bold')).pack()

# entery from the user 


