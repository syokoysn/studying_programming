import Bubble_Sort
import numpy as np

if __name__ == "__main__":
    test =np.random.randint(0,100,30)
    print(all(sorted(test) == Bubble_Sort.bubble_sort(test)))