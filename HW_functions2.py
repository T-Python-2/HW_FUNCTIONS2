## Create a function that takes two parameters of type int . The function should do the following:
'''
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int . 
'''

#### Example : when we call the function with parameter1 =  -15 , and parameter2 = -4 , the printed output should look like this:


def negative_numbers( x:int , y:int ):

    if ( x < y < 0 ):

        for i in range(x ,y+1):
         print(i)
    else:
      print("The numbers should be negative")


negative_numbers(-15,-4)