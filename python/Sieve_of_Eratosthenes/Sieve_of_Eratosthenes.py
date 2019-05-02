def seive_of_eratosthenes(n): 
    data = [i for i in range(2, n+1)]
    result = []
    while True :
        if data == [] :
            break
        result.append(data.pop(0))
        data = [i for i in data if i%result[-1] != 0]
    return result 

if __name__ == "__main__":
    n = 100
    print(seive_of_eratosthenes(n))