import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    try:
        inverse= np.linalg.inv(matrix)
        return inverse
    except :
        return None
    pass