num_list = [1, 2, 3] 
result = num_list[0]

if 1 in num_list: print(True);

for n in num_list:
    if n == 1:
        print(True)
        break

# // The memory growth pattern for a list in python is - 0, 4, 8, 16, 25, 35, 46...
# list .append method has an Ammoritized constant Space Complexity

num_list.append(14)
print(num_list)

# extend method in python list for joining two lists together
# Extend effective makes a series of append calls on each of the element 
# in the new list until all of them have been appended to the original list

new_list = [8, 3, 4]
num_list.extend(new_list)

print(num_list)
