import copy

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''list.append'''
nums.append(11)
nums.append(12)
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

'''list.extend'''
more_nums = [13, 14, 15]
nums.extend(more_nums)
print("More nums: ", nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

'''list.insert'''
nums.insert(3, 68)
print(nums) # prints [0, 1, 2, 68, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums.insert(5, 42)
print(nums) # prints [0, 1, 2, 68, 3, 42, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

'''list.remove'''
nums.remove(68)
print(nums) # prints [0, 1, 2, 3, 42, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# nums.remove(41) reaises ValueError

'''list.pop'''
number42 = nums.pop(4)
print(number42) # prints 42
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
number15 = nums.pop()
print(number15) # prints 15
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

'''list.clear'''
old_nums = copy.deepcopy(nums)
nums.clear()
print(nums) # prints []
nums = old_nums
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

'''list.index'''
index14 = nums.index(14)
print(index14) # prints 14
nums.insert(3, 14)
index14 = nums.index(14)
print(index14) # prints 3
index14 = nums.index(14, 5, 16) # upperbound exclusive
print(index14) # prints 15

'''list.count'''
print(nums.count(14)) # prints 2

'''list.sort'''
nums.sort(reverse=True)
print(nums) # prints [14, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums.sort()
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]

'''list.reverse'''
nums.reverse()
print(nums) # prints [14, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums.reverse()
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]

'''list.copy'''
num_copy = nums.copy()
print(num_copy)  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]
num_copy.clear()
print(num_copy) ## prints []
print(nums) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]