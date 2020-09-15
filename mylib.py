def read_float_variable(variable_name):
    while True:
        variable_str = input(f"Введите рацианальное число {variable_name}: ")
        if variable_str.replace(".", "").isdigit() and len(variable_str.split(".")) in (1, 2):
            return float(variable_str)
        else:
            print("Введённое значение не является рациаональным числом")
            continue
