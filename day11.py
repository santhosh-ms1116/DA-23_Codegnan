'''
strings--->> caseconversions, searchind &finding ,string testing methods,
Replace,space removal

#serching,finding,replacing,joining...
a='Codegnan'

print(len(a))
print(min(a))
print(max(a))

b=a.index('g')
print(b)

c=a.index('n')
print(c)#it returns only the first occurannce

d=a.index('n',6)
print(d)#it returns the next occurance

#d=a.index('n',8)
#print(d) #valuerror
g=a.index('n',1,4)
print(g)

#rindex()---->>> returns the last occurance
b=a.rindex('g')
print(b)

c=a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8) #it return the valuerror

# count()--->>> returns the number of items object is repeating
print('codegnan'.count('n'))
print('code'.count('w'))    #it returns 0 as we dont have 'w'in code
print('venkatesh'.count('v'))

print('codegnan'.find('n'))
print('codegnan'.find('r')) #it returns '-1' becoz it dont have 'r' in codegnan

print('codegnan'.rfind('r'))

print('codegnan'.rfind('n'))


a='Data'
print(len(a))
for i in a:
    print(a.count(i),a.index(i))
'''

#replacing, splitting,Joining
#strings are immutable
'''
a='codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)

print('venkatesh@warlu'.replace('@',' '))

print(a.replace('x','venkatesh'))
'''
'''
a='venky codegnan python'
#print(len(a))
b=a.split()  #by default if we have space it splits and (returns list)
print(b)
#print(len(b))

c='venky,codegnan,python'
d=c.split()

print(d)
print(len(d))
e=c.split(',')
print(e)
print(len(e))

#JOIN()
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('SANTHOSH'))
print(' '.join('SANTHOSH'))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....

a='codegnan123'
print(a.isalnum()) #retuns true for alphanumeric strings else false
b='codegnan'
print(b.isalpha())
print(a.isalpha()) #retuns true only for alphabets
print(a.isdigit())
print('9353112270'.isdigit())
print('2345'.isnumeric())
print('codegnan'.startswith('c'))
print('codegnan'.endswith('f'))

print('coddgnan'.islower())
print('codegnan'.islower())
print('codegnan python'.istitle())

#space removal --->strip() (removes leading and trailing spaces)
a='codegnan'
print(a.strip())
b=input("enter the string:").strip().lower()
print(b)
'''
print('234'.zfill(4))
print('234'.zfill(7))

print('hai'.center(6))
print('hai'.center(6,'#'))
print('hai'.ljust(6,'#'))
print('hai'.ljust(6,'#'))


































