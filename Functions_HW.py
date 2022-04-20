#Functions Homework

def in_between(start:int, end:int):
    '''The function will take two negative numbers, in which the first number should be less than the second number, and will print all numbers in the range between the smaller and the larger numbers inclusive.'''
    if start < 0 and end < 0:
        if start < end:
            for number in range(start,end+1,1):
                print(number)
        else:
            print("The first number is greater than the second number")
    else:
        print("The numbers should be negative")

the_first_number = int(input("Enter the first negative number "))
the_second_number = int(input("Enter the second negative number "))

in_between(the_first_number,the_second_number)
print(in_between.__doc__)
