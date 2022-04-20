

def print_values(x:int,y:int): 


    while x < 0 and y<0:

        if x<y:
            for i in range(x,y+1):
                print(i)
            break
        else:
            print("First number should be lesser than second number")
            break
    else:
        print("The numbers should be negative")  

print_values(-15,-4)     