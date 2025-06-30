# d = {
    # "KeyName0": "Value0",
    # "KeyName1": 1
# }

# TODO: Create a dictionary called student
# Include three keys: name, age, grade
# Each key needs a value - yourself or random

student = {
    "Name": "Bob",
    "Age": "∞",
    "Grade": "∞" # key value pairs
}

# print(f"Bob is {student['age']} years old.")

# TODO: Display the name or the grade in the console
print(f"Once upon a time, there was a dude named {student['Name']}.")

# adding new key-value pair
# student['fav_color']

# removing a key-value pair
# def student['fav_color']

# displaying keys of a dictionary
# print(student.keys())

# coverting values to a list and displaying
# print(list(student.valuese()))

# print() <-- extra line of spacing

# Loop throught the dictionary and display the key and value pairs one at a time
for (k, v) in student.items():
    print(k, v)