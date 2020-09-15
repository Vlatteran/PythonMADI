def read_float_variable(variable_name):
    while True:
        variable_str = input(f"Введите рацианальное число {variable_name}: ")
        if variable_str.replace(".", "").isdigit() and len(variable_str.split(".")) in (1, 2):
            return float(variable_str)
        else:
            print("Введённое значение не является рациаональным числом")
            continue


if __name__ == "__main__":
    a = read_float_variable("a")
    b = read_float_variable("b")
    c = read_float_variable("c")

    if c == 20:
        s = a * b
    else:
        s = 2 * a

    if 10 <= c < 20:
        p = abs(a * b) ** 2
    else:
        p = b ** 2
    q = s + p

    print(f"S = {s}; P = {p}, Q = {q}")
