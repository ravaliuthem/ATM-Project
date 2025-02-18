from ATMExcept import DepositError,WithdrawError,InSufFundError
bal=500-0#here bal is called global variable
def deposit():
    damt=float(input("Enter ur Deposite Amount:"))#valueError---alnums/strs/symbols
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("ur Account XXXXX123 Deposited with INR:{}".format(damt))
        print("NOw ur Account XXXXX123 Balance INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter ur withdraw Amount:"))#value--error---alnums/strs/symbols
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSufFundError
    else:
        bal=bal-wamt
        print("ur Accountxxxxx123 Debited with INR:{}".format(wamt))
        print("Now ur Accountxxxxx123 BalanceINR:{}".format(bal))
def balenq():
            print("ur Accountxxxxx123Balance INR:{}".format(bal))

