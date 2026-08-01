

#identity operators --> chckes the identity of objictes -->id()

'''
a=4
b=2
  print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5==5)


a=[1,2,3,4]
b=a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))

#as  we have lists(mutable collection)both c and a lists will have different
#ids wheras values are same
print(c is a) #output is false
print(c==a) #output true
print(a is not c)

# bitwise operators --> we perform bitwise operators over operands
#&(and),|(or),^(xor),shifting operators(<<,>>)
#number will be coverted to binary format

print(5&3) #both 5 and 5 to be coverated binary and bitwise and is performed

print(5|4)#bitwise or

print(5^3) #bitwise xor

print(5 and 3) # here and is logical opetores checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case


#leftshift operator << ,right shift opertors
print(5<1) #false comparison
print(5 <<1)
print(5>>1) #rigth shift operations


print(15<<2) covert 15 to binary and perfrom 2 times left shifting

print(15>>2) #same 2 times rigth  shifting

# input formatimg  --> input(),int(input()),float (input())
#you know -->single input
#2 or 3 inputs --> maps()
#group of ingerers --> list (map(int,input().split(','))

name =input("enter the name:").split(',')
print(name)

name1,name2 =map(str,input("enter the friends names:").split(','))
print(name1,name2)

#tokens-->numeric datatype --> operartors --> flow of the program
#contorl block staements --> they control the flow of the program
#when to exeutce ,how to execute
#conditional staements --> if ,else elif (rely on condition to be executed)
#repetion staemnets (loops)-->id usage
#conditional statements -->if useage

syntax:

if <conditions>:
    statement(s)...

#age=16
age=int(input("Enter the age:"))
if age>=18:
    print('your age is :',age)
'''

age =int(input("enter the age:"))
if age >=18 and age in [19,20,25]:
    print('your age is', age)  



























 


