
def fibonacci_matrix(position: int) -> int:

    def multiply_matrix(matrix_a:list, matrix_b:list) -> list:
        # Create an auxiliary matrix to store elements after multiply
        mul_matrix = [[0 for x in range(3)]
                          for y in range(3)]
        
        # Multiply matrix
        for i in range(3):
            for j in range(3):
                mul_matrix[i][j] = sum(matrix_a[i][k]*matrix_b[k][j] for k in range(3))

        # Update matrix_a 
        for i in range(3):
            for j in range(3):
                matrix_a[i][j] = mul_matrix[i][j]
        return matrix_a

    def power(fib_matrix:list, n:int) -> int:
        initial_matrix = [[1, 1, 1], 
                          [1, 0, 0], 
                          [0, 1, 0]]
        if n == 1:  
            return fib_matrix[0][0] + fib_matrix[0][1]
        
        power(fib_matrix, n//2)
        
        fib_matrix = multiply_matrix(fib_matrix, fib_matrix)
        
        if n % 2 != 0:
            fib_matrix = multiply_matrix(fib_matrix, initial_matrix)
        
        return fib_matrix[0][0] + fib_matrix[0][1]
    
    def find_pos_n(n: int) -> int:
        fib_matrix = [[1, 1, 1],
                      [1, 0, 0],
                      [0, 1, 0]]
        return power(fib_matrix, n-2)
    
    return find_pos_n(position)

print(fibonacci_matrix(50))