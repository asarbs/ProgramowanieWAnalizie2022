import math

def main():
    word = input("insert word")
    if is_palindrom(word):
        print("{} is palindrom".format(word))
    else:
        print("{} is not palindrom".format(word))


def is_palindrom(word):
    i = 0
    word_length = len(word)
    while i < word_length:
        a = word[i]
        b = word[(word_length + (-1 * i)) -1]
        if a != b:
            return False
        i += 1
    return True


if __name__ == "__main__":
    main()


