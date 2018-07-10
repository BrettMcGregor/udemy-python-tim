def odd_number_generator():
    number = 1
    while True:
        yield number
        number += 2


def pi_series():
    odds = odd_number_generator()
    approx = 0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx


approx_pi = pi_series()

for x in range(1000000):
    print(next(approx_pi))

