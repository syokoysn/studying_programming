def euclidean_algorithm(a,b):
    '''a>b'''
    a,b = b,a%b
    if b ==0 :
        return a 
    else :
        return euclidean_algorithm(a,b)

if __name__ == "__main__":
    print(euclidean_algorithm(15,5))