#Selection Sort
#implementation thought
#
#
import pdb
import pprint

#version 1 :using the brand new list to store the list
def selection_sort(items):
    b = []
    while len(items)>0:
        min = 0
        for i in range(1,len(items)):
            if items[i] < items[min]:
                min = i
        b.append(items.pop(min))
    return b


#version 2 :swap the element in the single list 
def selection_sort_in_place(items):
    # TODO: how to debug in sublime
    import pdb;pdb.set_trace()
    for i in range(0,len(items)):
        min = i
        for j in range(i+1,len(items)):
            if items[j]<items[min]:
                min = j
        #swap each other
        temp = items[i]
        items[i] = items[min]
        items[min] = temp
        print("No.%s-%s"%(i,items))
    return items


if __name__=='__main__':
    a = [3,1,4,2,5,0]
    a = a[:]
    print("Before sorting %s"%a)
    #pprint.pprint("After sorting %s"%selection_sort(a))
    pprint.pprint("After sorting %s"%selection_sort_in_place(a))
    


