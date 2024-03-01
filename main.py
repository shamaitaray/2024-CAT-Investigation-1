#2024 CAT Investigation 1#

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

def simple_interest(P, R, T):
    si = P*(R/100)*T
    return round(si, 2)

def compound_interest(P, R, cT, T):
    ci = P*((1+((R/100)/cT))**(cT*T))
    return round(ci, 2)

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