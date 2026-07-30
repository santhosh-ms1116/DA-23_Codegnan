'''
token-->variables punctuators

variables --> name memory  loaction ,its placholder for data
#rules are to be followed
'''
#multiassigment of variables

name,age,place='codegnan',7,'hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='----->')

#a,b=2,3,4 #valueError as too many values to unpack
#reassing variables

name='codegnan'
a,b=45,1.5
#print(a,b)
#a,b=b,a
#print(a,b,sep='-')

#a,b =b,c #namerror as c is not found

#deleting the variables -->del
#del a,b
#print(a,b)
# punctuators --> [](lists), () (tuples),{}(dict,sets)
name ="codgnan";age=23;course='data analysis'
print(name,age,course)

#data types -->numeric(int,float,comlex),boolean,none,
#-->sequences -->lists,tuples,sets,strings,
# frozensets mappings(dict)
#numeric type -->int,float,complex
#int datatype -->quantity,age
age=7
print(age)#type--> retuns the datatype of objects

print(type(233))

#quantity =03 #its is not allowed
#print(quantity)

#float datatype-->temp,salary,price
price=1000.24;discount =2.5
print(price,discount)
print(type(price))

#complex --> combination of real and imag
data =5+i2
print(data)

data =5+2j #j is imag representaion
print(data)
print(type(data))
'''


#boolean -->true /false

valid =true
print(type(valid))

error =false
print(type(erroe))

erroe =false
print(type(erroe))
'''
#typecasting -->coverting one type to another type
#python by default follows implicit type (we need not mention the dadatype)

#we will go for explicit coversion

#evry bulit-in datatype is a built -in functions
#int,float,complex,bool

#typecasting -->int,float,complex,bool

age=35
print(type(age))
b=float(age)
print(b)   
c=complex(age)
print(c)
d= bool(age)#retuns true foe existing data
print(d)
e= bool(0)
print(e)

#float --> typecasting--> int,complex,bool

price=770.46
print(type(price))
d = int(price)
print(d)
print(type(d))
e = cpmplex(price)
print(e)
f = bool(price)
print(f)



















