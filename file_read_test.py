#!/usr/bin/env python3
f = open('data.txt', 'r')


read_data = f.read()
print(read_data)


f.close()

# Split the read data into a list of lines
list_of_lines = read_data.split('\n')
print(list_of_lines)

# METHOD 1
f = open('data.txt', 'r')
method1 = list(f)
f.close()
print("Method 1:", method1)

# METHOD 2
f = open('data.txt', 'r')
method2 = f.readlines()
f.close()
print("Method 2:", method2)
