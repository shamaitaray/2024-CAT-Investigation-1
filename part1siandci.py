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
SR = float(input("Enter the interest rate (enter 7% as 7):"))
print("")

print("Compound Interest Account:")
CP = float(input("Enter the principal amount in $: "))
CR = float(input("Enter the interest rate (enter 7% as 7):"))
CT = float(input("Enter the compounding period(year, quarter, month, week, day, custom): "))
print("")

PT = float(input("Enter the amount of time to project into the future:"))
print("")

print(f"SI account: P = {SP}, r = {SR}% per year")
print(f"CI account: P = {CP}, r = {CR}% per year")
print(f"Projection timeframe: {PT} year")
print("")

print(f"SI Account projected amount: ${SP + simple_interest(SP, SR, PT)}, Interest earned: ${simple_interest(SP, SR, PT)}")
print(f"CI Account projected amount: ${CP + compound_interest(CP, CR, CT, PT)}, Interest earned: ${compound_interest(CP, CR, CT, PT)}")