#!/usr/bin/env python
# coding: utf-8

# # 1. Variable

# ##### To set asside memory to be formatted in certain datatype to use in program;in python we don't specify the datatype

# ### Storing numbers

# In[1]:


shoe_size=10 #integer
shoe_size=10.5 # whole number


# ### Listing Keywords or reserved words - Cannot use as variable. to chcek keywords use this command:

# In[2]:


import keyword
print(keyword.kwlist)


# ### Strings - Sequence of zero or more characters

# In[3]:


name='Python'
name1="Python"


# ### Escape Sequence \" \t tab \n new line

# In[5]:


quote='This women is great,\"Cook\"\t and \"Artist\"\nHer charisma is extraordinary.'
print(quote)


# ## Multiple Assignment

# In[6]:


a,b=1,2
print(a)
print(b)


# # 2. Interactive programming

# In[9]:


value = input("Please enter your name: ") # Get the name from the user
print (value)
s


# In[8]:


age = int( input("Enter your age "))
future_age = age + 10
print (future_age)


# ### Numeric manipulation mathematical calculations+, -, * and / **to the power % modulus

# In[10]:


print (2 ** 2)
print (100 ** 10)


# ##### An import statement is a line of code that tells the computer that you're going to reference something in a particular library file

# In[11]:


import math

print ("The value of Pi is") 
print (math.pi)
print ("There's even another way to do power, with math.pow")
print (math.pow(4, 2) )


# ##### String Manipulation

# In[12]:


print ("New " + "York") 
word = "My words are important!"
print (len(word))
print ("and over " * 3) 


# ### Indexing
# Strings are just a collection of zero or more characters. Python enables you to access individual characters with a number or index. 

# In[13]:


phrase = "Python rocks"
print (phrase [0] )

phrase = 'p' + phrase [5:] 
print(phrase)


# ### Slicing
# If you provide two numbers, separated by a colon, you can get a range of characters out of the string. That’s known as slicing.

# In[14]:


phrase = "Python rocks"
print (phrase [1:3] )
print (phrase [7:] ) 


# 
# #### Math Library 
# MembersOpens in new window
# https://docs.python.org/3/library/math.html
# Here's a link to all of the members of the math library. The page includes the list of members, and some have short examples to show you how to use them.
# #### String Functions
# Opens in new window
# https://docs.python.org/3/library/stdtypes.html#string-methods
# This page shows all of the string functions that are available for you to use in your programs. The page shows the list of members, and some have short examples to show you how to use them.

# # 3. Decision

# #### If Statement
# if <condition>: #: important for ifcondition
#     <true statement> # same amount of indentation should be there for all lines thast are part of if
#  <Statement outside if>
#      
# Relation operator
#      
# 
# Less than	<
# Less than or equal to	<=
# Greater than	>
# Greater than or equal to	>=
# Equal to	==
# Not equal to	!=

# In[16]:


age = 10 #change to 10 to get 'ten' in print
if age == 10:
    print ("ten")
print ("how's that?")


# In[17]:


name = "me"   # with strings
if name == "me":
    print ("the same")


# In[18]:


letter = "E" # comparison is on Unicode basis, unicode is number assigned to each character in alphabets
if letter < "D":
    print ("less than D")
    print ("less than D line 2")
    print ("less than D")
print ("less than D not include in if")
a=10
b=20
c=a+b
print(c)
if letter > "B":
    print ("greater than B")


# #### The Else clause
# if <condition> :
#    < true statements >
# else:
#    < false statements >
# < statements outside the if structure >

# In[19]:


age = int(input("What is your age: "))
if age >= 18:
   print ("You are old enough to vote.")
   print("Line 2")
else:
   print ("You are not old enough to vote.")
   print("Line 3")


# In[20]:


year = int(input("Enter year: "))
if year == 1:
  print ("Freshman")
else:
  if year == 2:
     print ("Sophomore")
  else:
     if year == 3:
        print ("Junior")
     else:
        if year == 4:
           print ("Senior")


#  #### nested if and elseif for multiple conditions

# In[21]:


year = int(input("Enter year: "))
if year == 1:
  print ("Freshman")
else:
  if year == 2:
     print ("Sophomore")
  else:
     if year == 3:
        print ("Junior")
     else:
        if year == 4:
           print ("Senior")


# #### Elif and else

# In[22]:


year = int(input("Enter year: "))
if year == 1:
   print ("Freshman")
elif year == 2:
   print ("Sophomore")
elif year == 3:
   print ("Junior")
elif year == 4:
   print ("Senior")
else:
    print("Not valid year")


# #### Compound conditions

# In[25]:


age = int(input("How old are you? "))  # nested if
registered = input("Are you registered? (y/n) ").lower()

if age >= 18:
    if registered == "y":   # can use multiple conditions
         print ("You are ready to vote!")
else:
    print ("You are not ready to vote.")


# In[26]:


age = int(input("How old are you? "))     # and operator
registered = input("Are you registered? (y/n) ").lower()

if age >= 18 and registered == "y":
    print ("You are ready to vote!")
else:
    print ("You are not ready to vote.")


# In[27]:


