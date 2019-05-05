
def bubble_sort(l):
    '''input l : list
    ''' 
    n = len(l)
    for left in range(n):
        for right in range(left+1,n):
            #print(l[left], l[right])
            if l[left] > l[right] :
                l[left], l[right] = l[right], l[left]
    return l

if __name__ == "__main__":
    test = [1,32,2,40,5,63,21,23,55,66,45,43,26,17]
    print(bubble_sort(test))