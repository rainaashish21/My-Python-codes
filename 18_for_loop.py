for x in range(1,10):
    print(x)

for x in reversed(range(1,10)):
    print(x)

for x in range(1,10,3):
    print(x)

for x in range(1,11):
    if x==8:
        continue
    else:
        print(x)

for x in range(1,10):
    if x==7:
        break
    else:
        print(x)


credit_num= "1234-5678-ABCD"
for x in credit_num:
    if x =="-":
        continue
    else:
        print(x)