import random
my_number = random.randint(1,100)
for i in range(20):
    you_input = eval(input("number:"))
    if you_input==my_number:
        print("对")
    else:
        if you_input>my_number:
            if you_input-20>my_number:
                print("太大")
            else:
                print("大")
        else:
            if you_input+20<my_number:
                print("太小")
            else:
                print("小")
