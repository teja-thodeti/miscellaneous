#After Comparing elements to the left we move all the compared elements
# to right to make room for the least element 
# TimeCompexity-O(n^2)
def insertionsort(arr):
    n=len(arr)
    for i in range(1,n-1):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j=j-1
    return arr
arr=list(map(int,input("Here : ").split()))
print(insertionsort(arr))
