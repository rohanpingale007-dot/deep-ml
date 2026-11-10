import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    s=np.linalg.svd(A)
    return s
    pass