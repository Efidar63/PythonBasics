import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        print("Function " + func.__name__ + " took " + str(finish - start) + " seconds")
    return inner

@calculate_time
def usalma(a, b):
    print(math.pow(a, b))

@calculate_time
def factorial(num):
    print(math.factorial(num))

@calculate_time
def addition(a, b):
    print(a + b)

    usalma(2, 3)
    factorial(5)
    addition(10, 20)
    
    if __name__ == "__main__":
    usalma(2, 3)
    factorial(5)
    addition(10, 20)
