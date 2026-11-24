"""
    Generators are functions that return values at a time using 
    `yield` key words instead of storing all values in a memory\. 

    it usefull for saving memory space. 

    1. yield keyword => preserve the function final state for example: 
       
         def funName(): 
            yield 10
            yield 20
            yield 30

        first it well return the 10 and save where the function stop 
        second it will return 20 and so on.

    2. Generator Expression

    They provide a shorter way to create generators without defining a separate function.
    They use parentheses instead of square brackets and generate values lazily.

"""

# 1. 
def generate_numbers():
    yield 10
    yield 20
    yield 30

gen = generate_numbers()

print(next(gen))
print(next(gen))
print(next(gen))


# 2. 
squares = (num*num for num in range(1, 6))

for value in squares: 
    print(value) 


# 3.
def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


for num in fibonacci():
    if num > 50:
        break
    print(num, end=" ")