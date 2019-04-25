import numpy as np
def euclidean_distance(a,b):
    '''
    input a,b => array
    output floot
    '''    
    return  np.linalg.norm( a - b)


if __name__ == "__main__":
    a = np.array([1,23,45])
    b = np.array([32,12,55])
    print(euclidean_distance(a,b) )