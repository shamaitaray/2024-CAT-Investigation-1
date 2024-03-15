import numpy

def time_target(P, r, n, A):
    r = r/100
    a = numpy.log(A/P)
    b = numpy.log(1 + (r/n))
    nt = a/b
    time = nt/n
    return a, b, nt, time

print(time_target(1000, 5, 4, 1500))

r = 'Compare two Compound Interest savings accounts'

print(r.upper())