# trancate

from random import uniform, seed
seed(42)


def truncate(n):
    return int(n * 1000) / 1000


def simulation():
    actual_value, troncated_value = 100, 100
    res_actual = [uniform(-0.05, 0.05) + actual_value for _ in range(int(1e6))]
    res_troncated = [truncate(uniform(-0.05, 0.05) + troncated_value)
                     for _ in range(int(1e6))]
    return res_actual, res_troncated


# res_actual, res_troncated = simulation()
# actual = sum(res_actual)
# print(actual)
# troncated = sum(res_troncated)
# print(troncated)

actual_value, troncated_value = 100, 100

for _ in range(int(1e6)):
    randn = uniform(-0.05, 0.05)
    actual_value = actual_value + randn
    # troncated_value = truncate(troncated_value + randn)
    troncated_value = round(troncated_value + randn, 3)


print(actual_value)
print(troncated_value)
