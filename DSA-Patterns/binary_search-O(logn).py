#Note:binary search only works on assending order .since the array is sliced on the basis of value of the index
def binary_search(sorted_array,target):
    starting_index=0
    ending_index=len(arr)-1
    while starting_index<=ending_index:
        middle_index=(starting_index+ending_index)//2
        if arr[middle_index]==target:
            return middle_index
        elif arr[middle_index]<target:
            starting_index=middle_index+1 #from middle+1 to end (array chopping)
        elif arr[middle_index]>target:
            ending_index=middle_index-1 # from 0 index to middle -1 idex (array chopping)
arr=list(map(int,input("enter the list seperated by commas ").split(",")))
sorted_array=arr.sort()#sort in assending order
target=int(input("element you want to find in the list"))
result=binary_search(arr,target)
print("quiery "+str(target)+" found at index position "+str(result))