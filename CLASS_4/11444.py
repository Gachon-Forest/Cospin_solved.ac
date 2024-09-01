def matrix_mul(A, B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%1000000007,
            (A[0][0]*B[0][1]+A[0][1]*B[1][1])%1000000007],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%1000000007,
            (A[1][0]*B[0][1]+A[1][1]*B[1][1])%1000000007]]

def matrix_pow(matrix, n):
    if n==1:
        return matrix
    elif n%2==0:
        half=matrix_pow(matrix,n//2)
        return matrix_mul(half,half)
    else:
        return matrix_mul(matrix,matrix_pow(matrix,n-1))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    initial_matrix=[[1,1],
                    [1,0]]
    result_matrix=matrix_pow(initial_matrix,n-1)
    return result_matrix[0][0]

n = int(input())
print(fib(n))