year = int(input("How long have you been in fighting relationship "))     # and operator
registered = input("Are you single parent (y/n) ")

if year >= 1 or registered == "y":
    print ("You can get help!")
else:
    print ("You cannot get help")


# In[14]:


rate = int(input("What is your hourly wage? "))
hours = int(input("How many hours did you work? "))

if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate
    overtimeHours = hours - 40
    overtimePay = overtimeHours * (rate * 1.5)
    pay = pay + overtimePay
print(pay)


# Assignment
# Meteorologists use the Saffir-Simpson Scale to classify the strength of hurricanes. The intensity is based on the maximum sustained wind speed of a storm as follows:
# 
# Category	Wind Speed (mph)
# 1	74-95
# 2	96-110
# 3	111-130
# 4	131-155
# 5	156 and higher
# Write a Python program that will prompt the user for a wind speed. The program should use this wind speed to display a message telling the user the hurricane's intensity based on the table above.

# In[8]:


windspeed=int(input("Please enter the windspeedd in mph"))
if windspeed>=74 and windspeed<=95:
    print("It is category 1 hurricane")
elif windspeed>=96 and windspeed<=110:
    print("It is category 2 hurricane")
elif windspeed>=74 and windspeed<=130:
    print("It is category 3 hurricane")
elif windspeed>=74 and windspeed<=155:
    print("It is category 4 hurricane")
elif windspeed>=156:
    print("It is category 5 hurricane")
else:
    print("There is no hurricane")


# # 4. Looping - While and For
# While format 
# while < condition >:
#          < statements >
# For format
# for < variable > in < sequence >:
#          < statements >

# With the if statement, the code only runs once. With the while statement, just as you might expect, the code runs over and over until the condition becomes false.
# The for loop is essentially a shorthand version of the while loop.
# 
# Python creates this list and takes the first number (the value 1) out of the list and stores it in the number variable. Next, control enters the body of the for loop and the print statement is executed. Arriving at the end of the loop, Python goes back to the for statement and takes the next value (the number 2) out of the list and stores it in the number variable. This pattern continues until there are no more items in the list.
# 
# Unlike the while loop, notice how you don't need to worry about updating the variable so that some condition eventually becomes false. Instead, it just goes through every element in the list. Most important, it can't get stuck in an infinite loop.

# In[15]:


number = 1
while number <= 5: # called counter control loop
         print (number)
         number = number + 1    #must give to avoid infinite loop
         print ("hello!")
print ("Goodbye!")


# In[17]:


number = 1
answer = input("Are you a female y/n?")
while answer == 'y':
         print (number)
         number = number + 1
         answer = input(
                "Do you want the next number? ")


# In[18]:


for number in range(1, 6): # 6 is not part of answer
         print (number)


# In[19]:


for number in range(6): # will start number from 0
         print (number)


# In[20]:


for number in range(1, 6,2): # the last number is used as incrementing times
         print (number)


# In[21]:


for number in range(10, 0,-2): # the last number is used as descending times
         print (number)


# In[29]:


# accumulator variable. That’s a variable that holds the sum of all the numbers entered.
num_of_nums = int(input(
         "How many numbers do you want to average? "))
sum = 0.0
for count in range (num_of_nums):
    value = int(input("Enter a value: "))
    sum = sum + value
average = sum / num_of_nums
print ("The average is:", average)


# Assignment
# Write a program that reads in a list of numbers from the users and displays the sum and average of this list. Your program should enable the users to enter as many numbers as they wish. When the users are finished entering numbers, they'll enter the value -1. Be sure not to include the -1 in your calculations for the sum and average.

# In[46]:


sum=0.0
count=0
avg=0.0
num=int(input("Enter the numbers (-1 to quit)"))
while (num != -1):
     sum=num+sum
     num=int(input("Enter the numbers (-1 to quit) "))
     count=count+1
print("The sum of numbers is: ")
print(sum)
# This is necessary, in case the user doesn't enter any values
if(count!=0):
    avg= sum/count
print("the avg is: ")
print(avg)


# https://en.wikibooks.org/wiki/Python_Programming/Loops

# Nested loops

# In[47]:


for i in range(0, 10):
         print ("~~~", i, "~~~")
         for j in range(0, 10):
                   print (i*j)
         print ( )


# Compoud consitions
# while a=='y' or 'Y' #Here 'Y' is considered as boolean and will run for any true value
# Break statement - By placing the word break inside your loop, you force the program to stop at that exact point and exit the loop.
# Continue Statement - The continue statement enables you to skip the remaining statements in your loop and start a new one.

# In[48]:


for number in range(1, 11):
         if number == 4:
                   break
         print (number)
print ("Thanks!")


# In[49]:


for number in range(1, 11):
         if number == 4:
                   continue
         print (number)
print ("Thanks!")


# In[55]:


for number in range(1, 11):
         if number == 4:
                   continue
         print (number)
         if number == 9:
                    break
else:
         print ("Exited normally")


# In[1]:


list_num=[]
for i in range(0,100,2):
    list_num.append(i)
list_num


# In[57]:


