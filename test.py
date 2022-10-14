'''
def sorted( arr):
     if len(arr) <= 1:
        return arr
     mid=len(arr)//2
     left=arr[:mid]
     right=arr[mid:]

     sorted(left)
     sorted(right)

     merge_sort(left,right,arr)
def merge_sort(left,right,arr):

    i=j=k=0
    sorted_list=[]
    while i < len(left) and j < len(right):
          if left[i] <= right[j]:
              arr[k]=left[i]
              i+=1
          else:
               arr[k]=right[j]
               j+=1
          k=k+1
          print(arr)
    
    while i < len(left):

              arr[k]=left[i]
              i+=1
              k=k+1

    while j < len(right):

              arr[k]=right[j]
              j+=1
              k=k+1
    

 


if __name__ == "__main__":
    elements=[10,3,15,7,8,23,98,29]
    sorted(elements)
    print(elements)





'''






'''
def highest_occurences(arr):
    
    dicts={}
    for indexes in range(len(arr)):
    	 if arr.count(arr[indexes]) > 1:
    	 	  dicts.update({arr[indexes]:arr.count(arr[indexes])})
    check_dict=bool(dicts)
    if check_dict == False :
    	return -1
    else:
    	return max(dicts,key=dicts.get)
print(highest_occurences([2,3,2,8,8,5,8,4,0,4]))
print(highest_occurences([4,5,4,5,3]))
print(highest_occurences([1,2,3,4,9,5]))
'''

'''
def highest_occurences(List):
    return max(set(List), key = List.count)


print(highest_occurences([4,5,4,5,3]))
'''


def swap(a,b,arr):
     if a!=b:
        arr[a],arr[b] = arr[b],arr[a]

def partition(element):
    pivot_index=0
    pivot=element[pivot_index]

    start=pivot_index+1
    end=len(element)-1

    while start < end:
        
        while element[start] <= pivot:
             start+=1

        while element[end] > pivot:
             end-=1

        

        if start < end :
           swap(start,end,element)

    swap(pivot_index,end,element)


def quickSort(element):
     partition(element)


if __name__ == "__main__":

    element=[11,9,29,7,2,28]
    partition(element)
    print(element)