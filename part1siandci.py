def regular_deposits(P, r, n, t, D,):
    opening = []
    interest = []
    deposit = []
    closing = []

    total = round(P, 2)

    for i in range(t + 1):
        opening.append(round(total, 2))
        total *= round((1 + ((r/100) / n))**n, 2)
        i = round(total - opening[-1], 2)
        interest.append(i)
        total += round(D, 2)
        deposit.append(D)
        closing.append(round(total, 2))

    zipped = zip(opening, interest, deposit, closing)

    print('column headings: opening, interest, deposit, closing')
    for row in list(zipped):
        print(row)


print(regular_deposits(1000, 5, 12, 60, 250))

