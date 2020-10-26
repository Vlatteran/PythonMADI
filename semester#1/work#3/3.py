def main():
    words = [input(f'Input word №{i}: ') for i in range(4)]
    longest_word = words[0]
    max_len = len(longest_word)
    for i in words:
        current_len = len(i)
        if current_len > max_len:
            max_len = current_len
            longest_word = i
    print(f'Longest word is \'{longest_word}\'')


if __name__ == '__main__':
    main()