phrase = input("Enter a phrase: ") # to find if letter exists in a phrase or not
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
         if phrase [index] == letter:
                   print ("The letter first appears at index: ", index)
                   break
else:
         print ("Your letter wasn't found")


# # Function - A function provides a way to name and group a set of Python statements and run anytime needed.
# # def < function name > ( < parameter list >):
#     < documentation string >
#     < the function's code >
#     
#   

# In[5]:


def print_welcome():
    """This function prints two lines of text"""
    print ("Welcome to my program")
    print ("I hope you like it")
      
print_welcome()
      


# In[6]:


def print_value(value):
    """This function prints the value passed in"""
    print ("Your value is:", value)  
    
print_value(5)
print_value("number")

name = "Pat"
print_value(name)


# In[7]:


# changing value
# with local variable the variable is only used in that function and not outside
def change_value(value): 
    """This function changes the value passed in to 1"""
    print ("Inside, value is:", value)
    value = 1
    print ("Inside, value is changed to:", value)

number = 5
print ("Outside, number is:", number)
change_value(number)
print ("Outside, number is now:", number)


# In[2]:


# global variable-  the variable is  used in and outside that function
def change_number():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1

number = 5
print ("Outside, number is:", number)
change_number()
print ("Outside, number is now:", number)


# In[13]:


def square(num):
    """This function calculates the square of a number"""
    result = num * num
    return result
for i in range(1,11):
    print (square(i))


# In[5]:


def square(num = 3):
    """This function calculates the square of a number"""
    result = num * num
    return result
print (square( ))


# In[13]:


