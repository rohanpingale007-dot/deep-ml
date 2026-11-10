import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    a=np.linalg.svd(A)
    return a