numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

unique_list = []

for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", numbers)
print("List after removing duplicates:", unique_list)
