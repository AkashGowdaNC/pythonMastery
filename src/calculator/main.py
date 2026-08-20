from calculator.operations import add
import sys
import math
print(sys.path)
def main():
    print(add(2,3))

if __name__ == "__main__":
    main()
print(type(math))
print(dir(math))
print(math.__name__)
print("math" in sys.modules)
def student(name,age):
    print(name)
    print(age)
student("akash",22)
student(22,"vikas")
student(age=22,name="akash")
student(name="vikas",age=18)
student("akash",age=22)
def connect(host="localhost",port=5000):
    print(host,port)
connect()
connect("12.23.7.10.9")
connect(port=5000)
def add_item(item,items=[]):
    items.append(item)
    return items
print(add_item("A"))
print(add_item("B"))
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
"""clousre"""
def multiplier(n):

    def multiply(x):
        return x * n

    return multiply
double = multiplier(2)
print(double(10))
"""A closure happens when an inner function retains access to variables
 from an enclosing scope even after the outer function has finished executing"""
text="python"
text='j'+text[1:]
print(text)