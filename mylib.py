def read_float_variable(variable_name):
    while True:
        variable_str = input(f"Введите рацианальное число {variable_name}: ")
        if variable_str.replace(".", "").isdigit() and len(variable_str.split(".")) in (1, 2):
            return float(variable_str)
        else:
            print("Введённое значение не является рациаональным числом")
            continue


def read_value(type_of=int, msg="", error_msg="Incorrect type"):
    result = None
    while True:
        try:
            result = type_of(input(f"{msg}: "))
        except ValueError:
            print(error_msg)
        if result is not None:
            break
    return result


def read_list(list_name: str, list_size=0, type_of=int):
    if list_size == 0:
        list_size = read_value(type_of=int, msg=f"Введите длинну массива {list_name}")
    result = []
    for i in range(list_size):
        result.append(read_value(type_of=int, msg=f"{list_name}[{i}]"))
    return result


def binary_search(array, element, start=0, end=0):
    if end == 0:
        end = len(array) - 1
    if start == end or start > end or start < 0 or end > len(array):
        print(f"Error")
        return
    while True:
        mid = int(start + (end - start) / 2)
        if end < start:
            return -1
        elif element == array[mid]:
            return mid
        elif element > array[mid]:
            start = mid + 1
        else:
            end = mid - 1


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        from random import randint as random
        mid = array[random(0, len(array) - 1)]
        low = []
        eq = []
        high = []
        for i in array:
            if i < mid:
                low.append(i)
            elif i > mid:
                high.append(i)
            else:
                eq.append(i)
        low = quick_sort(low)
        high = quick_sort(high)
        return low + eq + high


def time_test(function, arguments: list, msg=True):
    import time
    start_time = time.time()
    function(arguments)
    end_time = time.time()
    if msg:
        print("--- %s seconds ---" % (end_time - start_time))
    return end_time - start_time


class Graph:
    def __init__(self, weighted=False, directed=False):
        self.directed = directed
        self.weighted = weighted
        self.nodes = {}

    # def add(self, node:dict.):
    #     self.nodes[node.]
