

def select_sort(l):
    u = len(l)
    for i in range(u-1):
        for j in range(i+1,u):
            if l[i]>l[j]:
                l[i], l[j] = l[j], l[i]
    return l


if __name__ == "__main__":
    test = [1,32,2,40,5,63,21,23,55,66,45,43,26,17]
    print(select_sort(test))