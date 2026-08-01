# Student Grade Program
'''
# Read marks from the user
marks = int(input("Enter marks: "))

# Check the grade
if marks >= 90 and marks<=100:
    print("The grade is A", marks)

elif marks >= 80 and marks < 90:
    print("The grade is B", marks)

elif marks >= 70 and marks < 80:
    print("The grade is C", marks)

elif marks >= 60 and marks < 70:
    print("The grade is D", marks)

elif marks >= 0 and marks < 60:
    print("The grade is Fail")

else:
    print("Invalid marks! Please enter marks between 0 and 100.")
    


marks = int(input("enter the marks (1-100):"))
if marks > 0 and marks <=100:
    if marks >=90:
        print("user has secured grand A")
    if marks >=80 and marks <=89:
        print("user has secured grand B")
    if marks >=70 and marks <=79:
        print("user has secured grand C")
    if marks >=60 and marks <=69 :
        print("user has secured grand D")
    if marks <60:
        print("user has failed,study again")
else:
    print("enter only +ve values greater than 0 and less than 100")


age=int(input("enter the age:"))
if age>18 and age<=100:
    print('----- user has vote Eligibility-----')
    print('------access granted----')
elif age<18 and age>0:
    print('-----user still need to get vote eligibility----')
    print("-----user need to wait for more ",(18-age),'year(s)----')
else:
    print('-----only +ve values and less than 100 acceptable----')

#prefer if-elif-else....

#output formatting -->old style formatting (using commas)
#output formatting --> old style formatting (using commas)
#%usage (%f,%d),.format() usage, fstring notation

a,b =7,9
print(a)
print(b)
print(a,b)
name ="codegnan";batch ="dataanaysis"
print(name,batch) #by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='---->')
#end='\n' ,\t -->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("hyderabad")
'''
name='codegnan';age=7;batch='Da-023';place='hyderabad'
'''print(batch,'is in',name) #variables and msg to be separated by comma
print(name,'is in',place,'age is',age,'years')
#old style formatting -->%d-->integer,%-->string,%-->float

salary =25,000
print("his salary is %d"%(salary))
print("his salary is %f"%(salary))
print("his salary is %.1f"%(salary))#%if-->rounding to decimal
'''

#.format()usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage (more recommended)

print(f'{name} is in public')
print(f'{"santhsoh"} is in {name}')














      
      



      
                          
