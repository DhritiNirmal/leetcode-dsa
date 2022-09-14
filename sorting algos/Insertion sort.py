#Insertion Sort:
#Insertion sort picks one element of a given list at a time and places it at the exact spot where it is to be placed.

#Insertion Sort Algorithm:

#Step 1: Compare the first element with the next element (key) and if the element to the left and the key element are not in order, swap them

#Step 2: Take the next element (key) and if the new key element requires to be repositioned, shift the elements of the sorted list towards the right until an appropriate place is created for the element under consideration

#Step 3: Repeat step 2 until all elements of the given list are sorted

 

#Insertion Sort Program:

def isort(a): 
    for x in range(1, len(a)): 
        k = a[x]  #element present at index number 1
        j = x-1
        while j >=0 and k < a[j] :      #comparing elements with the next until the last item 
                a[j+1] = a[j] 
                j -= 1         #comparing each element to the elements present to its left 
        a[j+1] = k     #new item becomes the key
 
a = [24, 56, 1, 50, 17] 
isort(a) 
print(a)
