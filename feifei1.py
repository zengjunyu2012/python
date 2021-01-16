import random
my_number = random.randint(1,100)
for i in range(15):
    a = eval(input("number:"))
    if a<my_number:
        print("小")
    elif a>my_number:
        print("大")
    else:
        print("对")
    
