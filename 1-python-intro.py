# Examples of iteration with for loops.

my_list = [0, 1, 2, 3, 4, 5]

# Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
for item in my_list:
    print('The value of item is: ' + str(item))

# Print each index and value pair.
for i, value in enumerate(my_list):
    print('The index value is: ' + str(i) +
          '. The value at i is: ' + str(value))

# Print each number from 0 to 9 using a while loop.
i = 0
while(i < 10):
    print(i)
    i += 1

# Print each key and dictionary value. Note that you can use the "in" keyword
# to iterate over dictionary keys.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])


my_dict = {'a': [0, 1, 2, 3], 'b': [0, 1, 2, 3],
           'c': [0, 1, 2, 3], 'd': [0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)

num = 5
if num < 5:
    print('The number is smaller than 5.')
elif num == 5:
    print('The number equals 5.')
else:
    print('The number is greater than 5.')
