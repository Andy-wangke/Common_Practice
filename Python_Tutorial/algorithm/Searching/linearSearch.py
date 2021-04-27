# linear search 
#which simply checks the values in sequence until the desired value is found.

import pdb
import pprint

##
def linear_search(items,x):
    f = []
    for i in range(0,len(items)):
        if items[i]==x:
            f.append(i)

    return f

##
def linear_searchV2(items,x):
    for position,item in enumerate(items):
        if item == x:
            return position

    raise ValueError("%s was not found ");


if __name__ == '__main__':
    items = [1,3,7,5,4,3,2,9,3]
    x=10
    pprint.pprint("the original items:[%s],find the item at position %s from zero"%(items,linear_search(items,x)))


