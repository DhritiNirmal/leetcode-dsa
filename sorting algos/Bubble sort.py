#Bubble Sort:
#Bubble sort is a comparison algorithm that first compares and then sorts adjacent elements if they are not in the specified order.

#Bubble Sort Algorithm:

#Step 1: Beginning from the first element i.e the element at index 0, progressively compare adjacent elements of an array

#Step 2: If the current element and the next element are not in the specified order, swap the elements

#Step 3: If the current element and the next element are in the specified order, move on to the next element


Bubble Sort Program:

#a = name of list
def bs(a):                   
    b=len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a
a=[3,6,1,8]
bs(a)
OUTPUT: [1, 3, 6, 8]
