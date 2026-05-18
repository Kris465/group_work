chislo = int(input("Введите шестизначное число: "))

firstpol = chislo % 1000
secondpol = int(chislo / 1000)

edin = secondpol % 10
desyatky = int((secondpol / 10) % 10)
sotny = int((secondpol /100 ) % 10)

sum1 = edin + desyatky + sotny

edin2 = firstpol % 10
desyatky2 = int((firstpol / 10) % 10)
sotny2 = int((firstpol /100 ) % 10)

sum2 = edin2 + desyatky2 + sotny2

if sum1 == sum2:
    print("Да, число счастливое")
else:
    print("Нет, число не счастливое")

