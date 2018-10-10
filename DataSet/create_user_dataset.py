"""THIS PROGRAM CREATES A USER AND SIMPLY STORES ITS INFO IN A TXT FILE TO BE RE-READ BY PYTHON"""

from pip._vendor.distlib.compat import raw_input
import json
from tkinter import *


class User():
    '''simulates a user for a social network or pc'''
    def __init__(self, first_name, last_name, username, password, location, *interests):
        '''initialize attributes of user class'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.password = password
        self.location = location.title()
        self.interests = interests
        
    '''TKINTER'''#######################
    @classmethod
    def create_window(cls):
        root = Tk()
        root.configure(background="gray15")
        root.title("Robles Network")
        
        '''PAGE TITLE'''
        welcome_label = Label(root, text="Welcome to this Network", font=("BankGothic Md BT", 30), fg="Deep Sky Blue", bg="gray15")
        welcome_label.grid(row=1, column=2)
        
        '''PAGE EXPLANATION'''
        explain_label = Label(root, text="Hello. This network is a simple attempt so simulate data storage" + 
                                   " and account management of social networks or simple user interface functions.\n" + 
                                   " It models a user creating an account and being able to sign in to that account.",
                                   font=("Arial Rounded MT Bold", 12), bg="gray15", fg="white")
        explain_label.grid(row=2, column = 2)
        
        '''LOGIN LABELS'''
        first_name_label = Label(root, text="Username: ", bg="gray15", fg="white", font=("BankGothic Md BT", 12), anchor=E)
        first_name_label.grid(row=3, column=0)
        
        last_name_label = Label(root, text="Password: ", bg="gray15", fg="white", font=("BankGothic Md BT", 12), anchor=E)
        last_name_label.grid(row=4, column=0)
        
        '''LOGIN INPUTS'''
        first_name_entry = Entry(root)
        last_name_entry = Entry(root)
        first_name_entry.grid(row=3, column=1)
        last_name_entry.grid(row=4, column=1)
        
        '''LOGIN/SIGN UP BUTTONS'''
        login_button = Button(root, text="Log In", font=("BankGothic Md BT", 12), bg="Deep Sky Blue", fg="white")
        login_button.grid(row=6, columnspan=2, ipadx=60)
        
        or_label = Label(root, text="OR", font=("BankGothic Md BT", 16), fg="white", bg="gray15")
        or_label.grid(row=7, columnspan=2)
        
        sign_up_button = Button(root, text="Sign Up", font=("BankGothic Md BT", 12), bg="Deep Sky Blue", fg="white")
        sign_up_button.grid(row=8, columnspan=2, ipadx=52)
        
        root = mainloop()


    @classmethod
    def get_userinfo(cls):
        '''creates a variable to store user inputs that correspond to User attributes'''
        first = raw_input("Welcome. PLease Enter Your First Name: ")
        last = raw_input("Please Enter Your Last Name: ")
        user = raw_input("Username: ")
        password = raw_input("Password must be 8 characters long, include a Capital Letter, and one of the following: '!@#$%^&*'" + 
                             "\nEnter your desired password: ")
        active = True
        while active:
            chars = "!@#$%^&*"
            if len(password) > 8 and any((c in chars) for c in password) and any(c.isupper() for c in password):
                break
            else:
                print("\nPassword must be 8 characters long, include a Capital Letter, and one of the following: '!@#$%^&*'")
                password = raw_input("Enter your desired password: ")
            
        
        location = raw_input("What is your location? : ")
        interests = []
        
        print("List some of your interests (Press 'Q' Key to End Program.)")
        
        active = True
        while active:
            '''infinite loop that creates elements in a list until user quits'''
            interest = input().strip()
            if interest == 'q':
                active = False
            else:
                interests.append(interest)
                print("Press 'Q' Key to End Program.")
        return cls(first, last, user, password, location, interests)
        """cls fills in the attributes that would go inside of a given User instance"""
        
    def to_json(self):
        '''returns the info that is dumped into the file'''
        return json.dumps({"first": self.first_name, "last": self.last_name, "username": self.username,
                               "password": self.password, "location": self.location, "interests": self.interests})
                
                
    @classmethod            
    def from_json(cls, j):
        dct = json.loads(j)
        cls(dct["first"], dct["last"], dct["username"], dct["password"], dct["location"], dct["interests"])
            

  
