# Administrator accounts list
def getCreds():
    
    # Prompt the user for their username and store it in a variable called username
    username = input("What's your username? ")
   
    # Prompt the user for their password and store it in a variable called password
    password = input("what's your password?")
    
    return {"username": username, "password": password}
    # Create a dictionary that will store username and password combinations.
    user_info = [
    {
        "username": username,
        "password": password
    },
    {
        "username": username,
        "password": password
    }
]

    # Return the above list (called user_info)
 
  
    

adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
    ]

getCreds()
# Build your login functions below

def checkLogin(user_info, adminList):
    for admin in adminList:

        if(admin["username"] == user_info["username"] and admin["password"] == user_info["password"]):
            
                
            return True
                    
    return False



LoggedIn = False

while(LoggedIn == False):
    user = getCreds()

    LoggedIn = checkLogin(user, adminList)

    print("--------------")

print("YOU HAVE LOGGED IN!")
