#Selection Sort:
#The Selection sort algorithm divides the given list into two halves where the first half will be the sorted list and the second is an unsorted list. At first, the sorted list is empty and all elements to be sorted are present in the unsorted list.

#The Selection sort algorithm will look at all the elements present in the unsorted list, pick up the item that is supposed to come first, and then places it in the sorted list. It then repeats the searching process and places the next element to the right of the first element in the sorted list.

#For example, if you have to sort the elements in ascending order, the selection sort algorithm will take a look at the complete list, select the smallest element and then places that element as the first element in the sorted list. Then it searches for the next smallest element and places it to the right of the first element and so on.

 

#Selection Sort Algorithm:

#Step 1: Make the first element as the minimum and compare it with the next element. If the next element is less than the selected element, mark that as the minimum and compare it with the next element. Repeat the same process until you compare all the elements of the unsorted list

#Step 2: Place the minimum in the sorted array (This becomes the first element of the sorted array)

#Step 3: Increment the position of the counter to point at the first element of the unsorted array and repeat steps 1 and 2 for all the elements of the unsorted array

 

#Selection Sort Program:

def selsort(myarray, r):
    for x in range(r):
        minimum = x      #first element is assumed to be the minimum
        for y in range(x + 1, r):    
            if myarray[y] < myarray[minimum]:     #comparing minimum with the next element
                minimum = y
        (myarray[x], myarray[minimum]) = (myarray[minimum], myarray[x]) #swap elements if required
mylist = [34, 23, 1, 67, 4]
r = len(mylist)
selsort(mylist, r)
print(mylist)
