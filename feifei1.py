import random
my_number = random.randint(1,100)
for i in range(1,11):
    you_input = eval(input("number:"))
    if you_input==my_number:
        print("对")
        print("你胜利了!")
        print("你猜了",i,"次")
        break
        if i>10:
            print("你失败了!")
            break
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
    if i"次">10:
        print("你失败了!")
    else:
        print("你胜利了!")
        print("你猜了",i,"次")
