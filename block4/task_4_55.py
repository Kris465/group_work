
n = int(input("Введите двузначное число: "))
a = int(input("Введите цифру a (0-9): "))

des = n // 10  
ed = n % 10    


if des == 3 or ed == 3:
    print("а) Да, цифра 3 входит")
else:
    print("а) Нет, цифра 3 не входит")


if des == a or ed == a:
    print("б) Да, цифра", a, "входит")
else:
    print("б) Нет, цифра", a, "не входит")