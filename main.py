### --- 2024 CAT Investigation 1 --- ###

#importing math to use the logarithm function when calulcating the time taken to reach a target
#also to do rounding up because the round function doesn't do that, apparently
import math
#functions:
conversions = {

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
#this is for conversions of time periods
def simple_interest(P, R, T):
    si = P*(R/100)*T
    return round(si, 2)
#this calcuates simple interest
def compound_interest(P, r, n, A):
    ci = P*((1+((R/100)/cT))**(cT*T))
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
    
    if menu == "6":
        print("Ok. Stopping program...")
        break

    elif menu == '1':
        print("MODULE 1: SIMPLE AND COMPOUND INTEREST COMPARISON")
        print("") 

        print("Simple Interest Account:")
        SP = float(input("Enter the principal amount in $: "))
        SR = float(input("Enter the interest rate (enter 7% as 7): "))
        SU = input('Enter the interest rate time unit (year, quarter, month, week, day: ')
        print("")

        print("Compound Interest Account:")
        CP = float(input("Enter the principal amount in $: "))
        CR = float(input("Enter the interest rate (enter 7% as 7): "))
        CU = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU == "custom":
            cT = int(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU = cT
        else:
            cT = conversions[CU][CPU]
        print("")

        PT = float(input("Enter the amount of time to project into the future: "))
        PU = input("Enter the projection time unit (year, quarter, month, week, day): ")
        print("")

        print(f"SI account: P = {SP}, r = {SR}% per {SU}")
        print(f"CI account: P = {CP}, r = {CR}% per {CU}, Compounding frequency: {CPU}")
        print(f"Projection timeframe: {PT} {PU}")
        print("")

        ST = PT * conversions[PU][SU]
        CT = PT * conversions[PU][CU]

        print(f"SI Account projected amount: ${SP + simple_interest(SP, SR, ST)}, Interest earned: ${simple_interest(SP, SR, PT)}")
        print(f"CI Account projected amount: ${CP + compound_interest(CP, CR, cT, CT)}, Interest earned: ${compound_interest(CP, CR, cT, PT)}")

    elif menu == '2':
        print("MODULE 2: TIME FOR A CI ACCOUNT TO REACH A TARGET AMOUNT")
        P = float(input("Enter the principal amount in $: "))
        r = float(input("Enter the interest rate (enter 7% as 7): "))
        CU = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        CPU = input("Enter the compounding period(year, quarter, month, week, day, custom): ")
        if CPU == "custom":
            n = float(input("Enter the number of compounding periods per interest rate time unit: "))
            CPU = cT
        else:
            n = conversions[CU][CPU]
        print("")

        A = float(input("Enter target amount: "))
        print("")
        
        print(f"CI account: P = {P}, r = {r}% per {CU}, Compounding frequency: {CPU}")
        print(f"Target amount: ${A}")
        print("")

        print(f"Time taken: {time_target(P, r, n, A)} {CPU}")


