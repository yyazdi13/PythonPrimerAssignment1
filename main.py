from datetime import date
from collections import Counter
import random
print("yasmin")
lyrics = "I'll stop the world and melt with you"
print(lyrics)
mylist = [1, 2, 3, 4, 5]
print(mylist)
math = 64 + 32
print(math)
x = 64
y = 32
mysum = x + y
print(mysum)
faveactress = "Jennifer Lawerence"
print(faveactress)
lucky = "My lucky number is %d" % 13
print(lucky[3:8])
today = date.today()
day = f"today's date is {today}"
print(day)
s = "today's date is %d/%d/%d" % (7, 6, 2016)
print(s)
str = "replace me me me"
print(str.replace("me", "this"))
print(str.replace("me", "twice", 2))
phrase = "this is a phrase this is"
print(phrase.replace("this is a phrase", "will this work"))
find = "SEnSiTive"
print(find.find("S", 1))
print("what color is the sky?")
answer = input()
print(answer.find("blue"))
words = ["this", "is", "a", "list", "of", "words"]
joinWords = "_,".join(words)
print(joinWords)
splitstr = "World,Earth,America,Canada"
print(splitstr.split(","))
print(phrase.split("this is"))
print(random.randint(0,100))
print(random.randrange(0,100))
print(random.randrange(0,100))
random = [1,1,1,2,2,3,3,3,4,4,4,4]
freq = Counter(random)
print(freq)
lang = input("fave programming language?")
print("really? " + lang + "??")
fave_num = input("fave number?")
num_range = [1,2,3,4,5,6,7,8,9,10]
if int(fave_num) not in num_range: print("invalid number")
else: print("ok!")
clist = ["Canada", "USA", "Mexico", "Australia"]
for x in clist:
  print(x)
for x in range(101):
  print(x)
for x in range(12):
  for y in range(12):
    print((x + 1) * (y + 1))
for x in reversed(range(11)):
  print(x)
for x in range(0,11,2):
  print(x)
start = 0
for x in range(100, 201):
  start += x

print(start)

i = 0
while i < len(clist):
  print(clist[i])
  i += 1

#while loops run while the condition is True
#yes, you can use a for loop inside of a while loop
#yes you can sum numbers inside while loops
def sum_list(list1):
  sum1 = 0
  for i in range(len(list1)):
    sum1 += (list1[i])
  print(sum1)
list1 = [1,2,3,4,5]
sum_list(list1)
#yes, functions can be called inside of another function
#yes, function can call another function (recursion)
#variables in a function can be used in another function only if they are returned

states = ["Montana", "New York", "Wyoming", "Texas", "Michigan","Mississippi"]
for i in states:
  if i[0] == "M":
    print(i)
y = [6,4,2]
y.extend([12,8,4])
print(y)
y[1] = 3
print(y)

def takefirst(elem):
    return elem[0]
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=takefirst)
print(x)

def takeSecond(elem):
    return elem[1]
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=takeSecond)
print(x)

my_list = list(range(1, 1001))
print(min(my_list))
print(max(my_list))

odd_list = []
even_list = []
for i in range(len(my_list)):
  if my_list[i] % 2 == 0:
    even_list.append(my_list[i])
  else:
    odd_list.append(my_list[i])
print(even_list)
print(odd_list)

countries = {'United States' : 'USA', 'Germany' : 'GER'}
for i in countries:
  print(i, countries[i])

f = open("demofile.txt", "w")
f.write("Take it easy")
f = open("demofile.txt", "r")
print(f.read())
f.close()

for i in range(3):
  for j in range(3):
    print(i,j)

persons = ["Adam", "Yasmin", "Evan", "Donna"]
for i in range(len(persons)):
  j = i
  while j < len(persons) -1:
    print(f"{persons[i]} met {persons[j+1]}") 
    j += 1
#A loop inside a loop is O^2 and something you want to avoid in the real world
pizzas = ["Hawaiian","Pepperoni","Mushroom","Margerita"]
print(pizzas[2:4])
string = "hello world"
print(string[6:11])

def func1(a,b):
  sum1 = a+b
  list1 = [a,b]
  return list1, sum1

print(func1(1,3))

def five_var(a,b):
  one = a
  two = b
  three = a + b
  four = a * b
  five = b - a
  return one,two,three,four,five
print(five_var(5,17))


def reduce_balance(balance):
  new_bal = balance - 100
  print(new_bal)
  return new_bal
reduce_balance(500)

today = date.today()
print("Today's date is:", today)

#Can try-except be used to catch invalid keyboard input?
#yes
#Can try-except catch the error if a file can‟t be opened?
#yes
#When would you not use try-except?
#when dealing with exceptions

#Can you have more than one class in a file?
#yes
#Can multiple objects be created from the same class?
#yes
#Can objects create classes?
#no, objects are instances of classes

class Car:
    def get_mileage(self): 
        return self._mileage 
      
    def set_mileage(self, x): 
        self._mileage = x 

    def noise(self):
        print('vroom vroom')
    
    def location(self):
      print("NYC")
Honda = Car()

#Add a variable age and create a getter and setter 
Honda.set_mileage(50000)  
print(Honda.get_mileage()) 
#Why would you use getter and setter methods?
#ensures data encapsulation, which avoids direct access to a specific variable 

#Import the math module and call the sin function
import math
print(math.sin(6))
#Create your own module with the function snake()
def snake():
  print("sssnake")
import main
main.snake()

#Create a new class that inherits from the class App
#class parent_class_name extends App - class header
#Try to create a class that inherits from two super classes (multiple inheritance)
class Class1:
    pass

class Class2:
    pass

class MultiClass(Class1, Class2):
    pass

#Can a method inside a class be called without creating an object?
#yes
#Why does not everybody like static methods?
#they don't have access to the attributes of an instance of a class, and they don't have access to the attributes of the class itself

#What is an iterable?
#An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method. 
#Which types of data can be used with an iterable?
#list , str , tuple, dict , file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements Sequence semantics

#What is a classmethod?
#A class method is a method that’s shared among all objects. Class methods can be can be called from instances and from the class itself
#How does a classmethod differ from a staticmethod?
#static method is not bound to any one class, while a class method is

#Do all programming languages support multiple inheritance?
#No (java)
#Why would you not use multiple inheritance?
#to prevent ambiguity of method names
#Is there a limit to the number of classes you can inherit from?
#no