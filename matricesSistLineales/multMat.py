def matrizMulti(A, B):
    m = len(A)
    n = len(B[0])
    p = len(B)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]
    return result


A = [[1, 2], [3, 4]]  #[[1,2,4], [3, 4,0],[1, 2,0]]
B = [[5, 6], [7, 8]]  #[[5, 6,3], [7, 8,7],[1,2,4]]
result = matrizMulti(A, B)
print(result)