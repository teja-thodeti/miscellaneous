#taking rows into list [r1,r2,r3] and printing each rows in seperate line.
def  twoD_array(rows,columns):
    matrix=[]
    for r in range(0,rows):
        row=[] #memeory assign as null matrix
        for c in range(0,columns):
            add_element_to_arr=int(input("enter the element for "+"["+str(r)+ "]" +"["+str(c)+"] :"))
            row.append(add_element_to_arr) #appending elements into null array(rows) r1=[1,2,3]
        matrix.append(row) #appending rows in into matrix[r1,r2,r3....]
    return matrix
m=int(input("enter number of rows :"))
n=int(input("enter the number of columns :"))
result=twoD_array(m,n)
for rows in result:
    print(rows) #seperating each row and printing in sperate column
print(result[0][1]) #accessing 