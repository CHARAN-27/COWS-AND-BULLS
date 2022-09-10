# importing modules from python library
from tkinter import *
import random as r
import tkinter.messagebox as m

# generating random 4 digit integer 
a= r.myRandom()

# setting counter as 0
counter =0

# Making a graphic window 1
root=Tk()

#creating geometry of (400*400)
root.geometry("400x200")

root.configure(background="#36454F")

# Applying label to window 1
Label(root, text='Cows and bull Game', fg="#fff0f5", bg = "#36454F",  font=('Times New Roman','33','bold')).place(x=0,y=0)

# Applying Entry Widget to get info of game player
name=Entry(root, font=('Courier','25','bold'), width=15)
name.insert(0,'Enter your name')
name.place(x=50,y=60)

# defining onclick function that makes new graphic window when button 'Submit' is pressed.
def onclick():

    button1['state'] = DISABLED
    # Making graphic window 2
    root1=Tk()
    root1.geometry("1100x400")
    root1.configure(background='#36454F')

    # defining a function rules which talk about the rules of game.
    def rules():
        b1['state']=DISABLED
        # provding rules as labels.
        Label(root1, text='This is version 1.0 of cows and bull game.\nRules of this game are:', font=('Times New Roman','13','bold')).place(x=425,y=100)
        Label(root1, text='1.  Computer will generate a random 4 digit number. \n 2.  user need to type 4 digit number based on his guess.\n3.  if correct number falls at right place then user is awarded with one cow for every guess \n 4.  else if the correct digit of number falls at wrong place he will be awarde with bull \n 5.  when user get the number correctly (i.e cows = 4 and bull = 0) the computer will show number of attemps made by him.', font=('Times New Roman','15','bold')).place(x=30,y=150)

        # defining the function game_start that starts game when user is ready.
        def game_start():
            b2['state']= DISABLED

            # makes graphic window 3 that has game inside it
            root2 = Tk()
            
            root2.configure(background ='#36454F' )

            # Generate title of the window 3
            root2.title("COWS AND BULLS GAME")

            # game
            def callback(a,b):

                # setting counter as global to avoid to avoid unbounded local error.
                global counter

                #incrementing count each time the function runs
                counter = counter+1

                # initialising cow and bull as zero
                cow=0
                bull=0

                # passing the parameters into for loop that counts for cow and bull
                for i in range(0,4):
                    if(a[i]==b[i]):
                        cow+=1
                    elif(b[i] in a):
                        bull+=1
                # printing details about cow and bull
                Label(root2, text='Cows are '+ str(cow) +' and bulls are ' + str(bull)).pack()

                # if cow = 4 then user wins the game and Congratulation message box is shown.
                if(cow==4):
                    m.showinfo('INFO', 'Congratulations '+ name.get()+' You guessed the number correctly in '+ str(counter)+' Attemps')
                    root2.destroy()
                    root1.destroy()
                    root.destroy()
                    return
                # else the function calls guess function. 
                else:
                    guess()

            # Guess function takes value from user and validate it and pass it in recursion function as parameter.
            def guess():
                num=Entry(root2, width=20)
                p=num.get()
                num.pack()
                def Submit_button():
                    b3['state'] = DISABLED
                    if(len(str(num.get()))==4):
                        # for i in range(4):
                        #     for j in range(i+1,4):
                        #         if(str(num.get()[i]==str(num.get()[j]))):
                        #             m.showerror("ERROR","Do not Duplicate the digits")
                        #             guess()
                        #         else:
                        #             Label(root2, text =a , fg = "#36454F").pack()
                        #             recursion(a,num.get())
                        if(str(num.get())[0] in [str(num.get())[1],str(num.get())[2],str(num.get())[3]] or str(num.get())[1] in [str(num.get())[0],str(num.get())[2],str(num.get())[3]] or str(num.get())[2] in [str(num.get())[1],str(num.get())[0],str(num.get())[3]] or str(num.get())[3] in [str(num.get())[1],str(num.get())[2],str(num.get())[0]] ):
                            m.showerror("ERROR","Do not Duplicate the digits")
                            guess()
                        elif(str(num.get()).isnumeric()==False):
                            # show error messagebox if any error.
                            m.showerror('ERROR', 'Please Enter 4 digit number only')
                            guess()
                        else:
                            Label(root2,text=a, fg = "#36454F").pack()
                            callback(a,num.get())
                    else:
                        m.showerror('ERROR', 'Please Enter 4 digit number only')
                        guess()
                    
                b3=Button(root2, text="Submit", command=Submit_button, width=20)
                b3.pack()

            # calls the guess function
            guess()

            # keep window 3 looping
            root2.mainloop()

        # create button for game_start function
        b2 = Button(root1, text='Click here to start the game', command=game_start)
        b2.place(x=450,y=290)

    Label(root1, text='Hello ' + name.get(), font=('Times New Roman','30','bold'), fg="#fff0f5", bg = "#36454F").place(x=330,y=0)

    #create button for rules function
    b1=Button(root1, text='Click here to continue', command= rules)
    b1.place(x=440,y=50)

    # keep looping window 2
    root1. mainloop()

# create button for onclick function
button1 = Button(root, text='Submit', width=20, command=onclick, borderwidth=3)
button1.place(x=105,y=120)

# looping window 1
root.mainloop()