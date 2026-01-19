"""
fruits =["Apple","banana","mango"]
vegetables =["potato","tomato","spinach"]
dry_fruit =["almond","cashew","walnut"]

groceries=[fruits,vegetables,dry_fruit]
print(groceries[1][1])

for collection in groceries:
    for item in collection:
        print(item,end=" ")
    print()
    """

num_pad =((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*","0","#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print() 