#Merge sort first divides the array into equal halves and then combines them in a sorted manner.

#divide and conquer algorithm splits a list in half, and keeps splitting the list by 2 until it only has singular elements.
#Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs as well. This process continues until we get a sorted list with all the elements of the unsorted input list.

#We recursively split the list in half until we have lists with size one. We then merge each half that was split, sorting them in the process.
#Sorting is done by comparing the smallest elements of each half. The first element of each list are the first to be compared. 
#If the first half begins with a smaller value, then we add that to the sorted list. We then compare the second smallest value of the first half with the first smallest value of the second half.

#Every time we select the smaller value at the beginning of a half, we move the index of which item needs to be compared by one.
#Merge Sort Algorithm:

#Step 1: Check if the list contains more than one items; if yes, divide the list into two halves, else the list is sorted

#Step 2: The list is to be divided repeatedly until there is only a single element left in each sub-list

#Step 3: Recursively merge the sub-lists by arranging them in the given order until you get a single sorted list

 

Merge Sort program:

def msort(mylist, left, right):
    if right - left > 1:
        middle = (left + right)//2
        msort(mylist, left, middle)
        msort(mylist, middle, right)
        mlist(mylist, left, middle, right)
 
def mlist(mylist, left, middle, right):
    leftlist = mylist[left:middle]
    rightlist = mylist[middle:right]
    k = left
    i = 0
    j = 0
    while (left + i < middle and middle + j < right):
        if (leftlist[i] <= rightlist[j]):
            mylist[k] = leftlist[i]
            i = i + 1
        else:
            mylist[k] = rightlist[j]
            j = j + 1
        k = k + 1
    if left + i < middle:
        while k < right:
            mylist[k] = leftlist[i]
            i = i + 1
            k = k + 1
    else:
        while k < right:
            mylist[k] = rightlist[j]
            j = j + 1
            k = k + 1
  
  
mylist = input('Enter the list values to be sorted: ').split()
mylist = [int(x) for x in mylist]
msort(mylist, 0, len(mylist))
print('The sorted list is: ')
print(mylist)
The above program will allow the user to enter a list that is to be sorted and will display the final sorted list as shown below:

OUTPUT:

Enter the list values to be sorted: 23 1 45 34 7
The sorted list is:
[1, 7, 23, 34, 45]
