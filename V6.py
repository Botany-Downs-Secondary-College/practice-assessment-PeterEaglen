from tkinter import *
import tkinter as tk
root = tk.Tk()

#Defining variables so tehy are global
Username = StringVar()
Password = StringVar()#Uses makes the label variable stay as a string, so it is then later converted
CreateUser =  StringVar()#(Only way I could make password work)
CreatePass =  StringVar()
ConfCreatePass =  StringVar()
frame1 = Frame(root)
frame2 = Frame(root)#Defining the frames and connecting them with root
frame3 = Frame(root)

SignInOptions = [["Peter", "abc123"], ["AdamR", "123abc"], ["Seyorn", "ABC123"], ["Chris", "123ABC"]]#List of possible passwords
SignInResponse =[]#List that will have their username and password once put in

def ConfirmPass():
    CreateUsername = CreateUser.get()#Changes the label variable to a variable that can be used in the if tag
    CreatePassword = CreatePass.get()
    ConfirmPassword = ConfCreatePass.get()
    if len(CreateUsername) >= 5 and len(CreatePassword) >= 5: #Makes sure the password is more than 5 charcters long
        if CreatePassword == ConfirmPassword:
            Main() # If the passwords match, the account will be created, so it can be logged in with, and will send the user to main screen
            SignInOptions.insert(0, [CreateUsername, CreatePassword])#Adds their username to the list in the first position, so it can be done as often as the user wants without breaking
        else:
            NotMatchingPass = Label(frame3, fg = "red", padx = 120, text = "Those passwords don't match! Try again.", font= ("Times", "12"))   #If the passwords don't match, it tells the user under the confirm password text box
            NotMatchingPass.grid(row = 7, column = 2)     
    else:
        NoUser = Label(frame3, fg = "red", text = "Please enter a valid username or password (must be more than 5 characters)", font= ("Times", "12"))   #If the username or password is less than 5 charcters, a message under the confirm password text box tells them so.
        NoUser.grid(row = 7, column = 2)           

def CheckPass():
    Passwrd = Password.get()#Changes the label variable to a variable that can be used in the if tag
    Usernme = Username.get()
    SignInResponse.insert(0, [Usernme, Passwrd]) #Adds their response (username and passsword), to the SignInResponse list. This way we can find out if it is in the SignInOptions (already made accounts). 
    print(len(SignInOptions))    
    if len(SignInOptions) <= 4:
        if SignInResponse[0] == SignInOptions[0]:
            Main()#If username and password are right send to main screen
        elif SignInResponse[0] == SignInOptions[1]:
            Main()   
        elif SignInResponse[0] == SignInOptions[2]:
            Main()    
        elif SignInResponse[0] == SignInOptions[3]:
            Main()    
        else:
            WrongPass = Label(frame2, fg = "red", text = "Your username or password is incorrect! Try again.", font= ("Times", "12"))   
            WrongPass.grid(row = 5, column = 2) 
    elif len(SignInOptions) == 5:
        if SignInResponse[0] == SignInOptions[0]:
            Main()
        elif SignInResponse[0] == SignInOptions[1]:
            Main()   
        elif SignInResponse[0] == SignInOptions[2]:
            Main()    
        elif SignInResponse[0] == SignInOptions[3]:
            Main()         
        elif SignInResponse[0] == SignInOptions[4]:
            Main()       
        else:
            WrongPass = Label(frame2, fg = "red", text = "Your username or password is incorrect! Try again.", font= ("Times", "12"))   
            WrongPass.grid(row = 5, column = 2)     
    else:   
        if SignInResponse[0] == SignInOptions[0]:
            Main()
        elif SignInResponse[0] == SignInOptions[1]:
            Main()   
        elif SignInResponse[0] == SignInOptions[2]:
            Main()    
        elif SignInResponse[0] == SignInOptions[3]:
            Main()         
        elif SignInResponse[0] == SignInOptions[4]:
            Main()       
        elif SignInResponse[0] == SignInOptions[5]:
            Main()
        else:
            WrongPass = Label(frame2, fg = "red", text = "Your username or password is incorrect! Try again.", font= ("Times", "12"))   
            WrongPass.grid(row = 5, column = 2)         
