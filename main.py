def d (num1:int, num2:int):
    if (num1 and num2 < 0 ):
        print("The numbers should be negative")
        return
    if (num1<num2):
        print("the {} is smaller than {}".format(num1,num2))
    for number in range(num1,num2):
        print(number)

def ascending_print (num1,num2) :
    for number in range(num1, num2+1):
        print(str(number) +"."+"\n")


ascending_print(-15,-4)

d(4,-7)