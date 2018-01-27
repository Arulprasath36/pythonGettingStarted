#This is an example of simple method and calling it
def sayHello():
    name=raw_input("Hello what is your name?")
    print("Hi "+name+" nice to meet you")
#sayHello()

# This is an example of calling a method with arguments
def sayHello(name):
    print("Hello "+name)
    count=len(name)
    print ("Hey "+ name+". Do you know your name has "+ str(count)+" letters")
sayHello("Arya")

#This is to explain the scope of variables
def eggCount():
    eggs = 31337
    print(eggs)
eggCount()
#print(eggs)-->This gives compilations error

#The local scope will not affect the scope of the other methods
def count():
    people= 99
    bacon()
    print(people)

def bacon():
    voter_id = 101
    people = 0
    print(people)

count()

#But local variables can read from the global variables. Here even though the value is not set
#It is fetching from the global variable.
def function1():
    print(value)
value=3
function1()
print(value)