def Main ():
    global frame1
    frame2.grid_remove()#removes the other frames
    frame3.grid_remove()
    frame1 = LabelFrame(root, bg = "light blue", height = 300)#Makes the background of teh frame light blue
    frame1.grid(row=0, column = 0)
    
    TitleLabel = Label (frame1, bg = "light blue", fg = "black", width = 27, padx = 30, pady = 10, text = "Welcome to Your Password Manager", font= ("Times", "25", "bold"))   #tells the user they are into their password manager 
    TitleLabel.grid(columnspan = 5)  
    
    button1 = Button(frame1, text = "Add a Password", font =("bold", "20"), bg = "white", pady= 10, anchor = W) #Takes the user to their add a passowrd screen, where they can add a new password
    button1.grid(row = 1, column = 2)  #defining where it is positioned
    ""
    button2 = Button(frame1, text = "View Passwords", font =("bold", "20"), bg = "white", pady= 10, anchor = W)  #Takes the user to a screen where they can view all of the passwords
    button2.grid(row = 2, column = 2)  #defining where it is positioned
    ""
    button3 = Button(frame1, padx = 46, text = "Sign Out", font =("bold", "20"), bg = "white", pady= 10, anchor = W, comman = SignIn)  #A sign out button that takes them to the first screen
    button3.grid(row = 3, column = 2) #defining where it is positioned


def SignIn():
    global frame2
    frame2 = LabelFrame(root, height = 300)
    frame2.grid(row=0, column = 0)
    frame3.grid_remove()
    frame1.grid_remove()#Removes frame 1 (when signing out)
    
    TitleLabel = Label(frame2, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "Sign In To your Account", font= ("Times", "25", "bold"))#All the title attributes
    TitleLabel.grid(columnspan = 5)#Setting the column span for the page
    
    User = Label(frame2, text = "Username", padx = 20, font =("bold", "14"), pady= 10)#text that says usename above the entry box for the username to be entered
    User.grid(row = 1, column = 2)            #defining where it is positioned
    
    UserBox = Entry(frame2, width = 20, textvariable = Username, font =("12"))#Where the user puts in their username
    UserBox.grid(row = 2, column = 2) #defining where it is positioned
    
    Pass = Label(frame2, text = "Password", padx = 20, font =("bold", "14"), pady= 10)
    Pass.grid(row = 3, column = 2)                  #defining where it is positioned        
    
    PassBox = Entry(frame2, show = "*", textvariable = Password, width = 20, font =("12")) #The entry box for the password, which displays '*' so no one can see what is being typed.
    PassBox.grid(row = 4, column = 2)  #defining where it is positioned    
    
    SignIn = Button(frame2, text = "Sign In", padx = 20, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = CheckPass)   #Creating the sign in button, that sends it to the check pass function
    SignIn.grid(row = 6, column = 2)  #defining where it is positioned
    
    Create = Label(frame2, text = "If you don't already have an account", padx = 20, font =("bold", "11"), pady= 10)  #Lets the user know they can create an account if they dont have one already. - text
    Create.grid(row = 7, column = 2)    #defining where it is positioned           
                   
    CreateAccount = Button(frame2, text = "Create Account", font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = NewAccount)  #Button that takes them to a screen where they can craete a new account
    CreateAccount.grid(row = 8, column = 2)  #defining where it is positioned
    
        

def NewAccount():
    global frame3
    frame3 = LabelFrame(root, height = 300)
    frame3.grid(row=0, column = 0)
    frame2.grid_remove()#removes frame 2 (When user clicks create account and changes from sign in screen to the create account screen)
    
    TitleLabel = Label(frame3, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "Create your Account", font= ("Times", "25", "bold"))#All the title attributes
    TitleLabel.grid(columnspan = 5)#Setting the column span for the page
    
    User = Label(frame3, text = "Username", padx = 20, font =("bold", "14"), pady= 10)#text that says usename above the entry box for the username to be entered
    User.grid(row = 1, column = 2)            #defining where it is positioned
    
    UserBox = Entry(frame3, width = 20, textvariable = CreateUser,font =("12"))#Where the user puts in their username
    UserBox.grid(row = 2, column = 2) #defining where it is positioned
    
    CPass = Label(frame3, text = "Password", padx = 20, font =("bold", "14"), pady= 10)
    CPass.grid(row = 3, column = 2)                  #defining where it is positioned        

    CPassBox = Entry(frame3, show = "*", width = 20, textvariable = CreatePass, font =("12")) #The entry box for the password, which displays '*' so no one can see what is being typed.
    CPassBox.grid(row = 4, column = 2)  #defining where it is positioned
    
    ConfPass = Label(frame3, text = "Confirm Password", padx = 20, font =("bold", "14"), pady= 10)
    ConfPass.grid(row = 5, column = 2)                  #defining where it is positioned        

    ConfPassBox = Entry(frame3, show = "*", width = 20, textvariable = ConfCreatePass, font =("12")) #The entry box for the password, which displays '*' so no one can see what is being typed.
    ConfPassBox.grid(row = 6, column = 2)  #defining where it is positioned
    
    SignIn = Button(frame3, text = "CreateAccount", padx = 20, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = ConfirmPass)   #Creating the sign in button, that sends it to the check pass function
    SignIn.grid(row = 8, column = 2)  #defining where it is positioned

SignIn()

root.title("Password manager")
root.geometry("+400+10")


root.mainloop()