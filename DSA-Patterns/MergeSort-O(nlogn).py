#Merge Sort= Recursively divide array in 2 , sort , Merge
#Run-Time Complexity= O(n log n)//better than bubble,selection ,insertion sorts
#space complexity= O(n)// takes more space than bubble,selection ,insertion sorts
def Mergesort(arr):
    length=len(arr)
    if(length<=1):
        return arr
    middle=len(arr)//2
    lefthalf=Mergesort(arr[:middle])
    righthalf=Mergesort(arr[middle:])
    return merge(lefthalf,righthalf)
def merge(left,right):
    merged=[]
    i=j=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            merged.append(left[i])
            i=i+1
        else:
            merged.append(right[j])
            j=j+1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
arr = list(map(int,input("Input Here: ").split()))
sorted_arr = Mergesort(arr)
print(*sorted_arr)

'''
    | Feature               | Merge Sort                          | Quick Sort                             |
   | --------------------- | ----------------------------------- | -------------------------------------- |
   | **Approach**          | Divide, merge (returns new array)   | Divide, conquer (modifies in-place)    |
   | **Space**             | O(n) extra space (needs new arrays) | O(log n) extra space (recursive stack) |
   | **Worst Time**        | O(n log n)                          | O(n²) (bad pivots 😭)                  |
   | **Best/Average Time** | O(n log n)                          | O(n log n)                             |
   | **Stable?**           | Yes ❤️                              | No 😢 (unless extra work)             |
   | **Returns Value?**    | Yes                                 | No (changes array directly)            |
   '''



# We’ll start by calling merge_sort([8, 3, 5, 2, 9, 1]).
# 
# We’ll split the array into halves, recursively keep splitting, and finally,
# merge the sorted pieces back together.

# Initial Call:
# merge_sort([8, 3, 5, 2, 9, 1])

# Step 1: Find the middle and split:
# Middle index = len([8, 3, 5, 2, 9, 1]) // 2 = 3
# Left half = [8, 3, 5]
# Right half = [2, 9, 1]

# First Recursion: Sort Left Half [8, 3, 5]
# merge_sort([8, 3, 5])

# Step 2: Find the middle of [8, 3, 5]:
# Middle index = len([8, 3, 5]) // 2 = 1
# Left half = [8]
# Right half = [3, 5]

# Step 3: Recursively call on [8] (base case, already sorted):
# Return [8]

# Now, sort [3, 5]:
# merge_sort([3, 5])

# Step 4: Find the middle of [3, 5]:
# Middle index = len([3, 5]) // 2 = 1
# Left half = [3]
# Right half = [5]

# Step 5: Recursively call on [3] and [5] (both are base cases):
# Return [3] and [5]

# Step 6: Merge [3] and [5]:
# Compare 3 and 5 → [3]
# Add 5 → [3, 5]

# Now, merge the sorted halves [8] and [3, 5]:
# Compare 8 and 3 → [3]
# Compare 8 and 5 → [3, 5]
# Add 8 → [3, 5, 8]

# So, the left half [8, 3, 5] is now sorted into [3, 5, 8].

# Now, sort the Right Half [2, 9, 1]:
# merge_sort([2, 9, 1])

# Step 7: Find the middle of [2, 9, 1]:
# Middle index = len([2, 9, 1]) // 2 = 1
# Left half = [2]
# Right half = [9, 1]

# Step 8: Recursively call on [2] (base case, already sorted):
# Return [2]

# Now, sort [9, 1]:
# merge_sort([9, 1])

# Step 9: Find the middle of [9, 1]:
# Middle index = len([9, 1]) // 2 = 1
# Left half = [9]
# Right half = [1]

# Step 10: Recursively call on [9] and [1] (both are base cases):
# Return [9] and [1]

# Step 11: Merge [9] and [1]:
# Compare 9 and 1 → [1]
# Add 9 → [1, 9]

# Now, merge the sorted halves [2] and [1, 9]:
# Compare 2 and 1 → [1]
# Compare 2 and 9 → [1, 2]
# Add 9 → [1, 2, 9]

# So, the right half [2, 9, 1] is now sorted into [1, 2, 9].

# Now, merge the two sorted halves [3, 5, 8] and [1, 2, 9]:
# merge([3, 5, 8], [1, 2, 9])

# Step 12: Merge:
# Compare 3 and 1 → [1]
# Compare 3 and 2 → [1, 2]
# Compare 3 and 9 → [1, 2, 3]
# Compare 5 and 9 → [1, 2, 3, 5]
# Compare 8 and 9 → [1, 2, 3, 5, 8]
# Add 9 → [1, 2, 3, 5, 8, 9]

# Final Sorted Array:
# [1, 2, 3, 5, 8, 9]

# Quick Recap:
# - Split the array into smaller arrays.
# - Sort each smaller array (recursive calls).
# - Merge the sorted arrays back into a larger sorted array.
# - Every time we merge two arrays, we always pick the smallest element
#   from the front of each array until we’ve gone through both arrays.
# - No memory loss. No forgetting. We always have our array of interest 
#   in the call stack while recursion happens.





    
