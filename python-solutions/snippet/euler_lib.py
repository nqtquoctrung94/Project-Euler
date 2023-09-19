# Prepared function that commonly used in solving problems
# Sorted by alphabet

from collections.abc import Iterator
import math

def divisors_count(n: int) -> int:
    """This function return the number of divisors of n. The idea is based on divisors_list function"""
    result = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            if i * i == n:
                result += 1
            else:
                result += 2
    return result


def divisors_list(n: int) -> Iterator[int]:
    """This function return the generator of all divisors of n"""
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            if i * i == n:
                yield i
            else:
                yield i
                yield n//i


def divisors_sum_list(limit: int) -> list:
    """This function return the divisors sum list from 0 to limit, for more indeep proof, check question 21"""
    sum_list = [0]*(limit+1)
    for divisor in range(1, limit//2 + 1):
        index = divisor
        while index < limit+1:
            sum_list[index] += divisor
            index += divisor
    return sum_list


def factorial_iteractive(n: int) -> int:
    """This function return factorial of n = n! using for loop"""
    result = 1
    for i in range(2,n+1):
        result*= i
    return result


def factorial_recursive(n: int) -> int:
    """This function return factorial of n = n! using recursive"""
    if n < 2:
        return 1
    return n*factorial_recursive(n-1) 


def fibonacci_iteractive(position: int) -> int:
    """This function return the Fibonacci number at nth position using for loop"""
    a = 1
    b = 1
    for i in range(3, position+1):
        a,b = b, a+b
    return b


def fibonacci_recursive(position: int) -> int:
    """This function return the Fibonacci number at nth position using for recursive"""
    if position <= 1:
        return position # fib(0) = 0 and fib(1) = 1
    return fibonacci_recursive(position-1) + fibonacci_recursive(position-2)


def fibonacci_matrix(position: int) -> int:
    """This function return the Fibonacci number at nth position using the power of matrix
    There are still some errors in the function.
    Reading: https://www.geeksforgeeks.org/matrix-exponentiation/
    """
    def multiply_matrix(matrix_a:list, matrix_b:list) -> list:
        # Create an auxiliary matrix to store elements after multiply
        mul_maxtrix = [[0 for _ in range(3)]
                          for _ in range(3)]
        for i in range(3):
            for j in range(3):
                mul_maxtrix[i][j] = sum(matrix_a[i][k]*matrix_b[k][j] for k in range(3))

        for i in range(3):
            for j in range(3):
                matrix_a[i][j] = mul_maxtrix[i][j]

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
    

def greatest_common_divisor_binary_module(a: int, b: int) -> int:
    """ This function find GCD of a and b using binary algorithm, also known as Stein's algorithm.
    The algorithm repeatedly applying these identities:
    - gcd(0 , b) = b and gcd(a, 0) = a.
    - gcd(2a,2b) = 2*gcd(a, b)
    - gcd(2a, b) = gcd(a, 2b) = gcd(a, b)
    - gcd(a , b) = gcd(|a − b|, min(a, b)), if a and b are both odd.

    Reading: https://en.wikipedia.org/wiki/Binary_GCD_algorithm
    """
    # Base case
    if a == 0: return b
    if b == 0: return a

    # Save the multipler of 2
    power2 = 0
    while (a % 2 == 0) and (b % 2 == 0):
        a //= 2
        b //= 2
        power2 += 1
    
    # Remove factors of 2 from a
    while (a % 2 == 0):
        a //= 2

    # Calculate GCD
    while b != 0:
        while (b % 2 == 0):
            b //= 2
        if a > b:
            a, b = b, a
        b -= a      # Shorter, but worse performance: a,b = min(a,b), abs(a-b)
    return a * (2**power2)


def greatest_common_divisor_binary_shift(a: int, b: int) -> int:
    """ This function find GCD of a and b using binary algorithm, by applying bitwise operations.
    The idea is the same as function greatest_common_divisor_binary_module

    Reading: https://saturncloud.io/blog/binary-gcd-a-faster-algorithm-for-greatest-common-divisor/   
    """
    # Base case
    if a == 0: return b
    if b == 0: return a

    # Save the multipler of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove factors of 2 from a
    while (a & 1) == 0:
        a >>= 1

    # Calculate GCD
    while b != 0:
        while (b & 1) == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b -= a      # Shorter, but worse performance: a,b = min(a,b), abs(a-b)
    return a << shift


def greatest_common_divisor_recursive(a: int, b: int) -> int:
    """ This function find GCD of a and b using Euclidean recursive algorithm.
    Reading: https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm
    """
    if b == 0:
        return a
    else:
        return greatest_common_divisor_recursive(b, a % b)


def is_even(n: int) -> bool:
    """This function check if number is even or not"""
    return (n % 2 == 0)


def is_palindromic(n: int) -> bool:
    """ This function check if number n is panlidromic, aka reading from left to right is the same with right to left
    - Turn n into string
    - Create reverse_n by apply slice notation list[<start>:<stop>:<step>]
    - Then compare string_n with reverse_n
    Reading: https://www.w3schools.com/python/python_howto_reverse_string.asp
    """
    string_n = str(n)
    reverse_n = string_n[::-1]    
    return (string_n == reverse_n)


def is_pentagonal_number(n: int) -> bool:
    """This function return if input number is a pentagonal number
    Reading: https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
    """
    if n < 1:
        return False
    x = (math.sqrt(24*n + 1)+1)/6
    return x.is_integer()


def is_prime(n: int) -> bool:
    """ This function check if input number n is prime or not
    Write the prime number in the form of p=6k+i, with i=[0,1,2,3,4,5]
    We can see that:
        - with i=[0,2,4] -- 6k+i is divisible by 2
        - with i=[0,3]   -- 6k+i is divisible by 3
    So first check divisble by 2 and 3, then check for every p = 6k+1 and 6k+5
    
    Reading: https://en.wikipedia.org/wiki/Primality_test#Python
    """
    if (n <= 3):
        return (n > 1)
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    for i in range(5, math.isqrt(n)+1, 6):      # Loop for 6k + 5
        if (n % i == 0) or (n % (i+2) == 0):    # i+2 = 6k+5+2 = 6(k+1) + 1
            return False
    return True


def is_square(n: int) -> bool:
    """This function return if input number is square"""
    if n < 2:
        return n >= 0
    rounded_square_n = math.isqrt(n)
    return rounded_square_n**2 == n


def is_triangular_number(n: int) -> bool:
    """ This function will check if a number is a triangular number:
    
    Triangular number T is defined as: 
    T(n) = 1 + 2 + 3 + ... + n = n*(n+1)/2

    This function use Triangular test:
    - Let T(n) = x 
    - 8x + 1 must be square number
    
    Prove:
    8x + 1 = 8*n*(n+1)/2 + 1 = 4n(n+1) + 1 = 4(n^2) + 4n + 1 = (2n+1)^2

    Reading:
    https://en.wikipedia.org/wiki/Triangular_number#Triangular_roots_and_tests_for_triangular_numbers
    """
    return is_square(8*n+1)


def least_common_multiple(a:int, b:int) -> int:
    """This function return Least Common Multiple of a and b
    Ref: https://en.wikipedia.org/wiki/Greatest_common_divisor#Least_common_multiple"""
    return (a*b) // greatest_common_divisor_recursive(a,b)
 

def one_to_n_sum(n: int) -> int:
    """ Calculate the sum of numbers from 1 to n:
    S(n) = 1 + 2 + 3 + ... + n = n*(n+1)/2
    Using n*(n+1)//2 is quicker than int(n*(n+1)/2) since it does not involve handing float numbers

    Ref: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    Proof: https://proofwiki.org/wiki/Closed_Form_for_Triangular_Numbers
    """
    return n*(n+1)//2


def one_to_n_square_sum(n: int) -> int:
    """ Calculate the sum of square numbers from 1 to n:
    S(n) = 1^2 + 2^2 + 3^2 + ... + n^2 = n*(n+1)*(2*n+1)/6 

    Ref: https://en.wikipedia.org/wiki/Square_pyramidal_number
    Proof: https://proofwiki.org/wiki/Sum_of_Sequence_of_Squares
    """
    return n*(n+1)*(2*n+1) // 6


def proper_divisors_list(n: int) -> Iterator[int]:
    """ This function return the proper divisors of n (number less than n which divide evenly into n)"""
    yield 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            if i * i == n:
                yield i
            else:
                yield i
                yield n//i


def proper_divisors_sum_list(limit: int) -> list:
    """ This function return the divisors sum list from 0 to limit, for more indeep prove, check question 21"""
    sum_list = [0]*(limit+1)
    for divisor in range(1, limit//2 + 1):
        index = divisor*2
        while index < limit+1:
            sum_list[index] += divisor
            index += divisor
    return sum_list


def reduced_fraction(a:int, b:int) -> tuple[int, int]:
    common_divisor = greatest_common_divisor_recursive(a,b)
    if common_divisor == 1:
        return a,b
    return a//common_divisor, b//common_divisor


def s_gonal_number(side: int, index: int) -> int:
    """ This function return the Polygonal number, given side and index
    Input: side >= 2, index >= 1
    Output: P(side,index)
    Reading: https://en.wikipedia.org/wiki/Polygonal_number
    """
    return (side-2)*(index*(index-1)//2) + index


def sieve_of_eratosthenes(limit: int) -> list:
    """ Return list of all prime below input 'n'
    consumes O(n) of the memory and performs O(n log log n)

    Reading list:
    - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    - https://t5k.org/glossary/page.php?sort=SieveOfEratosthenes
    - https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
    """
    # Create array of True value
    num_list = [True]*limit
    for i in range(2, math.isqrt(limit)+1):
        # if current index is prime (value = True)
        if num_list[i] == True:
            # then other n*i will be set to False => not prime
            j = i + i
            while j < limit:
                num_list[j] = False
                j += i
    # Ramaining True indices are prime numbers
    return [i for i in range(2, len(num_list)) if num_list[i] == True]


def totient_1_to_n(n:int) -> list:
    """ Create the list of totient numbers from 1 to n.
    The idea is based on Sieve of Eratosthenes.
    
    Reading: https://cp-algorithms.com/algebra/phi-function.html#etf_1_to_n
    """
    phi = [i for i in range(n+1)]

    for i in range(2, n+1):
        if phi[i] == i:
            for j in range(i, n+1, i):
                phi[j] -= phi[j] // i

    return phi


def totient_n(n):
    """ Compute Euler's totient function (phi function) for a given number n.

    Reading list:
    - https://mathworld.wolfram.com/TotientFunction.html
    - https://en.wikipedia.org/wiki/Euler%27s_totient_function
    - https://cp-algorithms.com/algebra/phi-function.html#implementation
    """
    result = n

    # Check division by 2
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        result -= result // 2

    # Check division by odd numbers
    i = 3
    while True:
        if i*i > n:
            break
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i   # Or result = result * (i - 1) // i
        i += 2

    # If n is still > 1 => n is prime
    if n > 1:
        result -= result // n       # Or result = result * (n - 1) // n
    return result