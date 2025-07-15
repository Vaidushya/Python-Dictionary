#-- Homework --#

test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test dictionary:", test_dict)

try:
    value = int(input("Enter the value to check its frequency: "))
    freq = list(test_dict.values()).count(value)
    print(f"Frequency of value {value}: {freq}")
except ValueError:
    print("Please enter a valid integer value.")
