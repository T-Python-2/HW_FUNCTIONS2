def ascending_print_neg (num1:int, num2:int):
    if (num1 > 0 and num2 > 0 ):
        print("The numbers should be negative")
        return
    if (num1<num2):
        for number in range(num1,num2):
            print(str(number) +"."+"\n")
    else:
        print("first number large")



ascending_print_neg(1,-4)
ascending_print_neg(-1,-4)
ascending_print_neg(-15,-4)