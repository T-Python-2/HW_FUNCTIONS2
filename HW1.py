## Create a function that takes two parameters of type int . The function should do the following:
'''
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int . 
'''

def numbers(max:int,min:int):
    if max<0 and min <0:
        if max<min:
            for i in range(max,min+1):
                print(i)
        else:
            print("max should be grester than min")    
    else:
        print("The numbers should be negative") 
numbers(-10,-12) 
           

