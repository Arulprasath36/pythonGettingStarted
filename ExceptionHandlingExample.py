"""
The below method will throw an error ZeroDivisionError: integer division or modulo by zero
and our program will stop there itself without continuing.
"""

def divide(numerator,denominator):
    return numerator/denominator
#print((divide(2,3)))
#print((divide(2,0)))
#print((divide(denominator=2,numerator=6)))


#But no matter what the exception our program should continue to do that
# we are going to handle the exception. Lets modify the above method a bit

def divideWithExceptionHandling(numerator,denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Denominator should not be zero")
print((divideWithExceptionHandling(2,3)))
print((divideWithExceptionHandling(2,0)))
print((divideWithExceptionHandling(denominator=2,numerator=6)))

