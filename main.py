# ------------------------------------ZADANIE 1--------------------------------------------

def warunek(liczba):
    if a > 0:
        print("Liczba dodatnia")
    else:
        print("Liczba niedoadatnia")


a = int(input("Podaj a"))
warunek(a)

# ----------------------------------ZADANIE 2----------------------------------------

def f(x):
    if x > 1:
        return x**2 + 1
    else:
        return 13

print(f(13))
print(f(-2))

#-----------------------------ZADANIE 3-------------------------------------------

def sprawdz(x):
    if x % 2 == 0:
        return "PARZYSTA"
    else:
        return  "NIEPARZYSTA"

x = 13
y = 16

print("wynik dla",x,"rowna sie",sprawdz(x))
print("wynik dla",y,"rowna sie",sprawdz(y))

#---------------------------ZADANIE 4------------------------------------------------

def petla(a,b):
    if a < b:
        w = 0
        for i in range(a,b,2):
            w = w + i
        return w

    else:
        exit(0)


print("Wynik dla petla(0,13):", petla(0,13))

#-------------------------Zadanie-kalkulator + menu----------------------------
def dodawanie(a,b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    return a / b

a = float(input("Podaj a:"))#podanie 1 liczby
b = float(input("Podaj b:"))#podanie 2 liczby
x = int(input("Wybierz menu\n1.dodawanie\n2.odejmowanie\n3.mnozenie\n4.dzielenie\nWybor:"))#sterownaie menu
# sterowaniem menu -> x rowna sie numer w menu
if x == 1:
    print(dodawanie(a,b))
elif x == 2:
    print(odejmowanie(a,b))
elif x == 3:
    print(mnozenie(a,b))
elif x ==  4:
    print(dzielenie(a,b))
#----------------------------------------Objetosc ostroslupa------------------------------------------------



def warunek(pp,h):
    if h > 3:
        return 1/3 * pp * h
    else:
        return pp * h

pp = float(input("Podaj pole podstawy:"))
h = float(input("Podaj wysokość"))
print("Objętość wynosi:",warunek(pp,h))






















