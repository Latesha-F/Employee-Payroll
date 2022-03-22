count = 0
print("Employee Payroll")
print("Let's get started with the first employee:")
while count < 10:
    count += 1
    print(count)
    
    user = str
    end="0"
    numhrswk = round(40,2)
        
    #Employee should enter their name below
    user=input("Hi, what is your name? ")
    print("The following questions are Payroll related as to determine your gross/net pay.")
    if user == end:
        print("Done")
    #Employee should enter their hourly pay rate below
    else:
        payrate=(float(input('What is your pay rate per hour? $')))



    #Employee should enter the number of hours worked below

        numhrswk=(float(input('How many hours have you worked during this pay period? ')))


    if numhrswk<=40:
      print("Employee's name:", user)
      print("Hours Worked: ", numhrswk)
       #Employee should enter their pay rate below
      print("Your regular payrate: $", payrate)
      regpay=round(numhrswk * payrate, 2)
      fedtax=round(regpay*0.10)
      statetax=round(regpay*0.06)
      fica=round(regpay * 0.03)
      gpay=round(regpay, 2)
      npay=round(regpay - (fedtax+statetax+fica), 2)
      print("Federal taxes: $", fedtax)
      print("State taxes: $", statetax)
      print("FICA: $", fica)
      regpay=round(numhrswk * payrate, 2)
      print("Gross Pay: $", gpay)
      print("Net Pay: $", npay)


    elif numhrswk>40:
        print("Employee's name:", user)
        print("Hours Worked: ", numhrswk)
        print("Your regular payrate: $", payrate)
        othrs = round(numhrswk - 40, 2)
        otrate=round(payrate * 1.5, 2)
        otpay=round(othrs * otrate)
        print("Overtime hours: ", othrs)
        print("Overtime pay: $", otpay)
        regpay=round(numhrswk * payrate, 2)
        gpay=round(regpay+otpay, 2)
        fedtax=round(gpay*0.10)
        statetax=round(gpay*0.06)
        fica=round(gpay*0.03)
        npay=round(regpay - (fedtax+statetax+fica),2)
        print("Federal taxes: $", fedtax)
        print("State taxes: $", statetax)
        print("FICA: $", fica)
        print("Gross Pay: $", gpay)
        print("Net Pay: $", npay)