"""THIS PROGRAM CREATES A USER PROFILE AND SIMPLY PRINTS IT INTO A TXT FILE"""

from pip._vendor.distlib.compat import raw_input
class User():
    '''simulates a user for a social network or pc'''
    def __init__(self, first_name, last_name, username, location, *interests):
        '''initialize attributes of user class'''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.location = location.title()
        self.interests = interests


    @classmethod
    def get_userinfo(cls):
        '''creates a variable to store user inputs that correspond to User attributes'''
        first = raw_input("Welcome. PLease Enter Your First Name: ")
        last = raw_input("Please Enter Your Last Name: ")
        user = raw_input("Username: ")
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
        return cls(first, last, user, location, interests)
        """cls fills in the attributes that would go inside of a given User instance"""
        
        
    def write_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write('First Name: {}\n'.format(self.first_name))
            file.write('Last Name: {}\n'.format(self.last_name))
            file.write('Username: {}\n'.format(self.username))
            file.write('Location: {}\n'.format(self.location))
            file.write('Interests:\n')
            for i in self.interests:
                print(i)
            for i in self.interests:
                file.write("\n\t- {}\n\n".format(str(i)))
                
                
                
                
                
                
                
                
                
                   

