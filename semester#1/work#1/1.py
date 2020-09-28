from math import sin
from mylib import read_float_variable as read


def main():
    m = read("M")
    while True:
        x = read("X")
        if sin(x) == 0:
            print("Недопустимое число (деление на 0)")
            continue
        else:
            break
    while True:
        b = read("B")
        if b == 0:
            print("Недопустимое число (деление на 0)")
            continue
        else:
            break
    k = (x ** 2 * (m - b)) / sin(x)
    q = (k / x - m / b) * abs(k) ** 0.5
    print("K = " + str(k) + "; Q = " + str(q))


if __name__ == "__main__":
    main()
