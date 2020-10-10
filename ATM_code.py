accounts = {822466:[1234,2000],822456:[2345,3000]}

#check balance
def check_balance(account_number, amt):
    print('account number:-',account_number,'\ntotal balance:-',amt)
    main_function(account_number, amt)

#withdraw balance
def withdraw(account_number, amt):
    withdraw_amt = int(input('\nenter amount for withdraw:-'))
    amt=amt-withdraw_amt
    print('\nafter withdraw remaining balance:-',amt)
    #update dict amt at run time
    accounts[account_number][1] =amt
    print(accounts)
    main_function(account_number, amt)

#main function after authentication
def main_function(account_number, amt):
    print(
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
        main_function(account_number, amt)

#function to authenticate user account number and pin..
def authentication():
    #___take input from user for authenticate account no and pin....
    account_number = int(input('enter account number:-'))
    pin = int(input('enter pin:-'))

    for acc, pins in accounts.items():
        if account_number == acc:
            if pin == pins[0]:
                amt = pins[1]
                main_function(account_number, amt)
            else:
                print('wrong credentials')
                authentication()

authentication()