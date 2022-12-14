#class to perform account actions
class Account:
    def __init__(self, name):
        self.name = name
        self.balance= 0
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount
    
    def show_balance(self):
        print(self.name,'',self.balance)

#dict to store the accounts
accounts={}

#check whether account exists
def check_exists(id):
    if id.lower() in accounts.keys():
        return True

#the command loop
while True:
    command = input()
    if command== "":
        # print(accounts)
        print("Thank you for banking with us!!")
        break
    else:
        command=command.split()
        try:
            if len(command)<=3:
                id= command[1].lower()
                if len(command)==3:
                    amount = command[2]
                command = command[0]

                if command.lower() == "create":
                    if check_exists(id)!=True:
                        accounts[id]= Account(amount)
                    else:
                        print("Account with given name already exists")
                
                elif command.lower() == "deposit":
                    try:
                        amount=int(amount)
                    except:
                        print("Enter valid amount in numbers")
                    if check_exists(id):
                        accounts[id].deposit(amount)
                    else:
                        print("Account with given name does not exist")
                    
                elif command.lower() == "withdraw":
                    try:
                        amount=int(amount)
                    except:
                        print("Enter valid amount in numbers")
                    if check_exists(id) :
                        if accounts[id].balance>= amount:
                            accounts[id].withdraw(amount)
                        else:
                            print("Insufficient balance:",accounts[id].balance )
                    else:
                        print("Account with given name does not exist")
                
                elif command.lower() == "balance":
                    if check_exists(id):
                        accounts[id].show_balance()
                    else:
                        print("Account with given name does not exist")
                
                else:
                    print("Invalid Command")
            else:
                print("Invalid Command")
        except:
            print("Invalid Command")

