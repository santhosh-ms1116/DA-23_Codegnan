'''
sequences --> strings ,lists,tuples,sets
mapping --->dictionary

#lists --->collection of heterogenous elements(items)
#list --->indexed,ordered,mutable,heterogenous,we use []to strore the data

marks =[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)
#operations: indexing,slicing,striding,membership,merging,reprtition

#nested lists --->a list inside another list

names=['codegnan',24,[54,24,53,43],'DA23',53]

print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4]) #it retuns code
print(names[0][4:])

#get the output as cdga
print(names[0][::2])
names[0]=names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
#indexqing ,slicing -->mutable
names[2]='python'
print(names)
#by indexing if we change the elements,length of collection will remain same
names[3]=['codegnan','PFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[4][0][4:1])

Nnames[2:4]='abhiram','sai','santhu','sairam'
print(names)
#in slicing whatever elements u pass as per the logic length keeps on increas

#o/p as follows:
#['codegnan',25,'abhiram','python','saketh','java','DA23',34]
print(names[2:6:2])

#names =['codegnan','santhosh']
#names.append('data')
#print(names)
names.append(['analysis','agents'])
#print(names)
#print(name[3])
#print(names[3].append('chatgpt'))
#print(names[3])
print(names)

#extend() --->inserts multiple elements to end of list

names.extend('analysis')
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,85])
print(names)
#names.extend(35,43)typeerror
#print(names)
'''
names.insert(1,'python')
print(names)
#names.insert([1:4],['a','b']) #syntaxerror 
#print(names)
 


















      
