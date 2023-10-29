def calculate2Darray(rows, cols):
    matrix = [[i * cols + j for j in range(cols)] for i in range(rows)]

    return matrix
rows = 2
cols = 3
result = calculate2Darray(rows, cols)
print(result)
