

def sum_square_diff(n):

    square_sum = n * (n + 1) * (2 * n + 1) // 6
         
    sum_square = (n * (n + 1) // 2) ** 2
    
    return abs(sum_square - square_sum)


def test_function(func, param):
    import time

    ntests = 10 ** 4
    print(f'-> Testing {func.__name__}({param}) ... * {ntests}')

    start_time = int(time.time() * 1000)
    for n in range(ntests):
        result = func(param)
    stop_time = int(time.time() * 1000)

    print(f'    {func.__name__}() * {ntests} = {stop_time - start_time} ms')

    print(f'    Results = {result}')


if __name__ == '__main__':

    test_function(sum_square_diff, 10 ** 4)