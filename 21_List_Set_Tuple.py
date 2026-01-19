#Collection = single variable used to store multiple items
#list= Ordered and Changable.Duplicates OK.  Duplicates OK
#Set ={} unordered and immutable . bUt can add or remove elements
#Tuple =()  ordered and unchangable. Duplicates Ok



"""fruits = ["Apple","Orange","Banana","Mango","Watermelon"]

#for fruit in fruits:
 #   print(fruit)

fruits.append("Pineapple")
fruits.remove("Orange")
fruits.insert(2,"Mango")
fruits.sort()
fruits.reverse()
#fruits.clear()
print(fruits.index("Mango"))
print(fruits.count("Mango"))
print(fruits)"""

"""fruits = {"Apple","Orange","Banana","Mango","Watermelon"}
fruits.add("Kiwi")
fruits.remove("Orange")
fruits.pop()
fruits.clear()
print(fruits)"""

fruits = ("Apple","Orange","Banana","Mango","Watermelon")

#print("Mango" in fruits)
#print(dir(fruits))
#print(help(fruits))

print(fruits.index("Banana"))
print(fruits.count("Orange"))
print(fruits)
