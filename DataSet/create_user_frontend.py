"""THIS PROGRAM CREATES INSTANCES OF USER AND STORES THEIR INFO IN A FILE"""
from create_user_dataset import User
from tkinter import *


userx = User

def create(user): 
    '''creates an instance of User object'''
    filename = r'''users.json'''

    with open(filename, 'a') as f:
        '''writes each attribute of User into a file'''
        x = user.create_window().get_userinfo().to_json()
        f.write(x + "\n")
    
        
create(userx)


'''if __name__ == "__main__":
    create()
    create(user1)'''


        
    
    



    



    

