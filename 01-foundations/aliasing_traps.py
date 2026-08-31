# Module 01.1
# Lab 1: Aliasing Traps
# Date: 08.17.2026
#
# PURPOSE
# Testing mental model of how Python binds names to objects.
# Each trap probes one of: aliasing, rebinding, mutation, shallow copy,
# or immutability.
#
# RULES: 
# Predict every output in a comment before running. 
# Predictions stay in the file even when wrong.


# TRAP 1
a = [1, 2, 3]
b = a
b.append(4)
print(a)                    # PREDICTION: [1, 2, 3, 4]

# TRAP 2
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)                    # PREDICTION: [1, 2, 3]

# TRAP 3
a = [[1, 2], [3, 4]]
b = a[:]
b[0].append(99)
print(a)                    # PREDICTION: [[99, 1, 2], [3, 4]]

# TRAP 4
x = 5
y = x
y += 1
print(x)                    # PREDICTION: 5

# TRAP 5
a = [1, 2, 3]
b = a
a = [9, 9, 9]
print(b)                    # PREDICTION: [1, 2, 3]

# TRAP 6
def modify(lst):
    lst.append("added")
data = [1, 2]
modify(data)
print(data)                 # PREDICTION: [1, 2, 'added']

# TRAP 7
def reassign(lst):
    lst = ["completely", "new"]
data = [1, 2]
reassign(data)
print(data)                 # PREDICTION: [1, 2]

# TRAP 8
a = [1, 2, 3]
b = a
del a
print(b)                    # PREDICTION: [1, 2, 3]

# RESULTS
# Missed: Trap 3 (position only — predicted [99,1,2], actual [1,2,99])
# Why: append() always adds to the END. Forgot that it adds to the END.
