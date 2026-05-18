num = input("Введите 4 значное число: ")
if num[0] == num[1] == num[2]: 
    print("содержит")
elif num[0] == num[1]  == num[3]: 
     print("содержит")
elif num[0] == num[2]  == num[3]: 
     print("содержит")     
elif num[1] == num[2] == num[3]:
     print("содержит")
elif num[1] == num[3] == num[0]:
     print("содержит")
else:
    print('не содержит')     
         