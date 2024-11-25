add=lambda a,b: a + b
print(add(10,4))

multiplay=lambda a,b: a * b
print(multiplay(23,59))

#Square of each number
number=range(11)
square_numbers=list(map(lambda x: x**2, number))
print("Squere numbers: ", square_numbers)

#Even
even_numbers=list(filter(lambda x: x%2 == 0, square_numbers))
print("Even Numbers: ", even_numbers)