def prompt_user(prompt, num_tries = 2):
    """This function prompts the user a certain number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)
#prompt_user(prompt="Hello ")
prompt_user(num_tries=3, prompt="Hi. Go again? ")


# Write a Python program that will print a table of Celsius temperatures and their Fahrenheit equivalents between 0 and 100 Celsius in increments of 10 degrees. Your program should include a function named convert_to_fahrenheit that takes a Celsius temperature and returns the corresponding Fahrenheit temperature.
# 
# The formula used to convert a Celsius temperature to a Fahrenheit temperature is this:
# 
# Fahrenheit = 9.0/5.0 * Celsius + 32
# 

# In[36]:


#C = int(input("Celius value"))
def convert_to_fahrenheit(celsius):
    """This function converts celsius to Fahrenheit"""
  #  global F
    fahrenheit = 9.0/5.0 * celsius + 32
    return fahrenheit
    

for cel in range(0,101,10):    
    print("C = ", cel," and F = ", convert_to_fahrenheit(cel) )
    

    


# # class
# A class is a way to group code, but it's more than that. A class gives you the ability to write a specification, or blueprint, for how an object created from this class should look and behave.

# In[28]:


class Time:
    """ Blueprint for a Time object"""
    def __init__(self):
        self.hour = 00
        self.minute = 0
        self.second = 0
            
    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print_time(self):
        print (self.hour, ":", self.minute, ":", self.second)

# from Time import Time  #- used to create 2 files , 1 to create object  and other to do rest of the things

# First Time object
myTime1 = Time()
myTime1.print_time()
myTime1.set_time(1, 2, 3)

# Second Time object
myTime2 = Time()
myTime2.set_time(12, 0, 0)

print ("My two time objects are now storing:")
myTime1.hour=50
myTime1.print_time()
myTime2.print_time()



# In[51]:


#Name Mangling - to avoid direct accesing the class variables

class Time:
   """ Blueprint for a Time object"""
   def __init__(self):
      self.__hour = 0
      self.__minute = 0
      self.__second = 0

   def set_time(self, hour, minute, second):
      self.__hour = hour
      self.__minute = minute
      self.__second = second

   def print_time(self):
      print (self.__hour, ":", self.__minute, ":", self.__second)

   def set_second(self, second):
      self.__second = second

   def get_second(self):
      return self.__second
 
myTime1 = Time()
#print(myTime1.__second) 
# to make it run use print(myTime1._Time__second)  

# attributes to print the name of the file
print (myTime1.__doc__) 
print (Time.__doc__)

# shows the module name, followed by a dot and then the class name.
print (myTime1.__class__)


# The two underscore characters for its variable names to restrict access as much as possible.
# A getter and setter function for each of the hour, minute, and second variables. Be sure the set functions do the error checking necessary to insure valid times.
# A function named tick( ) that will increment the number of seconds by 1. Be aware that this function will need to check to be sure that you haven't moved to the next minute or hour.
# When you're finished with your new and improved Time class, write a short Python program that creates a Time object and works with some of the functions. Inside this program, you might consider writing a loop and placing a call to the tick function to watch your time move forward.

# two underscore
# A getter and setter function for each of the hour, minute, and second variables.
#  error checking necessary to insure valid times.
#   tick( ) that will increment the number of seconds by 1.

# In[22]:


class Time:
    """ Blueprint for a Time object"""
    def __init__(self):  # Define variables
        self.__hour = 0
        self.__minute = 0
        self.__second = 0


    def tick(self):# clock tick
        self.__second = self.__second + 1
        if (self.__second == 60):
            self.__second = 0
            self.__minute = self.__minute + 1
            if (self.__minute == 60):
                self.__minute = 0
                self.__hour = self.__hour + 1
                if (self.__hour == 24):
                    self.__hour = 0

        
    def set_time(self, hour, minute, second):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_second(second)
        

    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

        
    def set_hour(self, hour):
        if (hour>=0 and hour<=23):
            self.__hour = hour
        else:
            self.__hour = 0
    
    def set_minute(self, minute):
        if (minute>=0 and minute<=59):
            self.__minute = minute
        else:
            self.__minute = 0
        
    def set_second(self, second):
        if (second>=0 and second<=59):
            self.__second = second
        else:
            self.__second = 0    

    def get_hour(self):
        return self.__hour
    def get_second(self):
        return self.__second
    def get_minute(self):
        return self.__minute

# Main program
myTime = Time()
myTime.set_time( 23, 59, 45)



for i in range(20):
    myTime.print_time()
    myTime.tick()


# # Tkinter

# In[28]:


from tkinter import *
frame01=Frame()
frame01.mainloop()


# In[30]:


from tkinter import *
from time import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

# to call the functions
frame02 = MyFrame()
frame02.mainloop()


# In[1]:


from tkinter import *
from time import * # for pause and upadte

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        
        self.myCanvas = Canvas(width=300, height=200, bg="pink") # to call the shapes
        self.myCanvas.grid() # load manager to place the shapes
        self.myCanvas.create_rectangle(10, 10, 100, 100) # to create rectangle
        self.myCanvas.create_rectangle(10, 10, 200, 100, outline = "red", fill = "blue") # to create rectangle
        self.myCanvas.create_oval(10, 10, 200, 100, fill="white")
        self.myCanvas.create_line(1, 1, 200, 200, arrow="last") # first", "last", and "both" for placement of arrow
        #self.myCanvas.create_text(50, 50, text="Hello World",anchor = "s")
       # self.myCanvas.create_text(50, 50, text="good", anchor = "center")# give anchor to decide the direction - cntre, n,w,e,s,ne etc
      #  self.myCanvas.create_text(1, 1, text="Hello World", width=70, fill="red", anchor="nw",  justify="center", font=("Times", 16))
        self.myCanvas.create_arc(10, 10, 100, 100) # to create rectangle   
        self.myCanvas.update()   
        sleep(1) # to pause execution
        
        for count in range(10):
            increment = 10*count
            self.myCanvas.create_rectangle(10 + increment, 10 + increment, 50 + increment, 50 + increment)
            self.myCanvas.update()
            sleep(1)
           
        
# to call the functions
frame02 = MyFrame()
frame02.mainloop()



# In[4]:


from tkinter import *
from time import *

class MyFrame(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.myCanvas = Canvas(width=300, height=200, bg="white")
		self.myCanvas.grid()

		for count in range(10):
			increment = 10*count
			self.myCanvas.create_rectangle(10 + increment,
				10 + increment, 50 + increment, 50 + increment)
			self.myCanvas.update()
			sleep(1)

			# Now color over the previous rectangle
			self.myCanvas.create_rectangle(10 + increment,
				10 + increment, 50 + increment, 50 + increment,
				outline="pink")

frame02 = MyFrame()
frame02.mainloop()


# In[1]:


from tkinter import *
from time import *

class MyFrame(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.myCanvas = Canvas(width=300, height=200, bg="white")
		self.myCanvas.grid()

		my_rect_id = self.myCanvas.create_rectangle(10, 10, 50, 50, outline="purple")
		self.myCanvas.update()

		for count in range(10):
			increment = 10*count
			self.myCanvas.coords(my_rect_id,
				10 + increment, 10 + increment,
				50 + increment, 50 + increment)
			self.myCanvas.update()
			sleep(1)

frame02 = MyFrame()
frame02.mainloop()


# Rainbow arc

# In[44]:


from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=500, height=500, bg="Skyblue")
        self.myCanvas.grid()
      
        my_arc_id = self.myCanvas.create_arc(200, 200, 360, 360, outline="blue",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(180, 180, 380, 380, outline="lightgreen",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(160, 160, 400, 400, outline="yellow",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(140, 140, 420, 420, outline="orange",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_arc_id = self.myCanvas.create_arc(120, 120, 440, 440, outline="red",style = "arc",start=0, extent=180,width = 20)
        self.myCanvas.update()
        sleep(1)
        my_rect_id = self.myCanvas.create_rectangle(0, 500, 500, 280,outline="green", fill="green")
        self.myCanvas.update()
        sleep(1)
        my_circle_id = self.myCanvas.create_oval(0, 180, 40, 220,outline="orange", fill="orange")


frame02 = MyFrame()
frame02.mainloop()


# # Data Structures

# 

# In[2]:


days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print (days_of_week [2] )


# In[7]:


for count in range(7):
  print (days_of_week [count] )
len(days_of_week)


# In[8]:


for count in range(len(days_of_week)):
    print(days_of_week [count])


# In[9]:


days_of_week [0] = "Sunday"


# In[10]:


print(days_of_week)


# In[11]:


print(days_of_week [2:5])


# In[14]:


# Nesting
child1 = ['Pat', 5, 6.5]
family = [child1]
print (family [0] [1] )


# In[17]:


# to add to list
my_list = [ ]
my_list.append(10)
my_list.append('ten')
my_list


# In[38]:


# to add multiple items in list
my_list.extend(['twenty',20])
my_list


# In[39]:


my_list = my_list + [30, 'thirty']
my_list


# In[29]:


my_list


# In[47]:


# to add at specific index
my_list.insert(3, 'hi there!')
my_list


# In[46]:


# to remmove from list
my_list.remove('hi there!')
my_list


# In[ ]:


my_list.pop()


# In[48]:


my_numbers = [16, 8, 15, 42, 23, 4]
print ( max(my_numbers))


# In[44]:


student = [["Name","A","B","C","D","E"],
          ["MK",23,45,67,89,78],
          ["GK",54,43,23,65,76],
          ["SK",56,78,90,32,45],
          ["TK",45,78,97,54,37]]

# student marks
student_marks = [['Name',  ['A','B','C','D','E']],
                 ['Ankit',  [41, 34, 45, 55, 63]],
                 ['Aravind',[42, 23, 34, 44, 53]],
                 ['Lakshay',[32, 23, 13, 54, 67]],
                 ['Gyan',   [23, 82, 23, 63, 34]],
                 ['Pranav', [21, 23, 25, 56, 56]]
                ]


# In[47]:


name = student_marks[1][1]
name1 = student[1][1]
print(name1)


# In[48]:


studentsWithB = []

#PRint b marks
for marks in student_marks[1:]:
    name = marks[0]
    marks_in_B = marks[1][1]
    studentsWithB.append([marks_in_B,name])
print(studentsWithB)

    
    


# In[49]:


sorted(studentsWithB)


# In[ ]:


print(studentsWithB)


# In[52]:


studentsWithB = []

#PRint b marks
for marks in student[1:]:
    name = marks[0]
    marks_in_B = marks[2]
    studentsWithB.append([marks_in_B,name])
print(studentsWithB)


# In[53]:


sorted(studentsWithB)


# In[54]:


sorted(studentsWithB, reverse=True)


# In[3]:


from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=300, height=200)
        self.myCanvas.grid()
        
        my_font = ("Times", 16)
        self.myCanvas.create_text(50, 50, text="First",
        font=my_font)
        self.myCanvas.create_text(80, 80, text="Second",
        font=my_font)

frame02 = MyFrame()
frame02.mainloop()


# In[2]:


from tkinter import *

class MyFrame(Frame):
   def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=300, height=200)
        self.myCanvas.grid()
        self.myCanvas.create_text(1, 1, text="Hello World", width=70, fill="blue", 
                                  anchor="nw", justify="center", font=("Times", 16))
        
        
frame02 = MyFrame()
frame02.mainloop()


# In[4]:


from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=150, height=150, bg="white")
        self.myCanvas.grid()

        self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
        self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
        self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

        print ("Finds all shapes")
        print (self.myCanvas.find_enclosed(0, 0, 30, 70))

        print ("Finds middle shape")
        print (self.myCanvas.find_enclosed(0, 25, 30, 45))

    
        print ("Finds no shapes")
        print (self.myCanvas.find_enclosed(0, 0, 1, 1) )

frame02 = MyFrame()
frame02.mainloop()


# Assignment
# Write a program that computes the average of a series of numbers entered by the user. To make the program more user-friendly, store all the numbers in a list so that the user's numbers can be displayed before the average appears. Have your program stop accepting values when the user enters the value -999. Note that this value, -999, should not be averaged in with the other numbers.
# 
# Sample output from your program might look like the following:
# 
# Please enter a number (-999 quits): 1
# Please enter a number (-999 quits): 2
# Please enter a number (-999 quits): 3
# Please enter a number (-999 quits): 3
# Please enter a number (-999 quits): -999
# Using the numbers:
# 1 2 3 3 
# The average is: 2.25

# In[25]:


number_list = []
sum = 0


user_number = int(input("Please enter a number: "))

while (user_number != -999):
    number_list.append(user_number)
    sum = sum+user_number
    user_number = int(input("Please enter a number: "))

if (len(number_list)!=0):
    avg = sum/len(number_list)
    print("The average is",avg)
else:
    print("There are no numbers")

print("The list is",number_list)


        
    


# In[57]:


#set
myset = {1,2,3,1,2,3}
print(myset)


# In[59]:


myset.add(4)
print(myset)


# In[60]:


myset.discard(1)
print(myset)


# In[62]:


myset.remove(2) -  will throw error if the value is not present


# In[63]:


# convert tuple to set
mytuple =('a',2,5,6,8,'b',2,5,6,8) 
myset=set(mytuple)
print(myset)


# In[ ]:


myset.insection(otherset)


# In[ ]:





# In[ ]:





# In[ ]:





# # dictionary
# dict={}

# In[61]:


dict={1:"a",2:"b",3:"C"}
print(dict)  # print complete dictionary
print (dict.keys())
print (dict.values())


# In[62]:


print(dict[1] )


# In[28]:


print (dict.items()) 3 print key and value pairs as tuple


# In[29]:


print(2 in dict)# to chcekl the presence


# In[59]:


#del dict[1]
print(dict[1])


# In[32]:


my_dictionary = { }

days_in_month = {'Jan':31, 'Feb':28, 'Mar':31} 
days_in_month2 = {'Apr':30, 'May':31, 'Jun':30}
days_in_month.update(days_in_month2)
print(days_in_month.items())


# In[42]:


#remove

print(dict)


# In[49]:


odds = {1:'one', 3:'three', 5:'five'}
evens = {2:'two', 4:'four', 6:'six'}
odds.clear()

print ("After clearing odds:")
print (odds)

del evens
print ("After clearing evens:")
print (evens)


# In[50]:


days_in_month = {}
print (days_in_month.get('January'))
print (days_in_month.get('January', 'January not present'))


# In[53]:


dict = {}
print(dict.get('1')) # if it doesnot have value
print(dict.get('1','2')) # if display the value


# In[57]:


words = {}
value = input("Please enter a word (or -999 to quit): ")
while (value != '-999'):
    if value in words:
        words[value] = words[value] + 1 # equating the key in dictionary to its value
    else:
        words [value] = 1

    value = input("Please enter a word (or -999 to quit): ")

for current_key in words.keys():
    print (current_key, '\t', words [current_key] )


# In[64]:


print ()
print ("Ordered by number of times entered:")
temp_list = []
# Select a key in the dictionary
for current_key in words.keys():
    # determine the number of words in the sorted list
    list_length = len(temp_list)

    # start looking at position 0
    placeholder = 0

    # As long as there are still items in the list
    while placeholder < list_length:
        # Get the word in the sorted list
        list_key = temp_list [placeholder]

        # Determine if this word has been entered
        # more times than the current word
        if words [list_key] > words [current_key] :
            break

        # It wasn't, so let's look at the next word
        # in the sorted list
        placeholder = placeholder + 1

    # We found the location in the sorted list for
    # this word, insert it
    temp_list.insert(placeholder, current_key)

for current_key in temp_list:
    print (current_key, '\t', words [current_key] )


# Write a program that stores information about student test grades in a dictionary. Your program should prompt the user for the student's name and score. Once the user is finished entering grades, allow them to search the dictionary for a particular student and print their score.

# In[ ]:


# Introduction to Python Programming
# Lesson 09 Assignment
# Sample Solution

test_scores = { }
name = input("Please enter a student name (-999 quits): ")

while name != '-999':
    score = eval(input("Please enter the students score: "))
    test_scores[name] = score

    print()
    name = input("Please enter a student name (-999 quits): ")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
search_name = input("Which student's score would you like to see (-999 quits): " )

while search_name != '-999':
    if search_name in test_scores:
        print (search_name, "\t", test_scores[search_name])
    else:
        print (search_name, "not found in list")

    print()
    print()

    search_name = input("Which student's score would you like to see (-999 quits): " )


# # External Data Files

# In[73]:


out_file = open('C:/Users/manpr/Documents/PythonJupyter/Text-file.txt', 'w') # open new file in write mode


# In[77]:


out_file.write("This is test 1\n") # Write single string


# In[3]:


weekend = ['Saturday','Sunday']
out_file.writelines(weekend)  # write multi[pel lines


# In[81]:


out_file.flush( ) # to post


# In[82]:


out_file.close( ) # to close the file


# In[90]:


in_file = open('C:/Users/manpr/Documents/PythonJupyter/Text-file.txt', 'r') # open new file in read mode


# In[2]:


print("```````read no of chars")
#print(in_file.read(10))
print("```````read````````")
# print(in_file.read( ))
print("```````readline````")
#print(in_file.readline())
print("```````readlines````")
print(in_file.readlines( )) # in form of array


# In[92]:


in_file.close( ) # to close the file


# In[2]:


out_file = open('/Users/Manpreet/Documents/ProgramsPython/text.txt', 'a') # open new file in append mode 
#it'll keep all the existing data and add in the new data at the end of the file


# In[9]:


out_file.write('\nkick')
out_file.flush( )


# In[12]:


# r+ and w+ to read and write; w+ will craete a non existing file
out_file.tell( ) # tell no of bytes


# In[11]:


out_file.seek(10) # to move curson to specified char length


# In[15]:


in_file = open('/Users/Manpreet/Documents/ProgramsPython/text.txt', 'r+')
print (in_file.readline())
in_file.seek(0)
in_file.write('Hi!')
in_file.seek(0)
print (in_file.readline())
in_file.close()


# # Pickle
# The pickling process simply converts an object to a stream of bytes. This stream can then be reconverted to the original object later. This is a useful thing to do for a couple reasons. First, by converting to a string of bytes, we’ll actually save a little bit of space on the disk. But possibly more important than this, is that we can store an entire object using just a single line of code. That is, without the ability to use pickle, we would need to store every field of an object one at a time in the file, and then when we restored the data, we would need to read in each piece of data and create a new object. Even for something like an object from our little Time class, we’re talking about replacing three lines of code: one for each of the hour, minute, and second, into a single line.
# dumps( ), if you want to store the result in a string. The other function, dump( ), stores the result in a file.

# In[25]:


class Time:
    """ The blueprint for a Time Class object"""
    def __init__ (self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

import pickle
from Time import Time

myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
print (pickled_time)


# In[31]:


class Time:
    """ The blueprint for a Time Class object"""
    def __init__ (self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

import pickle
from Time import Time

myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
print (pickled_time)


# In[ ]:


#pickle to file
#dumps( ), if you want to store the result in a string. The other function, dump( ), stores the result in a file.

myTime1 = Time(1, 2, 3)
out_file = open('data.txt', 'wb')
pickled_time = pickle.dump(myTime1, out_file)
out_file.close()


# In[ ]:


# pickle from file
#loads( ) or the load( ) - the first unpickles from a string and the second from a file.
import pickle
from Time import Time
myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
unpickled_time = pickle.loads(pickled_time)
unpickled_time.print_time()


# In[33]:


import shelve
db_file = shelve.open('/Users/Manpreet/Documents/ProgramsPython/letters', 'c') # c to open shelve file
db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file ['end'] = ['x', 'y', 'z']
db_file.close()


# In[34]:


import shelve
db_file = shelve.open('/Users/Manpreet/Documents/ProgramsPython/letters.txt', 'c')
print ( list(db_file.keys( )))
print ("Original containing vowels:", 'vowels' in db_file )
del db_file ['vowels']
print ("After deleting vowels:", 'vowels' in db_file )
print ( list(db_file.keys( )))
db_file.close()


# In[35]:


# If you want to immediately write the data, you can use the sync( ) function.


# In[ ]:


# Revise your program from the Lesson 9 Assignment so that it stores the student grades in a shelf file. 
#Remember, this program should prompt the user for the student's name and score. 
#After the user has finished entering grades, allow them to search that file for a particular student's score.


# In[1]:


# Introduction to Python Programming
# Lesson 10 Assignment
# Sample Solution

import shelve

test_scores = shelve.open('/Users/Manpreet/Documents/ProgramsPython/student_scores.txt', 'c')
name = input("Please enter a student name (-999 quits): ")

while name != '-999':
    score = eval(input("Please enter the students score: "))
    test_scores[name] = score

    print()
    name = input("Please enter a student name (-999 quits): ")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

search_name = input("Which student's score would you like to see (-999 quits): " )

while search_name != '-999':
    if search_name in test_scores:
        print (search_name, "\t", test_scores[search_name])
    else:
        print (search_name, "not found in list")

    print()
    print()

    search_name = input("Which student's score would you like to see (-999 quits): " )

test_scores.close()



# # try catch

# In[4]:


value = eval( input("Enter a number: ") ) # dynamically evaluate expressions.accept int and float


# In[6]:


try:
   age = eval( input('Please enter your age: ') )
   ten_years = age + 10
   print ("In 10 years, you'll be", ten_years)
except NameError:
   print ("You must enter a number for your age")

print ("Have a nice day. Goodbye.")


# In[12]:


try:
   age = eval( input("Please enter your age: ") )
   ten_years = age + 10
   print ("In 10 years, you'll be", ten_years)
except NameError:
   print ("You must enter a number for your agehj")
except SyntaxError:
   print ("You must enter a number for your age")

print ("Have a nice day. Goodbye.")


# In[ ]:


try:
   age = eval( input("Please enter your age: ") )
   ten_years = age + 10
   print ("In 10 years, you'll be", ten_years)
except (NameError, SyntaxError):
   print ("You must enter a number for your age")

print ("Have a nice day. Goodbye.")


# In[13]:


#A NameError is an exception that comes up when Python encounters a variable name that it doesn't recognize.
#The 10ten input generates a SyntaxError, and because this is a different kind of exception, Python doesn’t run the exception code.

try:
   age = eval( input("Please enter your age: ") )
   ten_years = age + 10
   print ("In 10 years, you'll be", ten_years)
except NameError:
   print ("A NameError has occurred")
except Exception:
   print ("Something unexpected has happened")

print ("Have a nice day. Goodbye.")


# In[19]:


# the IndexError and NameError arguments contain a message that give you a single line of text to describe what happened
try:
   my_list = [0, 1, 2]
   print (my_list [5])
except IndexError as ie:
   print (ie)


# In[18]:


#IOError gives you a variety of properties to give us details about what's going on.
try:
   infile = open('dataFile.txt', 'r')
   infile.write("hello")
   infile.close()
except IOError as ioe:
   print ("filename:", ioe.filename)
   print ("strerror:", ioe.strerror)


# In[20]:


dir(IOError ) # all ioerror


# In[23]:


# else
try:
   user_num = eval( input("Please enter a number: ") )
   result = 10 / user_num
except (NameError, SyntaxError):
   print ("The value you entered was not a number")
except ZeroDivisionError:
   print ("You cannot divide by zero")
else:
   print ("The result of dividing 10 by your number is", result)


# In[27]:


# finally. - This block is where you'll place code that you want to be run whether an exception occurs or not.
try:
   infile = open('/Users/Manpreet/Documents/ProgramsPython/text.txt', 'r')
   try:
       value = infile.readline()
       number = int(value)
       print (number)
   finally:
       infile.close()
       print ("the data file was closed")
except IOError as io:
   print ("Could not open file:", io.filename)
except ValueError:
   print ("Could not convert", value, "to a number")


# Assignment
# Two other exception types Python gives us are the OverflowError, which happens when a floating-point number (a number with a decimal point) is too big to be stored in memory, and the KeyboardInterrupt, which occurs when the user presses CTRL + C.
# 
# Use the following infinite loop code segment inside a try block. Write two except statements: one for each of OverflowError and KeyboardInterrupt. Have the code inside your except statements print the value of number so that the user will know how far the loop progressed before the exception occurred.
# 
# counter = 1
# while (counter >= 1):
#    number = 2.0 ** counter
#    counter = counter + 0.001

# In[28]:


# Introduction to Python Programming
# Lesson 11 Assignment
# Sample Solution

try:
    counter = 1
    while (counter >= 1):
        # This code simply prints the number and
        #   is for debugging purposes
        #print (counter)

        # A second set of code
        # This code will raise 2^counter
        result = 2.0 ** counter

        # I used the following line for debugging
        #   purposes for the second case
        #print ("2 ^", counter, "=\t", result)

        counter = counter + .001
except OverflowError:
    print ("\n\nOverflowError: You stopped the program with counter =", counter)

except KeyboardInterrupt:
    print ("\n\nKeyboardInterrupt: You stopped the program with counter =", counter)

    # This is the output I used for the 2^number code
    #print ("\n\nKeyboardInterrupt: You stopped the program with result =", result)



# #Tkinter

# In[ ]:


#Labels display text or an image to the user; they provide a way for your program to deliver output to the interface.
from tkinter import *

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.grid()

       self.message = Label(self, text = "Hello World!")
       self.message.grid()

frame01 = MyFrame()
frame01.mainloop()


# In[ ]:


#title
self.master.title("My GUI")


# In[ ]:


# change size
self.master.geometry("250x200")


# In[ ]:


from tkinter import *

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("250x200")
       self.master.title("My GUI")
       self.grid()

       self.button_click_here = Button( self, text = "Click Here",
           command = self.click_here_click )
       self.button_click_here.grid()

   def click_here_click(self):
       print ("You did it!" )

frame02 = MyFrame()
frame02.mainloop()


# In[ ]:


#add spacing 
self.button_submit.grid(columnspan = 2, pady = 10)


# In[29]:


from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Text Sampler")
        self.grid()

        self.sample_label = Label(self, text="Some Sample Text", font = "Courier 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 1, column = 1)

    def set_font(self):
        new_font = "Courier 10"

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
       
        self.sample_label.config( font = new_font)

frame04 = MyFrame()
frame04.mainloop()



# In[ ]:


#Radio button
self.ten_point = Radiobutton(self, text = "10 point",
   variable = self.point_size, value = "10",
   command = self.set_font)


# In[ ]:


#multiple radio buttons
self.family = StringVar()
self.times = Radiobutton(self, text = "Times",
   variable = self.family, value = "times",
   command = self.set_font)
self.times.grid(row = 3, column = 0)


# In[30]:


# Introduction to Python Programming
# Lesson 12 Assignment
# Sample Solution

from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x300")
        self.master.title("Lesson 12 Assignment")
        self.grid()

        # Prompt, Entry and Button
        self.prompt = Label(self, text = "Enter your text: ")
        self.prompt.grid(row = 0, column = 0)
      
        self.input = Entry(self)
        self.input.grid(row = 0, column = 1)

        self.button_submit = Button( self, text = "Submit",
                                       command = self.submit_click )
        self.button_submit.grid(row = 0, column = 2)

        # Display the text here
        self.my_text = StringVar()
        self.my_text.set("Enter your text above")
        self.message = Label(self, textvariable = self.my_text, font = "Courier 8")
        self.message.grid(row = 1, columnspan = 3, pady = 20)

        # Now for the options
        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 2, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)

        self.check_underline.grid(row = 2, column = 1)

        # And the font sizes
        self.point_size = StringVar()
        self.point_size.set("8")
        self.eight_point = Radiobutton(self, text = "8 point",
                variable = self.point_size, value = "8",
                command = self.set_font)
        self.eight_point.grid(row = 3, column = 0)

        self.ten_point = Radiobutton(self, text = "10 point",
                variable = self.point_size, value = "10",
                command = self.set_font)
        self.ten_point.grid(row = 3, column = 1)
      
        self.twelve_point = Radiobutton(self, text = "12 point",
                variable = self.point_size, value = "12",
                command = self.set_font)
        self.twelve_point.grid(row = 3, column = 2)

    def set_font(self):
        new_font = "Courier"

        if self.point_size.get() == "8":
            new_font = new_font + " 8"
        elif self.point_size.get() == "10":
            new_font = new_font + " 10"
        else:
            new_font = new_font + " 12"
      
        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
       
        self.message.config( font = new_font)

    def submit_click(self):
        self.my_text.set(self.input.get())

asn_frame = MyFrame()
asn_frame.mainloop()



# In[ ]:




