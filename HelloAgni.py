"""
This is an example of the basic stuffs of python.
"""

#This is a comment
print ('Hello Agni. Your daddy has just started learning Python')

#data types
string="Hello Agni"
int=2
float=2.0
list=[1,2,3,'Hello Agni']

print(type(string), string)
print(type(int), int)
print(type(float), float)
print(type(list), list)

print(list[3])

# Getting a substring is super awesome
print(string[2:]) #llo Agni
print(string[:2]) #He
print(string[:-2]) # Hello Ag
print (string [-2:]) #ni
print(string[2:-2]) #llo Ag

#String concatenation and related stuffs 
message1="Hello"
message2=' Agni'

print(message1+ message2) 
print("Hello" " Agni") #this is also valid

print("Agni " *3)

print("Hello Arya"[0])# we can fetch the elements based on the index position like this

print(len("Hello Agni")) #len is used to find the lenghth

#format strings
print("{} is a {}".format("Agni", "great kid"))
print("{0} is {1} to {2}".format("Python","Awesome","learn"))
# You can use keywords if you don't want to count.
print("{name} loves {dogtype}".format(name="Agni", dogtype="labrador"))

# None is an object. we have to use is to check this
value="some value"
print(value is None) # False
value=None
print(value is None) #True

#getting the values from console
#valuesObtained=input("Enter any number: ")
#print(valuesObtained)

#list examples
nameList=["Arul","Aishu","Arya","Agni","Riya","Moni"] # we can prefill the list values.
print(nameList)

productList=[]
productList.append("Milk")
productList.append("Ghee")
productList.append("Butter")
productList.append(3)

print(productList)

productList.pop(3)
print(productList)

#slicing operation in list

print(productList[1:3])

print(productList[::-1])

#Adding two lists
print(nameList+productList)

#check if an element is present in a list or not

print("Arya" in nameList)

#length of the list
print(len(nameList))

#Tuples (It is just like List. But it is immutable)

tup=(1,2,3)
print(tup)
print(tup[0])

#tup[0]=5
#print(tup[0]) --> This willl give us error. 
#Because we are trying to change the tuple but it is immutable by nature. But we can change the list
#like this.
productList[0]="Vanaspati"
print(productList)

#unwrapping the tuples and lists
value1,value2,value3=(1,2,3)
print(value1,value2,value3)
listValue1,listValue2,listValue3=["a","b","c"]
print(listValue1,listValue2,listValue3)

#Get ready to be awesome, we have dictionary as a dataype in Python
myDictionary={} # empty dictionary

dictionaryWithValues={"Arul":"Genius", "Agni":"Intelligent"}

print(dictionaryWithValues["Arul"])

#fetch keys
print(dictionaryWithValues.keys())
#fetch values
print(dictionaryWithValues.values())
#fetch keys and values
print(dictionaryWithValues.items())

#set example. It is also like a list. but without duplicate data
set1={1,2,2,3} # result is 1,2,3
print(set1)
set1.add(4)
print(set1)

#Intersection operation
set2={3,6,7}
print(set1&set2) #3

print(set1|set2)

# Check data type of variable
type(set1)   # => set
type(myDictionary)   # => dict
type(5)   # => int

#If else if
number=10
if number > 10:
	print "Number is not greater than 10"
elif number == 10:
	print "Number is 10"
else :
	print "Number is less than 10"

#for loop example

for number in range (4):
	print number

for number in range(1,5):
	print number

#for iterate over a list
for name in ["Aishu", "Riya", "Moni", "Deepa"] :
	print ("{} is a girl".format(name))
