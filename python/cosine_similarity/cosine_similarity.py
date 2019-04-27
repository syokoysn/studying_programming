import numpy as np

def cosine_similarity(a,b):
    '''
    input : a,b => array
    '''
    return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))
    