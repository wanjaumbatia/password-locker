import random 
# This is an application
users=[] 
credentials=[]

class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password

class Credentials: 
    def __init__(self, site ,username, password):
        self.site=site
        self.username=username
        self.password=password
    def new():
        print("Select an option to continue")
        print("1.New credentials\n2.Existing credentials\n3.View credentials\n4.Delete credentials")
        option=input()
        if option=="1":
            site=input("Enter site name: ")
            username=input("Enter username: ")
            print("Do you want the application to generate you a password?\n1.Yes\n2.No")
            selection=input()
            if selection=="1":
                password=str(random.randint(1000000,9999999))
            elif selection=="2":
                password=input("Enter password: ")
            else:
                print("Invalid option")
            credential=Credentials(site, username, password)
            credentials.append(credential)
            print("Added successfully")
            Credentials.new()
        elif option=="2":
            site=input("Enter site name: ")
            username=input("Enter username: ")
            password=input("Enter password: ")
            credential=Credentials(site, username, password)
            credentials.append(credential)
            print("Added successfully")
            Credentials.new()
        elif option=="3":
            for x in credentials:
                print("Site name: " + x.site)
                print("username: " + x.username)
                print("password: " + x.password)
            Credentials.new()
        elif option=="4":
            print("Enter the name of the site you want to delete: ")
            name=input()            
            for i, o in enumerate(credentials):
                if o.site== name:
                    del credentials[i]
            Credentials.new()
        else:
            print("Invalid option")


class Main:
    
    def register():
        print("Create new account")
        username=input("Enter username: ")
        password=input("Enter new password: ")
        c_password=input("Confirm your password: ")
        if password==c_password:
            user=User(username,password)
            users.append(user)
            Main.login()

        else:
            print("passwords do not match")
            Main.register() 
            
    def login():
        print("Login to your account")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for x in users:
            if x.username==username and x.password==password:
                Credentials.new()
            else:
                print("Invalid login attempt")
                Main.login()


            

    def navigate (x):
        if x=="1":
            Main.register()
        elif x=="2":
            print("Login")
        elif x=="3":
            exit()
        else:
            print ("invalid password")
    
print ("Welcome to Password Locker")
print ("Select an option to continue")
print ("1.Register\n2.Login\n3.Exit") 
option=input()
Main.navigate(option)