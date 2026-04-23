# GROUP WORK ON LINEAR AND BINARY SEARCH

# Q1.PROBLEM DESCRIPTION
# We are looking for a blue bottle in a lost and found bin
# The data represents other random items found on campus

# Q2. ALGORITHM CHOICE
# Method used: Linear search (since items are not sorted)


# Q3 CODE IMPLEMENTATION
def linear_search(arr, value):
    for i in range(len(arr)):
        print(f"Checking index {i} value: {arr[i]}")
        if arr[i] == value:
            print(f"Found at index {i}")
            return i
    print("Not found")
    return -1

# Realistic dataset
lost_found_bin = ["sweater", "jacket", "Math textbook", "blue bottle", "lunch box", "phone charger", "notebook"]
target = "blue bottle"
result = linear_search(lost_found_bin, target)

# Q4 OUTPUT
# Checking index 0 value: sweater
# Checking index 1 value: jacket
# Checking index 2 value: Math textbook
# Checking index 3 value: blue bottle
# Found at index 3

# Process finished with exit code 0

# Q5: Reflection
# 1.Why linear search? (Items are not sorted, so we have to check each one)
# 2.Would binary search work? (No. Only if items are sorted)
# 3. What happens if the data becomes large? (Search time becomes slower with increase of items)

