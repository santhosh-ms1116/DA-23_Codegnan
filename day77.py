'''#for with else
work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0 #target variable 
current_streak = 0 
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest Streak is {longest_streak'}


while True:
    print("yes")

#it rins as infinite loop we need to press ctrl+c (keyboard interrupt)

i =0 #initialised statement
while i<=10:
    print(i)
    i=i+1 #counter

i=0
while  i<=10:
    i +=1
while i>1:
    i-=1
    print(i)
'''
#banking scenario--> PIN authentication if more than 3 attempts
#account locked..

pin ="1116"
max_attempts =3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin =input("enter the ATM PIN:")
    if entered_pin == pin:
        print("login successful")
        break
    else:
        print("Entered PIN is wrong.. try again carefully")
        current_attempt +=1
else:
    print("account locked,try after 24hours...")
    












    


