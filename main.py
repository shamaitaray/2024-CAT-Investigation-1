#2024 CAT Investigation 1#


conversions = {
    'year' : {
        'quarter': 4,
        'month': 12,
        'week': 52,
        'day': 365,
    },

    'quarter' : {
        'month': 3,
        'week': 12,
        'day': 90,
    },
    
    'month' : {
        'week': 4,
        'day': 30,
    },

    'week' : {
        'day': 7,
    },
}

time = input("unit of time: ")
many = int(input('how many? '))
time2 = input('converting to: ')


print(many*conversions[time][time2])