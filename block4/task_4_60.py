chislo = int(input("Введите четырёхзначное число "))

edinicy = chislo % 10
match edinicy:
    case 2 | 7 | 3 | 6 | 9:
        print(F"Да в этом числе есть {edinicy}")
desyatky = int((chislo / 10) % 10)
match desyatky:
    case 2 | 7 | 3 | 6 | 9:
        print(F"Да в этом числе есть {desyatky}")
sotny = int((chislo /100 ) % 10)
match sotny:
    case 2 | 7 | 3 | 6 | 9:
        print(F"Да в этом числе есть {sotny}")
tysach = int((chislo /1000 ) % 10)
match tysach:
    case 2 | 7 | 3 | 6 | 9:
        print(F"Да в этом числе есть {tysach}")
