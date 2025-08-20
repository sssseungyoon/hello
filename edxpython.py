import sys

def decorator(f):
    def wrapper():
        print("starting to run the function")
        f()
        print("done running the function")
    return wrapper

@decorator
def helloworld():
    print("hello world!")

helloworld()

# very interesting to see functional programming feature in python, which i believed to be operating under OOP
# also this decorator feature could be very useful in web programming, as if you want certain features to 
# function only if the user is logged in, you can simply use a decorator that checks if the user is logged in 
# and apply that decorator to the functions that operate exclusively when the user is logged in

people = [
    {"name": "seung", "house": "mk11"},
    {"name": "taeung", "house": "mk11"},
    {"name": "alberto", "house": "somewhere in ampang"}
]

people.sort(key= lambda person: person['name'])

print(people)

# lambda function can be used as an inline function. In the case of sorting a dictionary, this lambda function can be useful, as you must provide a key through which you want to sort your dictionary.

try:
    x= int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print("must be an integer")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print('cannot divide by zero')
    sys.exit(1)

print(f"{x} / {y} = {result}")

# you can use try and catch to prevent the program from unexpectedly crashing. This would also be useful when you
# are designing an algorithm.