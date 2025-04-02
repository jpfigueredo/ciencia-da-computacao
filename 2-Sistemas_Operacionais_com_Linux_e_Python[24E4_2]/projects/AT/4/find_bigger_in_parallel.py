import numpy as np
from vector import vector_by_scalar
from multiprocessing import Pool

def totalize_vector(vector):
    return np.sum(vector)

def biggest_sums(results):
    max_sum = max(results)
    return max_sum if max_sum > 0 else 0.0

def multiply_and_totalize(scalar):
    vector = np.random.uniform(1, 100, size=1000)
    
    vector_by_scalar(vector, scalar)
    
    return totalize_vector(vector)

if __name__ == "__main__":
    scalars = [2, 3, 4, 5, 6, 7, 8, 9]
    
    with Pool(8) as pool:
        results = pool.map(multiply_and_totalize, scalars)
    
    biggest_sum = biggest_sums(results)
    
    print("Somas totais dos vetores:")
    for scalar, result in zip(scalars, results):
        print(f"Escalar {scalar}: Soma Total = {result}")
    
    print(f"\nMaior soma encontrada: {biggest_sum}")
