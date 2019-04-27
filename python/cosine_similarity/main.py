import cosine_similarity
import numpy as np
if __name__ == "__main__":
    a = np.array([1,3,4,5])
    b = np.array([4,6,8,1])
    print(cosine_similarity.cosine_similarity(a,b))