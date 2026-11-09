import numpy as np 
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	vectors=np.array(vectors)
	
	if vectors.shape[0]<2:
		return [1.0]
	calculate_covariance=np.cov(vectors)
	return list(calculate_covariance)