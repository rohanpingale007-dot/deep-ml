import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x=np.zeros(len(b))
    d=np.diag(np.diag(A))
    r=A-d
    for k in range(n):
        x=(b-r@x)/np.diag(d)

    return x