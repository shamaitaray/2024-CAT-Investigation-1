### --- 2024 CAT Investigation 1 --- ###

#importing math to use the logarithm function when calulcating the time taken to reach a target
#also to do rounding up because the round function doesn't do that, apparently
import math

conversions = {   #this is for conversions of time periods

    'year' : {
        'year': 1,
        'quarter': 4,
        'month': 12,
        'week': 52,
        'day': 365,
    },
    'quarter' : {
        'quarter': 1,
        'month': 3,
        'week': 12,
        'day': 90,
    },
    'month' : {
        'month': 1,
        'week': 4,
        'day': 30,
    },
    'week' : {
        'week': 1,
        'day': 7,
    },
}

#functions:
def simple_interest(P, R, T):
    si = P*(R/100)*T
    return round(si, 2)
#this calcuates simple interest

def compound_interest(P, r, n, t):
    ci = P*((1+((r/100)/n))**(n*t))
    return round(ci, 2)
#this calculates compound interest

def time_target(P, r, n, A):
    r = r/100
    a = math.log(A/P)
    b = math.log(1 + (r/n))
    nt = a/b
    time = nt/n
    return math.ceil(time)
#this calculates the time needed to reach the target

def compare_ci(P1, P2, r1, r2, n1, n2, t1, t2):
    account_1 = []
    account_2 = []
    
    for i in range(t1+1):
        account_1.append(compound_interest(P1, r1, n1, i))
    
    for i in range(t2+1):
        account_2.append(compound_interest(P2, r2, n2, i))

    return account_1, account_2

def regular_deposits(P, r, n, t, A, D,):
    opening = []
    interest = []
    deposit = []
    closing = []

    if t == 0:
        t = time_target(P, r, n, A)

    total = round(P, 2)

    for i in range(t + 1):
        opening.append(round(total, 2))
        total *= round((1 + ((r/100) / n))**n, 2)
        i = round(total - opening[-1], 2)
        interest.append(i)
        total += round(D, 2)
        deposit.append(P)
        closing.append(round(total, 2))

    zipped = zip(opening, interest, deposit, closing)

    print('column headings: opening, interest, deposit, closing')
    for row in list(zipped):
        print(row)
# this calculate the regular deposits

#information for user + menu
print("""***
WELCOME TO, UH, WHATEVER THIS IS!!!
This program has five modules. Choose a module by typing its number:
(1) Compare simple and compound interest savings acccounts
(2) Calculate the time for a CI savings account to reach a target amount
(3) Compare two Compound Interest savings accounts
(4) Model a CI savings account with regular deposits
(5) Model increases in compounding frequency""")

