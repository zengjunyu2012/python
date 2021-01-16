import random
my_number = random.randint(1,100)
print(my_number)
for i in range(100):
    x = eval(input("number:"))
    cha=my_number-x
    if x<my_number:
        print("小")
        if cha<+20:
            print("太小")
    elif x>my_number:
        print("大")
        if cha>-20:
            print("太大")
    else:
        print("对")
