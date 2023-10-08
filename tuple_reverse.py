given_tuple = (10, 20, 30, 40, 50)
sorted_tuple = ()

for element in given_tuple:
     sorted_tuple = ((element,) + sorted_tuple)

resultant_tuple = sorted_tuple
print(sorted_tuple)