while True:  #use of while loop means the program can be used again and again wihtout rerunning
    print("***")

    menu = input("Enter 1 to 5, or 6 to quit: ") 

    print("")
    
    if menu == "6": # this is to quit
        print("Ok. Stopping program...")
        break

    elif menu == '1': 
        print("MODULE 1: SIMPLE AND COMPOUND INTEREST COMPARISON")
        print("") 

        print("Simple Interest Account:") # input for the simple interest account
        SP = float(input("Enter the principal amount in $: "))
        SR = float(input("Enter the interest rate (enter 7% as 7): "))
        SU = input('Enter the interest rate time unit (year, quarter, month, week, day: ')
        print("")

        print("Compound Interest Account:") # input for compound interest account
        CP = float(input("Enter the principal amount in $: "))
        CR = float(input("Enter the interest rate (enter 7% as 7): "))
        CU = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU == "custom": 
            cT = int(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU = cT
        else:
            cT = conversions[CU][CPU] # this converts from the compounding period to a number
        print("")

        # input for projection amount
        PT = float(input("Enter the amount of time to project into the future: "))
        PU = input("Enter the projection time unit (year, quarter, month, week, day): ")
        print("")

        # summary for info
        print(f"SI account: P = {SP}, r = {SR}% per {SU}")
        print(f"CI account: P = {CP}, r = {CR}% per {CU}, Compounding frequency: {CPU}")
        print(f"Projection timeframe: {PT} {PU}")
        print("")

        # this makes all the time units the same
        ST = PT * conversions[PU][SU]
        CT = PT * conversions[PU][CU]

        # use of f strings and functions for output
        print(f"SI Account projected amount: ${SP + simple_interest(SP, SR, ST)}, Interest earned: ${simple_interest(SP, SR, PT)}")
        print(f"CI Account projected amount: ${CP + compound_interest(CP, CR, cT, CT)}, Interest earned: ${compound_interest(CP, CR, cT, PT)}")
        print("")

    elif menu == '2':
        print("MODULE 2: TIME FOR A CI ACCOUNT TO REACH A TARGET AMOUNT")
        print("")

        # input for account
        P = float(input("Enter the principal amount in $: "))
        r = float(input("Enter the interest rate (enter 7% as 7): "))
        CU = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU == "custom":
            n = float(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU = n
        else:
            n = conversions[CU][CPU] # this converts the compounding period into a number

        # target amount info
        A = float(input("Enter target amount: "))
        print("")
        
        # summary
        print(f"CI account: P = {P}, r = {r}% per {CU}, Compounding frequency: {CPU}")
        print(f"Target amount: ${A}")
        print("")
        t = time_target(P, r, n, A)

        # outputs forward projection
        projections = []
        for i in range(t + 1):
            projections.append(compound_interest(P, r, n, i))
        
        # use of f strings and functions for output
        print(f"Forward projection: {projections}")
        print(f"Time taken: {t} {CPU}")
        print("")

    elif menu == '3':
        print("MODULE 3: COMPARE TWO COMPOUND INTEREST SAVINGS ACCOUNTS")
        print("")

        print("CI Account 1:") # input for account 1
        P1 = float(input("Enter the principal amount in $: "))
        r1 = float(input("Enter the interest rate (enter 7% as 7): "))
        CU1 = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU1 = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU1 == "custom":
            n1 = float(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU1 = n1
        else:
            n1 = conversions[CU1][CPU1] # converts from compounding period to a number

        # input for projection time
        PT1 = int(input("Enter the amount of time to project into the future: "))
        PU1 = input("Enter the projection time unit (year, quarter, month, week, day): ")
        print("")

        print("CI Account 2:") # input for account 2
        P2 = float(input("Enter the principal amount in $: "))
        r2 = float(input("Enter the interest rate (enter 7% as 7): "))
        CU2 = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU2 = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU2 == "custom":
            n2 = float(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU2 = n2
        else:
            n2 = conversions[CU2][CPU2] # converts from compounding period to a number

        # input for projection     
        PT2 = int(input("Enter the amount of time to project into the future: "))
        PU2 = input("Enter the projection time unit (year, quarter, month, week, day): ")
        print("")

        # time period conversions
        T1 = PT1 * conversions[PU1][CU1]
        T2 = PT2 * conversions[PU2][CU2]
        
        #output
        a, b = compare_ci(P1, P2, r1, r2, n1, n2, T1, T2)
        print(f"CI Account 1 forward projection: {a}")
        print(f"CI Account 2 forward projection: {b}")
        
    elif menu == '4':
        print("MODULE 4: MODEL A CI SAVINGS ACCOUNT WITH REGULAR DEPOSITS")
        print("")

        # input for account
        P = float(input("Enter the principal amount in $: "))
        r = float(input("Enter the interest rate (enter 7% as 7): "))
        CU = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU == "custom":
            n = float(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU = n
        else:
            n = conversions[CU][CPU] # converts from compounding period to a number
        
        # input for deposits
        d = float(input("Enter the regular deposit amount per compounding period: "))
        da = float(input("Enter the dollar amount to project to (if you enter 0, you will be asked for the amount of time to project for): "))
        if da == 0:
            t = int(input("In that case, enter the amount of time to project for: "))
            tu = input("Enter the projection time unit (year, quarter, month, week, day): ")
            t = t * n
        else:
            t = 0
        
        # printing output
        print(regular_deposits(P, r, n , t, da, d))
        print("")

    elif menu == "5":
        print('MODULE 5: STIMULATE INCREASES IN COMPOUNDING FREQUENCY')
        print("")

        print("QUARTERLY COMPOUNDING")
        print(regular_deposits(1000, 100, 4, 4, 0, compound_interest(1000, 100, 4, 4)))
        
        print("MONTHLY COMPOUNDING")
        print(regular_deposits(1000, 100, 12, 12, 0, compound_interest(1000, 100, 12, 12)))

        print("WEEKLY COMPOUNDING")
        print(regular_deposits(1000, 100, 52, 52, 0, compound_interest(1000, 100, 52, 52)))

        print("DAILY COMPOUNDING")
        print(regular_deposits(1000, 100, 365, 365, 0, compound_interest(1000, 100, 365, 365)))

        print("HOURLY COMPOUNDING")
        print("Error: the result is to large to output")

        print("TEN MINUTE COMPOUNDING")
        print("Error: the result is too large to output")
