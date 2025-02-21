from ATMExcept import DepositError,WithdrawError,InSufFundError
from ATMMenu import menu
from ATMOperation import deposit,withdraw,balenq
while(True):
    menu()
    try:
        ch=int(input("enter ur choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                      print("Don't try to Deposit alnums strs and Symbols")
                except DepositError:
                      print("Don't Enter-ve and Zero as Deposite Amount")
            case 2:
                try:
                     withdraw()
                except ValueError:
                      print("Don't try to Withdraw alnums strs and Symbols")
                except WithdrawError:
                      print("Dont enter -ve and Zero as withdraw Amount")
                except InSufFundError:
                      print("ur Account xxxxx123 does not have suffFund---Read python Notes")
            case 3:
                    balenq()
            case 4:
                    print("Thanks for using this application")
                    break
            case _:
                print("ur selection of operation is wrong ------try again")
    except ValueError:
        print("Don't enter alnums,strs and Symbols for choice-try again")






