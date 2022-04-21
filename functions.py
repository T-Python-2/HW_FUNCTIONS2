






def negatives(firstInput :int,secondInput :int):
    if firstInput and secondInput < 0 :
        if firstInput < secondInput :
            for i in range(firstInput,secondInput +1):
                print(i)
        else:
            print("First input should be bigger than the second input") 
    else:
        print("Inputs should be negative")
        


negatives(-6,-1)