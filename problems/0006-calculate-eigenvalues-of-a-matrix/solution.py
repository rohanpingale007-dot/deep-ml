def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues=[]
	det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	trace=matrix[0][0]+matrix[1][1]

	lambda_plus=(trace+((trace)**2-4*det)**0.5)/2
	lambda_miuns=(trace-((trace)**2-4*det)**0.5)/2
	return [lambda_plus,lambda_miuns]