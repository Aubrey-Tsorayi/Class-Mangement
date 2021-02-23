import login

def login(username,password):

    while True:
        choice = eval(input('1. Create account 2. Login 3. Quit : '))
        if choice == 1:
            username = input('Create username: ')
            password = input('Create password: ' )

            def password_check(password): 
    
                SpecialSym =['$', '@', '#', '%'] 
                val = True
    
                if len(password) < 6: 
                    print('length should be at least 6') 
                    val = False
        
                if len(password) > 20: 
                    print('length should be not be greater than 8') 
                    val = False
        
                if not any(char.isdigit() for char in password): 
                    print('Password should have at least one numeral') 
                    val = False
        
                if not any(char.isupper() for char in password): 
                    print('Password should have at least one uppercase letter') 
                    val = False
        
                if not any(char.islower() for char in password): 
                    print('Password should have at least one lowercase letter') 
                    val = False
        
                if not any(char in SpecialSym for char in password): 
                    print('Password should have at least one of the symbols $@#') 
                    val = False
                if val: 
                    return val 

 
            def main(): 
                passwd = password
    
                if (password_check(passwd)): 
                    database.add_user(username,password)
                    print('Account created')
                else: 
                    print("Invalid Password !!") 
        
    
        if __name__ == '__main__': 
                 main() 

        elif choice == 2:
            database.login()
            print("Login succees")
            break
        elif choice == 3:
            print("////////////////////////////")
            print("       Thank you            ")
            print("////////////////////////////")
        break


