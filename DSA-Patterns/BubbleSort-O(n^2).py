#Time Complexity: O(n^2)
#Logic: For each nested iteration one element(last one) is arranged // assending or decending 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):#len(arr)-i-1 leaves the last elemtent since it is already sorted
            if arr[j]>arr[j+1]:#use < for decreasing order
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=list(map(int,input("input here: ").split()))
result=bubble_sort(arr)
print(*result)#printing list with no commas and brackes use *

 