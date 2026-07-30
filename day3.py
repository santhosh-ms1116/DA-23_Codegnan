#numeric datatype -->int,float,comlex along with boolean
#input formating -->accepting input from the user-->input()

#accepting integr input from user
#by default input ()accepts any input -->str
#int (input())-->will accept only integers
'''age= int(input('enter the age:'))
print(age)
print(type(age))

#float (input())-->accepts integrs,float values
age= float (input('enter the age:'))
print(age)
print(type(age))

#accepting string input from user

name =input ("enter the name :")
print(name)
print(type(name))

#accept group of values

marks =int(input("enter the marks:"))
print(marks)

a=input().split() #now you enter spaces in output
print(a)
#comma separated value
a=input ("enter the values :").split(',')
print(a)

#list of integers
marks =list(map(int,input("enter the values ").split(',')))
print(marks)

#now we want to accept 2 values from user
age,salary = map(int,input("enter the values ").split(','))
print(age)
print(salary)

#single input -->int(input))
#two inputs-->a,b=map(int,input().split(','))
#any numbers results as list --> a=list(map(int,input().split(','))

#float of integers
marks =list(map(float,input("enter the values ").split(',')))
print(marks)

#group of float values
age,salary = map(float,input("enter the values ").split(','))
print(age)
print(salary)

#accepting input from user --> int,float -> input formating

#operators --> operators perfrom operators between values (operands )
#7 types --> arithmetic ,assignment, comparision (realationship)
#membership, identity ,logical bitwise

#arithemetic operators --> arithmetic operations
#+,-,*,/
print(5+3)
print(6-6)
print(2*8)
print(2/5)#float value
#floor division (interger division)--> returns quotient
print(5%4)
#power (exponential)
print(2**4)

#task -->accept interger input as length ,breadth --> find area of rectangles
#area =length *breadth
length, breadth =map(int,input("enter  the values:").split(','))
area =length *bredath
print(area)

#assignment operators --> assidn the values
#=,+,-=
a=45
print(a)
#update the value of a
a=a+5 #a+=5
print(a)
b=35
b+=a
print(b)
b-=5
print(b)


#task :*=,/=,//=,%=,**=workout
#copmarision operators --> we compare the values --> boolean
#==(equal to),!=not eual to),<(less than),>(greater than)
#<=(less than or equal to)>(greater than or equal to)

age =25
print(age==25)#returns boolean output
print(age!=35)
print(age<25)
print(age<=35)
print(age>35)
print(age>=35)
print (-5<-1)

#membership operators --->in,not in
#it checks for the existance of an object in a collection
marks=[56,75,45,85]
print(35 in marks)
#print(35 in 335)#type error
print(25 not in marks)
print('mani' in 'manikumar')
print('$' in 'adsa$dd')


#logical operators ---> logical decision making ---> and,or,not
#and---> all conditions to be satisfied
#or ---> any one condition to be satisified

a=(25 in [25,45,65]) and 45 <56
print(a)
b= 45>56 or 25<=45
print(b)
c=not(True)
print(c)
'''
#identity operators --->check for identity of an object --->id()
#is ,is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)

a=[1,3,4,5]
print(id(a))
c=a
print(c is a)
b=[1,3,4,2,5]
print(id(b))



















