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

def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n*factorial(n-1) 

def is_even(n: int) -> bool:
    """This function check if number is even or not. By using result of n % 2 == 0"""
    return (n % 2 == 0)

def is_panlindromic(n: int) -> bool:
    """This function check if number n is panlidromic
    - Turn n into string
    - Create reverse_n, ref: https://www.w3schools.com/python/python_howto_reverse_string.asp
    - Then compare string_n with reverse_n
    """
    string_n = str(n)
    reverse_n = string_n[::-1]    
    return (string_n == reverse_n)

def is_prime(n: int) -> bool:
    """Ref: https://en.wikipedia.org/wiki/Primality_test#Python
    If we write the prime number in the form of (p = 6k + i), with i=[0,1,2,3,4,5]
    We can see that:
        - with i=[0,2,4] -- 6k+i is divisible by 2
        - with i=[0,3] -- 6k+i is divisible by 3
    So first check divisble by 2 and 3, then check for every p = 6k+1 and 6k+5
    """
    if (n <= 3):
        return (n > 1)
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    for i in range(5, math.isqrt(n)+1, 6):      # Loop for 6k + 5
        if (n % i == 0) or (n % (i+2) == 0):
            return False
    return True

def least_common_multiple(a:int, b:int) -> int:
	"""This function return Least Common Multiple of a and b
	Ref: https://en.wikipedia.org/wiki/Greatest_common_divisor#Least_common_multiple"""
	return (a*b) // math.gcd(a,b)

def one_to_n_sum(n: int) -> int:
    """Ref: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    Proof: https://proofwiki.org/wiki/Closed_Form_for_Triangular_Numbers
    S(n) = 1 + 2 + 3 + ... + n = n*(n+1)/2
    Using n*(n+1)//2 seems to be quicker than int(n*(n+1)/2) since it does not involve handing float numbers
    """
    return n*(n+1)//2

def one_to_n_square_sum(n: int) -> int:
    """S(n) = 1^2 + 2^2 + 3^2 + ... + n^2 = n*(n+1)*(2*n+1)/6 = (n**3)/3 + (n**2)/2 + n/6
    Ref: https://en.wikipedia.org/wiki/Square_pyramidal_number
    Proof: https://proofwiki.org/wiki/Sum_of_Sequence_of_Squares"""
    return n*(n+1)*(2*n+1) // 6

def proper_divisors_list(n: int) -> Iterator[int]:
    """This function return the proper divisors of n (number less than n which divide evenly into n)"""
    yield 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            if i * i == n:
                yield i
            else:
                yield i
                yield n//i


def sieve_of_eratosthenes(limit: int) -> list:
    """Ref: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Ref 2: https://t5k.org/glossary/page.php?sort=SieveOfEratosthenes
    Return list of all prime below input 'n'
    consumes O(n) of the memory and performs O(n log log n)
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

