def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

def process(f1, f2, f3, f4, process_name):
    if process_name=="addition":
        print(f1(2,3))
    elif process_name=="subtraction":
        print(f2(7,3))
    elif process_name=="multiplication":
        print(f3(5,3))
    elif process_name=="division":
        print(f4(9,3))
    else:
        print("none")
    
process(addition, subtraction, multiplication, division, "addition")
process(addition, subtraction, multiplication, division, "subtraction")
process(addition, subtraction, multiplication, division, "multiplication")
process(addition, subtraction, multiplication, division, "division")
process(addition, subtraction, multiplication, division, "diiivision")