def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Número de colunas de matrix1 não é igual ao número de linhas de matrix2")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matrix2 = [[1, 1, 9], [1, 4, 2], [5, 3, 4]]

result = multiply_matrices(matrix1, matrix2)

print(result)