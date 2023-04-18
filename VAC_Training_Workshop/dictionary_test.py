# write A Program to display all keys and values of a dictionary.
# Get user input for dictionary
my_dict = {}
n = int(input("Enter the number of key-value pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

# Print out dictionary
for key, value in my_dict.items():
    print(key, ":", value)


# Write A Program to find the sum of all the items in a dictionary.\
# Initialize an empty dictionary
my_dict = {}

# Get the number of items in the dictionary from the user
n = int(input("Enter the number of items in the dictionary: "))

# Get the key-value pairs from the user and add them to the dictionary
for i in range(n):
    key = input("Enter key for item {}: ".format(i+1))
    value = int(input("Enter value for item {}: ".format(i+1)))
    my_dict[key] = value

# Calculate the sum of all the values in the dictionary
total = sum(my_dict.values())

# Print the total
print("The sum of all the items in the dictionary is:", total)

# Write Program to create a dictionary with key as first character and value as words starting with that character.

# Get input string from user
input_str = input("Enter a string: ")

# Declare an empty dictionary
my_dict = {}

# Split the string into words and store in a list
words = input_str.split()

# Traverse through the words and add them to the dictionary
for word in words:
    first_letter = word[0]
    if first_letter in my_dict:
        my_dict[first_letter].append(word)
    else:
        my_dict[first_letter] = [word]

# Print the final dictionary
for key, value in my_dict.items():
    print(key, ':', value)

# Write a Python program to convert a list into a nested dictionary of keys.

