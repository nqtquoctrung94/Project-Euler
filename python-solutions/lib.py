# Prepared function that commonly used in solving problems

import math


def one_to_n_sum(n: int) -> int:
    '''Ref: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    The sum from one to n is defined as
    S(n) = 1 + 2 + 3 + ... + n
    Using n*(n+1)//2 seems to be quicker than int(n*(n+1)/2) since it does not involve handing float numbers
    '''
    return n*(n+1)//2


def is_prime(n: int) -> bool:
    '''Ref: https://en.wikipedia.org/wiki/Primality_test#Python
    If we write the prime number in the form of (p = 6k + i), with i=[-1,0,1,2,3,4]
    We can see that:
        - with i=[0,2,4], 6k+i is divisible by 2
        - with i=[0,3], 6k+i is divisible by 3
    So first check if number are divisble by 2 and 3 first, then check for every p = 6k+-1
    '''

    if (n <= 3):
        return (n > 1)
    
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    
    for i in range(5, math.isqrt(n)+1, 6):      # Loop for 6k + 5
        if (n % i == 0) or (n % (i+2) == 0):
            return False
        
    return True


def Sieve_of_Eratosthenes(limit: int) -> list:
    '''Ref: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Return list of all prime below input 'n'
    consumes O(n) of the memory and performs O(n log log n)
    '''

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
    prime_list = [i for i in range(2,len(num_list)) if num_list[i] == True]

    return prime_list

