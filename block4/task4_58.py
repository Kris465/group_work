# number = int(input("Введите трехзначное число: "))

# my_list = [number // 100, (number // 10) % 10, number % 10]

# if 4 in my_list or 7 in my_list:
#     print("a) Цифры 4 или 7 входят в число.")
# else:
#     print("a) Не входят")


# if 3 in my_list or 6 in my_list or 9 in my_list:
#     print("б) Цифры 3, 6 или 9 входят в число.")
# else:
#     print("б) Не входят")

number = input("Введите трехзначное число: ")

if "4" in number or "7" in number:
    print("a) Цифры 4 или 7 входят в число.")
else:
    print("a) Не входят")

if "3" in number or "6" in number or "9" in number:
    print("б) Цифры 3, 6 или 9 входят в число.")
else:
    print("б) Не входят")
