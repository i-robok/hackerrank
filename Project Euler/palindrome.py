

def num_is_palindrome(n: int):
    temp=n
    rev=0
    while(n > 0):
        rev = rev * 10 + (n % 10)
        n = n // 10

    return temp == rev


def num_is_palindrome_2(n: int):
    return str_is_palindrome(str(n))


def str_is_palindrome(s: str):
    return s == s[::-1]


def nof_digits(n: int):
    return len(str(n))



def test_function(func, ntests, num):

    import time

    print(f'Testing {func.__name__}() ...')

    start_time = int(time.time() * 1000)
    for n in range(ntests):
        rc = func(num)
    stop_time = int(time.time() * 1000)

    print(f'{func.__name__}() * {ntests} = {stop_time - start_time} ms')

def largest_palindrome_less_than(n: int):

    n_max = 999
    n_min = 100

    largest_palindrome = 0

    for d in range(n_max, n_min, -1):
        # print(f'd={d}')
        if d < (n_max - n_min) // 2:
            ancho = d - n_min + 1
        else:
            ancho = n_max - d + 1

        debug = False # (d == 143)

        if (d * (d + ancho) > largest_palindrome) and ((d - ancho) * d <= n):

            for k in range(ancho - 1):
                i, j = d - k, d + 1 + k
                if debug: print(f'{i},{j}')
                if ((i >= n_min and j <= n_max) and (i * j < n) and num_is_palindrome_2(i * j) and (i * j > largest_palindrome)):
                    largest_palindrome = i * j
                    if debug: print(f'd={d}, k={k}, {i},{j} = {i * j}')
                    # return(i * j)

            for k in range(ancho):
                i, j = d - k, d + k
                if debug: print(f'{i},{j}')
                if ((i >= n_min and j <= n_max) and (i * j < n) and num_is_palindrome_2(i * j) and (i * j > largest_palindrome)):
                    largest_palindrome = i * j
                    if debug: print(f'd={d}, k={k}, {i},{j} = {i * j}')
                    # return(i * j):

    return largest_palindrome


if __name__ == '__main__':

    if (True):
        # largest palindorme product
        import time

        start_time = int(time.time() * 1000)

        for i in range(100):
            largest_palindrome = largest_palindrome_less_than(10 ** 6)
            largest_palindrome = largest_palindrome_less_than(101110)
            print(largest_palindrome)
            largest_palindrome = largest_palindrome_less_than(800000)
            print(largest_palindrome)

        stop_time = int(time.time() * 1000)

        print(f'{stop_time - start_time} ms')

        print(largest_palindrome)
                    

    if (False): 
        # test de performance
        nof_tests = 10 ** 6
        num = 1234567890987654321

        test_function(num_is_palindrome, nof_tests, num)
        test_function(num_is_palindrome_2, nof_tests, num)

    if (False):
        # read from stdin
        import sys

        for line in sys.stdin:
            n = int(line.strip())
        
            if(num_is_palindrome(n)):
                print("The number is palindrome!")
            else:
                print("Not a palindrome!")