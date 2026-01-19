#           X if CONDITION else Y

num = 5
a = 6
b=7
age =54
temp =21
user_role = "Admin"


#print("Posiitve" if num>0 else "Negative")
#print("Even" if num%2==0 else "Odd")
#max_num = a if a>b else b
#min_num = a if a<b else b
#print(max_num)
#print(min_num)
status = "Adult" if age>18 else "Child"
print(status)
weather= "Hot" if temp>20 else "Cold"
print(weather)

access ="Full access" if user_role =="Admin" else "Limited access"
print(access)
