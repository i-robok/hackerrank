import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Rutinas para calcular los numeros primos menores a 'n'.

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def primes_half_sieve(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)

    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def primes_numpy(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a array of primes, 3 <= p < n """
    sieve = np.ones(n//2, dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False

    return np.r_[2, ((2 * np.nonzero(sieve)[0][1::] + 1) | 1)]

def primes_numpy_third_sieve(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2, 3, ((3*np.nonzero(sieve)[0][1:]+1) | 1)]

def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = np.arange(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


# Rutinas para calcular el n-esimo numero primo.

def prime_n_half_sieve(n):
    """ Returns the nth prime """

    if n <= 1:
        return 2

    sieve_size = 2 * 10 ** 5
    sieve = [True] * (sieve_size // 2)

    # for i in range(3,int(n**0.5)+1,2):
    i = 3
    nof_primes = 1  # 2 es primo y partimos nuestra busqueda desde 3.
    while True:
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((sieve_size - i*i - 1)//(2*i)+1)
            nof_primes += 1

        if nof_primes >= n:
            break

        i += 2
            
    return i


# Rutinas para descomponer un numero en sus factores primos.

def prime_factors(n):
    max_prime = 10 ** 7 + 1
    primos = primes_half_sieve(min(n + 1, max_prime))

    x = n
    p_factors = []
    for p in primos:
        while x % p == 0:
            p_factors.append(p)
            x = x // p

        if x <= 2:
            break

    if (x > max_prime):
        # Es un primo muy grande ?
        p_factors.append(x)
    elif (x > 2):
        sub_factors = prime_factors(x)
        p_factors.extend(sub_factors)
        
    return p_factors

def prime_factors_gpt(n):
    # descomponer n en factores primos
    factores = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factores.append(d)
            n //= d
        d += 1

    if n > 1:
        factores.append(n)

    return factores

# Calcular la suma de los primos "no mayores" a n.

def summationOfPrimesSieve(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a list of sum of primes < i for i in range(1, n) """
    sieve = [True] * (n + 1)
    summation = [0] * (n + 1)
    summation[0] = 0
    summation[1] = 0
    summation[2] = 2

    # for i in range(3,int(n**0.5)+1,2):
    for i in range(2,n + 1,1):
        if sieve[i]:
            sieve[i*i::i]=[False]*((n-i*i)//(i)+1)
            summation[i] = summation[i-1] + i
        else:
            summation[i] = summation[i-1]

    return summation



# Rutinas de pruebas y test.

def get_max_prime_factor(n, prime_factors_func):

    p_factors = prime_factors_func(n)
    print(f'{prime_factors_func.__name__}({n}) = {p_factors}')

    debug = False
    if (debug):
        validacion = 1
        for p in p_factors:
            validacion *= p

        if validacion != n:
            print(f'error: {validacion} != {n}')
        else:
            print(f'exito: {validacion} == {n}')

    max_factor = p_factors[0]
    for p in p_factors:
        if p > max_factor:
            max_factor = p 
        
    # print(f'max factor={max_factor}')
    return max_factor


def summationOfPrimes(n, summation = None):
    if summation is None:
        summation = summationOfPrimesSieve(n)

    return summation[n]


def summationOfPrimesControl(n, primes = None):
    if primes is None:
        primes = primes_half_sieve(n)
        
    sum = 0
    for p in primes:
        if p > n:
            break
        sum += p
    return sum


def test_function(func, param, ntests = 100):

    print(f'-> Testing {func.__name__}({param}) ... * {ntests}')

    start_time = int(time.time() * 1000)
    for n in range(ntests):
        result = func(param)
    stop_time = int(time.time() * 1000)

    print(f'    {func.__name__}({param}) = {result}')
    print(f'    {func.__name__}({param}) * {ntests} = {stop_time - start_time} ms')




if __name__ == '__main__':

    import time

    tests = [5]

    if (0 in tests):
        start_time = int(time.time() * 1000)

        primes = primes_half_sieve(10 ** 6 + 1)
        summation = summationOfPrimesSieve(10 ** 6)

        test_cases = range(2, 10 ** 6)
        for test in test_cases:

            rc1 = summationOfPrimes(test, summation)
            # rc2 = summationOfPrimesControl(test, primes)

            #if (rc1 !=  rc2):
            #    print(f'ERROR para {test}: {rc1} <> {rc2}')

        # test_function(summationOfPrimes, test, 1)
        # test_function(summationOfPrimesControl, test, 1)

        stop_time = int(time.time() * 1000)
        print(f'3.- Duracion total = {stop_time - start_time} ms')

    if (1 in tests):
        start_time = int(time.time() * 1000)
        test_cases = [600851475143, 293103132237, 392373671]
        for test in test_cases:
            rc1 = get_max_prime_factor(test, prime_factors_gpt)
            rc2 = get_max_prime_factor(test, prime_factors)

            if (rc1 == rc2):
                print(f'Exito para {test}: {rc1}')
            else:
                print(f'ERROR para {test}: {rc1} <> {rc2}')

        stop_time = int(time.time() * 1000)
        print(f'Duracion = {stop_time - start_time} ms')

    if (2 in tests):
        # Tests de performance.
        start_time = int(time.time() * 1000)
        test_cases = [600851475143, 293103132237, 392373671]
        for test in test_cases:
            test_function(prime_factors, test)

        stop_time = int(time.time() * 1000)
        print(f'Duracion = {stop_time - start_time} ms')

        start_time = int(time.time() * 1000)
        test_cases = [600851475143, 293103132237, 392373671]
        for test in test_cases:
            test_function(prime_factors_gpt, test)

        stop_time = int(time.time() * 1000)
        print(f'Duracion = {stop_time - start_time} ms')

    if (3 in tests):
        start_time = int(time.time() * 1000)

        test_cases = [10 ** 4] # range(2, 100)
        for test in test_cases:
            print(f'{prime_n_half_sieve(test)}', end=', ')
        print()

        test_function(prime_n_half_sieve, 10 ** 4)

        stop_time = int(time.time() * 1000)
        print(f'3.- Duracion total = {stop_time - start_time} ms')

    if (4 in tests):
        start_time = int(time.time() * 1000)

        test_cases = [2, 3, 5, 7,10, 2 * 10 ** 9] # range(2, 100)
        for test in test_cases:
            print(f'Primes <= {test}: {primes_half_sieve(test + 1)}')

        stop_time = int(time.time() * 1000)
        print(f'4.- Duracion total = {stop_time - start_time} ms')

    if (5 in tests):
        start_time = int(time.time() * 1000)

        test_cases = [2, 3, 5, 7,10, 2 * 10 ** 9] # range(2, 100)
        for test in test_cases:
            if is_prime(test):
                print(f'{test} is prime')
            else:
                print(f'{test} is not prime')

        stop_time = int(time.time() * 1000)
        print(f'5.- Duracion total = {stop_time - start_time} ms')