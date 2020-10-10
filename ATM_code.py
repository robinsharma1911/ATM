
#accounts dict contains:-
    #keys as account no's of two persons and value[0] as pins and value[1] as balance
accounts = {822466:[1234,20000],822456:[2345,30000]}


#main function after authentication
def main_function(account_number, accounts):
    while True:
        amt = accounts[account_number][1]           #save balance of current user in amt variable
        #check balance
        def check_balance(account_number, amt):
            print('account number:-',account_number,'\ntotal balance:-',amt)
        #withdraw balance
        def withdraw(account_number, amt): 
            withdraw_amt = int(input('\nenter amount for withdraw:-'))
            amt=amt-withdraw_amt
            print('\nafter withdraw remaining balance:-',amt)                                         
            accounts[account_number][1] =amt                             #update dict balance at run time
            print(accounts)
         
        print(                                                           #choose  options
            '\nchoose option'
            '\n 1)check balance'
            '\n 2)withdraw'
            '\n 3)exit\n'
        )
        select = int(input('choice:-'))
        if select == 1:
            check_balance(account_number, amt)
        elif select == 2:
            withdraw(account_number, amt)
        elif select == 3:
            exit()
        else:
            print('\nwrong choice try again')



#function to authenticate user account number and pin..
def authentication():
    account_number = int(input('enter account number:-'))                #___take input from user for account no. and pin....
    pin = int(input('enter pin:-'))

    for acc, pins in accounts.items():
        if account_number == acc:
            if pin == pins[0]:
                amt = pins[1]
                main_function(account_number,accounts)                    #call main_function after successful authenticate a person...
            else:
                print('wrong credentials')
                authentication()


#program starts here...
authentication()