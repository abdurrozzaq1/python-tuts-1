# Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

#Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.intersection(set2)
print(result)

# Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.union(set2)
print(result)

# Update the first set with items that don’t exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}

print(set1.difference(set2))

for item in set1:
    if item not in set2:
        print(item)

#  Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.
set1 = {10, 20, 30, 40, 50}
set1.discard(10)
set1.discard(20)
set1.discard(30)
print(set1)


# Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set1.symmetric_difference(set2)
print(set3)

# Check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

for item in set1:
    if item in set2:
        print(item)

# Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for item in set2:
    if item not in set1:
        set3.add(item)

for item2 in set1:
    if item2 not in set2:
        set3.add(item2)
print(set3)

# Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1 = set1&set2
print(set1)


# Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict=dict(zip(keys, values))
print(new_dict)


# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)


# Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

result = sampleDict.get('class')
result_student = result.get('student')
result_marks = result_student.get('marks')
get_grade = result_marks.get('history')


# Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
emp_dict = dict.fromkeys(employees, defaults)
print(emp_dict)


# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
new_dict = dict()

for key in keys:
    if key in sample_dict.keys():
        new_dict.update({key: sample_dict[key]})
print(new_dict)


# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
sample_dict.pop('name')
sample_dict.pop('salary')
print(sample_dict)


#  Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary.
# Sometimes it is required to check if the given value is present.
# Write a Python program to check if value 200 exists in the following dictionary.
sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print('hello world')
else:
    print('bye bye world')


# Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict["location"] = sample_dict.pop('city')

# Write a Python script to add a key to a dictionary.
dict_1 = {0: 10, 1: 20}
dict_1[2]=30


# Write a Python script to concatenate the following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic_4 = dict()
dic_4.update(dic1)
dic_4.update(dic2)
dic_4.update(dic3)


# Write a Python script to check whether a given key already exists in a dictionary.

dict_1 = {0: 10, 1: 20, 2:30}

key = int(input('enter the key:  '))

if key in dict_1.keys():
    print('noooooooo')
else:
    print('hello')


