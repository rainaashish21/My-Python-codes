rows = int(input("Enter the number of rows : "))
column =int(input("Enter the number of columns : "))
symbol = input("Enter the symbol you want : ")

for x in range(rows):
    for y in range(column):
        print(symbol,end="")
    print()
