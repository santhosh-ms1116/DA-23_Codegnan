'''products = list(map(int, input().split(',')))

total = 0

for price in products:
    total += price

print("Total cart value =", total)

password = "Pravalika@123#"

upper = lower = digit = special = 0

for i in password:
    if i >= 'A' and i <= 'Z':
        upper += 1
    elif i >= 'a' and i <= 'z':
        lower += 1
    elif i >= '0' and i <= '9':
        digit += 1
    else:
        special += 1

print("Uppercase Letters :", upper)
print("Lowercase Letters :", lower)
print("Digits :", digit)
print("Special Characters :", special)
'''
email =input().split()
for mail in email:
    print(mail.split("@")(i))
                        



