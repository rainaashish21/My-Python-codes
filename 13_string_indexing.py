#indexing = accessing elements of a sequence using [] (indexing operator)
#          [start : end : step]

credit_number = "1234-5678-9876-5432"
print(credit_number[0:4])
print(f"The last 4 digits of your credit card number is XXXX-XXXX-XXXX-{credit_number[-4:]}")
print(f" The reverse of a credit card number is {credit_number[::-1]}")