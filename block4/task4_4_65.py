chislo = int(input("Введите год: "))

if chislo % 4 == 0:
    if chislo != 1700 | chislo != 1800 | chislo != 1900:
        print("Год високосный")
    else:
        print("Год невисокосный")
else:
    print("Год невисокосный")
