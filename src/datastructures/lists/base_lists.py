squares = [1, 4, 9, 16, 25]

''' Section 1: Indexing and Slicing '''
print(squares[0]) # displays 1
print(squares[-1]) # indexing backwards returns 25
print(squares[-3:]) # displays a new list: [9, 16, 25]
print(squares[2:])  # displays a new list: [9, 16, 25]

''' Section 2: Conocatenation '''
print(squares + [36, 49, 64, 81, 100]) # displays [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

''' Section 3: Mutability '''
squares[2] = 3
print(squares) # displays [1, 4, 3, 16, 25]
squares[2] = 9 # changes 3 in squares back to 9
print(squares) # displays [1, 4, 9, 16, 25]

''' Section 4: Shallow Copy Slicing'''
five_square = squares[:]
five_square[-1] = 81 # set last element in five_square to 81
print(five_square) # [1, 4, 9, 16, 81]
print(squares) # [1, 4, 9, 16, 25]

''' Section 5: Slicing Assignment '''
squares[2:5] = [36, 49, 64] # squares is now [1, 4, 36, 49, 64]
print(squares)
squares[2:5] = [] # removed, squares is now [1, 4]
print(squares)
squares[:] = [] # removed all, squares is now []
print(squares)
squares = [1, 4, 9, 16, 25] # repopulation
print(squares)

''' Section 6: Nested Lists '''
a = [[1, 2, 3], [4, 5, 6]]