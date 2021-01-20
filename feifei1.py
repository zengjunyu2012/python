import random
my_number = random.randint(1,100)
print(my_number)
for i in range(100):
    you_input = eval(input("number:"))
    cha=you_input-my_number
if you_input==my_number:
    print("对")
else:
    if you_input<my_number:
        print("小")
    else:
        print("大")
