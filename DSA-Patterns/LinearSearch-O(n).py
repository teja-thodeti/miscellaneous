#linear Search (Iterates thorugh the array until we find the Target)
#TIMECOMPLEXITY- # O(1)// Best case
                 # O(n)//worst case


#code:
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i,arr[i] #return can also return 2 values
    return -1,None
arr=list(map(int,input().split(",")))#splitting input with commas
target=int(input())
result_index,result_num=linear_search(arr,target)#have to name result both to store i and arr{index} 
if result_index==-1:
    print("Number does not exist in array")
else:
    print("Number "+str(result_num)+" found at index "+str(result_index)+ " position" )


#How It Works:
#You go through the list of friends one by one.
#If someone’s name matches your best friend’s name, boom, you found them!
#If you don't find them after asking everyone, well, looks like your best friend isn’t at this party. 😢
