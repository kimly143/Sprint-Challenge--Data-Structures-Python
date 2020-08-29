import time
from binary_search_tree import BSTNode 
from search import search

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

########### using binary_search_tree O(log(n))
# names_1_tree = BSTNode(names_1[0]) # name_1[0] : first name of the array
# for name in names_1[1:]:
#     names_1_tree.insert(name)

# for name in names_2:
#     if names_1_tree.contains(name):
#         duplicates.append(name)
# runtime: 0.09500432014465332 seconds


#---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
names_1.sort()
for name in names_2:
    if search(names_1, name):
        duplicates.append(name)
######### runtime: 0.035001277923583984 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


