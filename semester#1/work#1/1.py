from math import sin


def read_float_variable(variable_name):
    while True:
        variable_str = input(f"Введите рацианальное число {variable_name}: ")
        if variable_str.replace(".", "").isdigit() and len(variable_str.split(".")) in (1, 2):
            return float(variable_str)
        else:
            print("Введённое значение не является рациаональным числом")
            continue


m = read_float_variable("M")

if __name__ == "__main__":
    while True:
        x = read_float_variable("X")
        if sin(x) == 0:
            print("Ввёдённое значение x недопустимо")
            continue
        else:
            break

    while True:
        b = read_float_variable("B")
        if b == 0:
            print("Ввёдённое значение B недопустимо")
            continue
        else:
            break

    k = (x ** 2 * (m - b)) / sin(x)
    q = (k / x - m / b) * abs(k) ** 0.5
    print("K = " + str(k) + "; Q = " + str(q))
