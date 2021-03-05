"""
Autorem skryptu jest XYZ

"""


def get_info():
    print("Witaj, to jest prosty kalkulator")


def dodaj(a, b):
    wynik = a + b
    return wynik


def odejmij(a, b):
    return a - b


def dziel(a, b):
    result_int = a // b
    result_float = a/b
    result_modulo = a%b
    return result_int, result_float, result_modulo


get_info()

a = int(input())
b = int(input())

print(dodaj(a, b))
print(dziel(a, b))
print("Koniec programu. Papa!")
