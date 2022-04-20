'''
## Create a function that takes two parameters of type int . The function should do the following:
'''

def negative_numbers(num1:int, num2:int):
    if num1 and num2 < 0:
        #Check that the first parameter is smaller than the second parameter .
        if num1 < num2:
            print("the first parameter should be the greater ")
        else : 
            #Using a loop Print all the numbers bettween the smaller int up to the bigger int .
            for i in range(num2, num1+1):
               print(i)
    else: 
        #Check if all the variables are negative . Else print "The numbers should be negative"
        print("The numbers should be negative")




negative_numbers(5,-5)

