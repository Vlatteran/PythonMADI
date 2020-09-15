from mylib import read_float_variable as read

if __name__ == "__main__":
    a = read("a")
    b = read("b")
    c = read("c")

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
