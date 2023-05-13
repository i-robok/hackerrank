import sys

def pythagoreanTriplets(n):
    triplets = []

    for a in range(1, n - 1):
        for b in range(a, n):
            c = n - a - b
            if (c > 0) and (a**2 + b**2 == c**2):
                triplets.append([a, b, c])

    return triplets

def pythagoreanTripletLargestProduct(n):
    largest_product = -1
    lim_n = (n // 2)
    
    for a in range(1, lim_n + 1):
        for b in range(a, lim_n + 1):
            c = n - a - b
            if (c > 0) and (a**2 + b**2 == c**2):
                largest_product = max(largest_product, a * b * c)

    return largest_product

def pythagoreanTripletLargestProduct_gpt(n):
    largest_product = -1
    # lim_n = int(n ** 0.5) + 1
    if (n < 4):
        return -1
    
    lim_n = (n // 2) + 1

    for a in range(1, lim_n + 1):
        b = (n**2 - 2*n*a) // (2*n - 2*a)
        if (b > 0):
            c = n - a - b

            if (c > 0) and (a**2 + b**2 == c**2):
                print(f'n={n} -> a={a}, b={b}, c={c}')
                largest_product = max(largest_product, a * b * c)

    return largest_product


def test_function(func, param):
    import time

    ntests = 1
    print(f'-> Testing {func.__name__}({param}) ... * {ntests}')

    start_time = int(time.time() * 1000)
    for n in range(ntests):
        result = func(param)
    stop_time = int(time.time() * 1000)

    print(f'    {func.__name__}({param}) * {ntests} = {stop_time - start_time} ms')

    print(f'    Results = {result}')


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    for i in range(n, n + 1):
        rc1 = pythagoreanTripletLargestProduct(i)
        rc2 = pythagoreanTripletLargestProduct_gpt(i)

        if (rc1 == rc2):
            print(f'Error for {i}: {rc1} != {rc2}')
            triplets = pythagoreanTriplets(n)
            for triplet in triplets:
                # print(triplet)
                if triplet[0] + triplet[1] + triplet[2] == n:
                    if triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2:
                        print(f'Exito: {triplet}')
                    else:
                        print(f'Error: {triplet[0] ** 2} + {triplet[1] ** 2} != {triplet[2] ** 2}')
                else:
                    print(f'Error: {triplet[0]} + {triplet[1]} + {triplet[2]} != {n}')

    '''''
    test_function(pythagoreanTripletLargestProduct_gpt, n)
    test_function(pythagoreanTripletLargestProduct, n)

    triplets = pythagoreanTriplets(n)
    for triplet in triplets:
        # print(triplet)
        if triplet[0] + triplet[1] + triplet[2] == n:
            if triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2:
                print(f'Exito: {triplet}')
            else:
                print(f'Error: {triplet[0] ** 2} + {triplet[1] ** 2} != {triplet[2] ** 2}')
        else:
            print(f'Error: {triplet[0]} + {triplet[1]} + {triplet[2]} != {n}')
    '''
