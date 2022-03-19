# Online Python - IDE, Editor, Compiler, Interpreter
import math
from datetime import date
import random


def zad_2_3():
    while True:
        x1 = int(input("pierwsza liczba:"))
        x2 = int(input("druga liczba: "))
        print("{} + {} = {}".format(x1, x2, x1 + x2))
        print("{} - {} = {}".format(x1, x2, x1 - x2))
        print("{} * {} = {}".format(x1, x2, x1 * x2))
        print("{} / {} = {}".format(x1, x2, x1 / x2))
        print("sqrt({} + {}) = {}".format(x1, x2, math.sqrt(x1 + x2)))


def zad_4():
    print("imie: ")
    imie = input()
    print("wiek: ")
    wiek = int(input())
    todays_date = date.today()
    data_urodzenia = todays_date.year - wiek
    out = data_urodzenia + 100
    print("W {} {} skonczy sto lat".format(out, imie))


def zad_5():
    t = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vestibulum finibus eros ut lorem rutrum bibendum.
Morbi non sem ac lorem pellentesque consectetur vitae eget massa.
Maecenas pulvinar turpis et lorem interdum venenatis.
Etiam ut massa tristique, laoreet velit at, tempor elit.
Vivamus faucibus felis eu turpis volutpat interdum non gravida nunc.
Etiam consequat mauris ac diam malesuada interdum.
In nec tortor efficitur, faucibus nulla et, posuere ex.
Praesent eget magna ac enim viverra scelerisque.
Ut volutpat erat nec sapien ullamcorper vestibulum.
Praesent at orci eget mauris gravida posuere non a turpis.
Donec imperdiet purus eu viverra condimentum.
Nullam in nisi a elit euismod maximus.
Duis non enim quis magna sagittis vulputate.
Vestibulum vel sapien eget tellus fringilla congue.
Nam aliquet quam a sem congue porttitor quis eu erat.
Vivamus sit amet ligula ut ante fermentum feugiat eu a diam.
Ut a odio sollicitudin, consequat turpis a, faucibus ex.
Cras facilisis mauris id tempus faucibus.
Integer feugiat leo a ligula fringilla pulvinar."""
    l = t.split(" ")
    sentence = " ".join(random.sample(l, 20))
    print(sentence)


def zad_6():
    print("pierwsza liczba: ")
    x1 = int(input())
    print("druga liczba: ")
    x2 = int(input())
    print("trzecia liczba: ")
    x3 = int(input())
    r = math.sqrt(math.pow(x1, 2) + math.pow(x2, 2))
    fi = math.atan(x1 / x2)

    print("układ biegunowy r ={} , fi={}".format(r, fi))

    r = math.sqrt(math.pow(x1, 2) + math.pow(x2, 2) + math.pow(x3, 2))
    fi = math.atan(x1 / x2)
    omega = math.atan(x3 / r)
    print("układ sferyczny r ={} , fi={}, omega={}".format(r, fi, omega))


if __name__ == "__main__":
    pass