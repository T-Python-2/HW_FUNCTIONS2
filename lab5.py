def negativeNumbers(number1: int, number2: int):
    if number1 and number2 < 0 :
        if number1<number2:
            for n in range(number1, number2 + 1):
                print(n)
    else:
        print("The numbers should be negative")

negativeNumbers(-15,-4)