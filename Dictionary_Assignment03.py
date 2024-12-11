                           # Basic Operations
# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
# student = {
    # "name":"Azeem Anjum",
    # "age":20,
    # "Grade": "A+"
# }
# print(student)

# Access the value of the key grade in the student dictionary.

# grade = student["Grade"]
# print(grade)

# Add a new key city to the student dictionary and set its value to "New York".

# student["city"] = "New York"
# print(student)
# Update the value of the age key in the student dictionary to 20.

# student["age"] = 22
# print(student)
# Remove the key city from the student dictionary.

# remove_value = student.pop("city")
# print(student)




# Iterate through the dictionary student and print all keys.

# student = {"name":"Azeem", "age":20, "grade":"A+"}
# print(student.keys())


# Iterate through the dictionary student and print all values.

# print(student.values())

# Iterate through the dictionary student and print all key-value pairs in the format key: value.

# for key, values in student.items():
    # print(key, values, sep=" -->  ")

# Check if the key grade exists in the student dictionary and print True or False.

# exists = "grade" in student
# print(exists)

# Count the total number of keys in the student dictionary.

# count = len(student)
# print(count)



                    #  Merge the following two dictionaries and print the result:
# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  
# merge = dict1 | dict2
# print(merge)


# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
# data = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]
# result = dict(data)
# print(result)
# student = {
#     "name" : "Anjum",
#     "age" : 20,
#     "city": "Fsd"
# }
# print(student)

# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
# data = {'z':1, 'a':2, 'c': 3}
# result = {key: data[key] for key in sorted(data)}
# print(result)

# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
# dict = {'a': 1, 'b': 2, 'c': 3}
# reversed_values = {v: k for k, v in dict.items()}       # {v: k for k, v in original_dict.items()}
# print(reversed_values)


# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
# def are_dicts_identical(dict1, dict2):
#     """
#     Check if two dictionaries are identical.

#     Args:
#         dict1 (dict): The first dictionary.
#         dict2 (dict): The second dictionary.

#     Returns:
#         bool: True if the dictionaries are identical, False otherwise.
#     """
#     return dict1 == dict2
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'a': 1, 'c': 3}
# dict3 = {'a': 1, 'b': 2, 's': 3}

# print(are_dicts_identical(dict1, dict2))  # Output: True
# print(are_dicts_identical(dict1, dict3))  # Output: False


# 16       Create a nested dictionary to represent the following data:
# Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston  

# person = {
#     "name":"Anjum",
#     "Age": 20,
#     "Adress": {
#         "Streed": 15,
#         "City": "Fsd",
#         "phone": "123-456-7890"
#     }
    
# }
# print(person)


# 17   Access the value of the City key in the nested dictionary from the previous question.
# print(person["Adress"]["City"])

# 18 Add a new key Phone to the nested dictionary with the value "123-456-7890".
# person["Phone"] = "123-456-7890"
# print(person)

# 19 Delete the Address key from the nested dictionary.
# del person["Adress"]
# print(person)

# 20 Iterate through all the keys in the outermost level of the nested dictionary and print them.
# for key in person:
    # print(key)

                         # Applications of Dictionaries.
# 21 Use a dictionary to count the occurrences of each word in the string "hello world hello python world".
# text = "hello world hello python world"
# word_counts = {}

# # Split the string into words
# words = text.split()

# # Count the occurrences of each word
# for word in words:
#     word_counts[word] = word_counts.get(word, 0) + 1

# print(word_counts)

#  22  Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
# data = {
#     'a':10, 'b':15, 'c': 7
# }

# key = max(data, key=data.get)
# print("The maximum key is: ", key)

# 23 Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).
# Create the dictionary
# squares = {n: n ** 2 for n in range(1, 6)}

# print(squares)

# 24 Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}.
# data = {'a': 10, 'b': 15, 'c': 10, 'd': 15}

# # Create a new dictionary to store unique values
# unique_dict = {}
# seen_values = set()

# for key, value in data.items():
#     if value not in seen_values:
#         unique_dict[key] = value
#         seen_values.add(value)

# print(unique_dict)

# 25 write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def get_value(dictionary, key):
    """
    Retrieve the value associated with the given key in the dictionary.

    Args:
        dictionary (dict): The dictionary to search in.
        key: The key to look for.

    Returns:
        The value associated with the key, or "Key not found" if the key doesn't exist.
    """
    return dictionary.get(key, "Key not found")

# Example usage
data = {'a': 10, 'b': 15, 'c': 20}
print(get_value(data, 'b'))  # Output: 15
print(get_value(data, 'd'))  # Output: Key not found
