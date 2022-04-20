
def negativeNumbers(x:int,y:int):
    if x < 0 and y < 0 :
        if x < y :
            for i in range(x,y+1,1):
                print(i)
        else:
            print("First parameter is bigger than the second parameter ") 
    else:
        print("The numbers should be negative")
        


negativeNumbers(-15,-4)

