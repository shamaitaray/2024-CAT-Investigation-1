def simple_interest(P, R, T):
    si = P*(R/100)*T
    return round(si, 2)

print("MODULE 1: SIMPLE AND COMPOUND INTEREST COMPARISON")
print("") 
print("Simple Interest Account:")

P = float(input("Enter the principal amount in $: "))
R = float(input("Enter the interest rate (enter 7% as 7):"))
T = float(input("Enter the amount of time to project into the future:"))

print(f"SI account: P = {P}, r = {R}% per year")
print(f"Projection timeframe: {T} year")

print(f"SI Account projected amount: ${P + simple_interest(P, R, T)}, Interest earned: ${simple_interest(P, R, T)}")