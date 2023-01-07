import random,math
import datetime
import sys

try:
    
    class Bank_account:
        acc_num = ""

        def __init__(self):
            self.balance = 0
        
            greeting = "Welcome to Bank Of India"
            print(greeting.center(70,'*')) 
        
        def Create_acc(self):
            print("Please Enter your details for Proceed further :")
            self.name =input('Enter Your Name : ').capitalize()
            self.email = input('Enter Your Email : ').casefold()            
            date_of_birth =input('Enter your birth date [dd/mm/yyyy] :  ')
            self.age = int(input('Enter Your Age : '))
            self.mobile_no = int(input('Enter your mobile no : '))
            adhar_num = int(input("Enter your adhar number : "))
            account_num = self.randomNumber(16)
            print(f"Congratulation your Account created Successfully .... Your account number is={account_num}")
            self.acc_num = account_num
            print('-'*70)
            acc_type = input ("Enter which type of account do you want to open [saving/current] : ").casefold()
            if acc_type =='saving':
                print("RECHARGE WITH MINIMUM 500 RS. FOR OPENING SAVING ACCOUNT")
            elif acc_type =='current':
                print("RECHARGE WITH MINIMUM 1000 RS. FOR OPENING CURRENT ACCOUNT")
            else:
                print('Invalid Input....Try again with available options')
            self.a_type =acc_type
            print('-'*70)
            opening_amt =float(input("Enter The Initial amount(>=500 for Saving and >=1000 for current : "))
            self.balance += opening_amt
            print('-'*70)

            pwd = input("Create strong password containig uppercase,lowercase ,symbol,and number in combination[Abc@123] = ")
            conf_pwd= input("Confirm Your Password = ")
            if conf_pwd == pwd:
                with open(f"D:\\bank_project\\login_acc.txt", 'w') as f:
                    f.write(self.email + "\n")
                    f.write(pwd + "\n")
                    f.write(str(account_num))
                f.close()
            else:
                print("Password is not same as above! \n")
        
        def login(self):
            print('-'*50)
            print("*****LOGIN TO ENTER*****")
            print("-"*50)
            Email =input("enter your email address = ")
            password =input("enter your password = ")
            account_no = self.acc_num
            with open(f"D:\\bank_project\\login_acc.txt",'r') as f:
                Save_Email, Save_password,save_account_no = f.read().split("\n")
                f.close()

                if Email == Save_Email and password ==Save_password :
                    print("\t\t\t****LOGGED IN SUCCESSFULLY**")
                    print('-'*50)
                    
                    while True:
                        print(f"\t MAIN MENU LIST \n \
                            \t1)SHOW ACCOUNT INFO \n \
                            \t2)DEPOSIT MONEY \n \
                            \t3)WITHDRAW MONEY \n \
                            \t4)SHOW LAST FIVE TRANSACTION \n \
                            \t5)DISPLAY BALANCE \n \
                            \t6)EXIT")
                        
                        choice = int(input("Pick an option [1/2/3/4/5/6]= "))
                        if choice == 1:
                            obj.Show_Acc_Info()
                            print("\t\t\t\tWelcome to the Bank of India Family ........")
                            print('-'*70)
                        elif choice == 2:
                            obj.Deposit()
                            print("Thank you for crediting in our bank...") 
                            print('-'*70)    
                        elif choice == 3:
                            obj.Withdrawal() 
                            print("Thank you...") 
                            print('-'*70)    
                        elif choice == 4:
                            print("The last five transactions: ")
                            try:
                                with open(f'D:\\bank_project\\transaction_list.txt',mode='r',encoding='utf-8') as file:
                                    for line in (file.readlines()):
                                        print(line, end ='')
                            except BaseException as ex:
                                print(f"Problem Occurred = {ex}")
                            print('-'*70)
                        elif choice == 5:
                            obj.DisplayBal()
                            print('-'*70)

                        elif choice == 6:
                            print("Thanks for using the program")
                            sys.exit()
                        else:
                            print('input valid choice')
                else:
                    print("login failed try again")

        def randomNumber(self,n:int):
            min = math.pow(10,n-1)
            max = math.pow(10,n)-1
            self.n=n
            return random.randint(min,max)

        def Show_Acc_Info(self):
            print(f'\n 1]Account No : {self.acc_num}')
            print(f'\n 2]Account holder Name : {self.name}')
            print(f'\n 3]Email Id of Account holder : {self.email}')
            print(f'\n 4]Type Of Account  : {self.a_type}')
            print(f'\n 5]Balance of Account : {self.balance}')

        def Show_balance (self):
            print(f'Available Balance in Account : {self.balance}')

        def Deposit(self):
            amt = float(input("Enter amount to be deposited : "))
            self.balance+=amt 
            print(f"{amt} Rs. credited successfully in your bank account {self.acc_num} \n \
                 available balance is {self.balance}") 
            self.transaction(f"Deposit : {amt} amount credited at {datetime.datetime.today().replace(microsecond=0)}") 

        def Withdrawal(self):
            amt = float(input("Enter amount to be withdraw : "))
            self.balance-=amt 
            print(f"{amt} Rs. debited successfully from your bank account {self.acc_num} \n \
                 available balance is {self.balance}") 
            self.transaction(f"Withdraw : {amt} amount debited at {datetime.datetime.today().replace(microsecond=0)}")

        def transaction(self,trans):
            with open('D:\\bank_project\\transaction_list.txt',mode='w',encoding='utf-8') as file:
                file.write(f"{trans} \t\t\t Available Balance: {self.balance} \n")
        
        def DisplayBal(self):
            print('Your updated balance is : ',self.balance)
            with open('D:\\bank_project\\transaction_list.txt',mode='r',encoding='utf-8') as file:
                print(file.read())

        
    def intro():
        print("\t\t\t\t***************************")
        print("\t\t\t\tBANK MANAGEMENT SYSTEM")
        print("\t\t\t\t***************************")
        print("\t\t\t\tBrought To You By:")
        print("\t\t\t\tBhakti Suryawanshi")
        input("Press Enter To Continue : ")
                    
    if __name__=="__main__":
        obj = Bank_account()
        intro()
        while True:
            print("\tMENU LIST")
            print("\t1]. CREATE ACCOUNT")
            print("\t2]. LOGIN")
            print("\t3]. EXIT")
            chc = int(input("Enter your choice [1/2/3] = "))
            if chc ==1:
                obj.Create_acc()
                obj.Show_Acc_Info()
            elif chc ==2:
                obj.login()
            elif chc== 3:
                print("\nThank You For Using Our App ! . . . .")
                sys.exit()
            else:
                print("Please Enter a Valid Choice !")

except BaseException as ex:
    print(f"<<<ERROR>>>{ex}")

finally:
    print("Thank you very much for using banking system......")