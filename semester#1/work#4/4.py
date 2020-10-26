from mylib import read_list


def main():
    alpha = read_list(type_of=float, list_name="alpha", list_size=8)
    beta = read_list(type_of=float, list_name="beta", list_size=8)
    gamma = []

    for i, j in zip(alpha, beta):
        gamma.append(i / j)
    f = 0
    for i in gamma:
        f += i
    print(f"gamma: {gamma},\nF = {f}.")


if __name__ == '__main__':
    main()
