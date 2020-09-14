from math import sin

while True:
    m_str = input("Введите M: ")
    if m_str.isdigit():
        m = int(m_str)
        break
    else:
        print("Ввёдённое значение не является целым числом")
        continue

while True:
    x_str = input("Введите x: ")
    if x_str.isdigit():
        x = int(x_str)
    else:
        print("Ввёдённое значение не является целым числом")
        continue
    if sin(x) == 0:
        print("Ввёдённое значение x недопустимо")
        continue
    else:
        break

while True:
    b_str = input("Введите B: ")
    if b_str.isdigit():
        b = int(b_str)
    else:
        print("Ввёдённое значение не является целым числом")
        continue
    if b == 0:
        print("Ввёдённое значение B недопустимо")
        continue
    else:
        break

k = (x ** 2 * (m - b)) / sin(x)
q = (k / x - m / b) * abs(k) ** 0.5
print("K = " + str(k) + "; Q = " + str(q))
print("lol")
