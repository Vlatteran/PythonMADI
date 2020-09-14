def read_int_variable(variable_name):
    """Prints "Введие {variable_name}: " and returns int variable from console"""
    while True:
        variable_str = input(f"Введите {variable_name}: ")
        if not variable_str.isdigit():
            print("Ввёдённое значение не является целым числом")
            continue
        else:
            break
    return int(variable_str)


a = read_int_variable("a")
b = read_int_variable("b")
c = read_int_variable("c")

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
