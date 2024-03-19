def compound_interest(P, r, n, t):
    ci = P*((1+((r/100)/n))**(n*t))
    return round(ci, 2)
def compare_ci(P1, P2, r1, r2, n1, n2, t1, t2):
    account_1 = []
    account_2 = []
    
    for i in range(t1+1):
        account_1.append(compound_interest(P1, r1, n1, i))
    
    for i in range(t2+1):
        account_2.append(compound_interest(P2, r2, n2, i))

    return account_1, account_2
a, b = compare_ci(1000, 1000, 6, 2, 4, 12, 12, 104)
print(f"CI Account 1 forward projection: {a}")
print(f"CI Account 2 forward projection: {b}")
        

