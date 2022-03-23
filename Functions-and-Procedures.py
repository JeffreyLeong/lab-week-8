"""
functions lab example code
"""
def foo(num):
    '''
     f(num) = 3*num + 10
    '''
    # students should write code here
    return (3*num) + 10

def bar(first, second, third):
    """
     Create a function bar that takes 3 input arguments (first, second, and third)
     and returns a list containing the input values in a sorted list.
    """
    # students should write code here
    namesList = [first, second, third]
    namesList.sort()
    print("Sorted List:", namesList)

# students should write code to run foo and bar here
print("foo(0) = " + str(foo(0)))
print("foo(1) = " + str(foo(1)))
print("foo(2) = " + str(foo(2)))
print("foo(3) = " + str(foo(3)))
print("foo(4) = " + str(foo(4)))

bar("Lupita", "Jalen", "Apple")
