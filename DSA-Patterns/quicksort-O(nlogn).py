
# quick sort is an inplace algorithm
# inplace means we dont return the array to fucntion we make changes to arr and just print array at end 
# Time complexity-O(nlogn)
def quick_sort(arr,low,high):
    if low<high:                                 #Base case
        partition=partition_sort(arr,low,high) ##################
        quick_sort(arr,low,partition-1)        ##Recursion case##
        quick_sort(arr,partition+1,high)       ##################

def partition_sort(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=list(map(int,input("Input Here :").split()))
quick_sort(arr,0,len(arr)-1)
print(arr) #see no return value :)

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


