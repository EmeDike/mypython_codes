# Exercise:
# Check if the element 'apple' is present in the list fruits.
# Create a new list more_fruits containing 'banana' and 'orange' and concatenate it with the fruits list.
def check_element(fruits):
    if "apple" in fruits:
        return "YES"
    else:
        return "NO"

fruits = ['apple', 'orange', 'kiwi']
result = check_element(fruits)
print(result)