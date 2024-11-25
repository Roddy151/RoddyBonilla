#Iterator example

#Create a list

myList=[1,2,3,4,5]

#Get iterator

myIter=iter(myList)

#Use the iterartor

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

#Iterate in charter string
#Create a charter string
text="Hola Mundo"
#Get iterartor of the charter string
iter_text=iter(text)
#Iterate
for char in iter_text:
    print("\n",char)

#Create a iterator for odd numbers 
print("\n")
#Limit 
limit=10
#Create a iterator
oddIterator=iter(range(1,limit+1,2))
#Use the iterator
for oddNumbers in oddIterator:
    print(oddNumbers)

#Generator
print("\n")

def myGenerato():
    yield 1
    yield 2
    yield 3

for value in myGenerato():
    print(value)

#Fibonacci
#0 1 1 2 3 5 8 13 21...
print("\n")

def fibonacci(limit):
    x=0
    y=1
    while x<limit:
        yield x
        x, y = y, x+y

for num in fibonacci(30):
    print(num)

#Odd/even number generator 

def oddEvenNumber(type, limit):
    if type=="odd":
        x=list(range(1,limit+1,2))
        yield x
    elif type=="even":
        x=list(range(0,limit+1,2))
        yield x
    else: 
        print("Parameters sent to the function are incorrect")


iterList=iter(oddEvenNumber("odd",20))
for num in iterList:
    print(num)
