def traditional_matrix_multiplication(matrix_1, matrix_2):
    rows_1, cols_1 = len(matrix_1), len(matrix_1[0])
    rows_2, cols_2 = len(matrix_2), len(matrix_2[0])
    if cols_1!=rows_2:
        print("Matrix multiplication not compatible, please enter different dimensions")
    new_matrix = [[0 for i in range(cols_2)] for j in range(rows_1)]
    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(cols_1):
                new_matrix[i][j] += matrix_1[i][k]*matrix_2[j][k]
    return new_matrix

print(traditional_matrix_multiplication([[4,5,5], [1,3,2], [6,3,7]], [[2,5,5], [3,9,6], [3,8,7]]))