'''
lists,tuples

#list--->mutable,ordered,heterogenous

#index(),count(),copy(),sort(),reversed()

details=['codegnan',7,2018,'hyderabad']
print(len(details))
print(details.index(7))
print(details.index(7))
print(details.index('codegnan'))
details.extend.index(21)
print(details.index(21))
print(details.index(21,6))
#print(details.index('python'))#valueerror

print(details.count(21))
print(details.count('python'))

data =['codegnan','saketh','python','java']#input
#output should be as follows
0:codegnan
1:santhosh
2:python
3:java

for obj in data:
    print(data.index(obj),':',obj)


for obj in range(len(data)):
    print(obj,':',data[obj])

#copy() --->shallow copy of the given collection

new =data.copy()
print(new)
print(type(new))
print(len(data))

new[2] ='agentic AI'
print(new)
print(new)

data.append('santhosh')
print(data)
print(new)

data =[1,3,4,[21,43,53,53],23]
print(data)
new =data.copy()
print(new)

new[3][2]='agents' #whenever we make changes in nested list original will
#also be effected
print(new)
print(data)

new[1] ='python'
print(new)
print(data)

marks =[14,24,-45,27,35]
print(marks)
#print (marks.sort() #retuns none
#print(marks) #retuns in ascending order
#marks.sort(reverse = True)#retuns in descending order...
#print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse()--->retuns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print()

print(sorted('codegnan')#retuns lists in ascending order
#print(sorted(['code','23',34','45']))#raises error     

#tuples --->tuples are indexed,orderred,heterogenous,immutable collection
#dimensisons,coordinaties,database records,we prefer()for tuple notat

a=()
print(type(a))
print(len(a))

dimensions =1.5,2.5
print(dimensisons)
print(type(dimensions))
print(len(dimensions))

#operations --->indexings,slicing,striding,membership,merging,repetion


courses =('PFS','JFS',('DA','SA'),'AGENTIcAI',[100,6,6])

print(courses)
print(len(courses))      

print(courses[-2][-2:])
#courses[2] =23 tuples are immutable
courses[-1].append('codegnan')#we can make modifications inside list
print(courses)

#create a nested tuple as above and work on slicing,striding and list funct:
print('PFS' in courses)
d =courses* 2
print(d)
e= courses +(2,3,4,5)
print(e)

#tuples immutables --> count(),index()
print(courses.index('AgenticAI'))
print(courses.count('Agents'))

#print(courses.sort())#attributeerror --->sort() is in lists not in tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#type casting
d= tuple(sorted((23,12,3,2,4)))
print(d)

#accept group of intergers space separted
a,b =map(int,input("enter the values").split())
print(a,b)

a=tuple(map(int(input("enter the values").split(',')))
print(a)
print('9+4')
print(eval('9+4'))

a=eval(input("enter a lists"))
print(a)
print(type(a))
'''
#task:take a user input as strings,do this in two ways..
'''
1)give the count of each repeating character
test case1:programming

r is repating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is reapsting 2 times
index =[1,4]
g is













    

