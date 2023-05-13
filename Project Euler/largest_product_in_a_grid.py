

def getLargestProductInAGrid(grid):

    largestProduct = 0
    L = 4

    # Multiplicar horizontales.
    for i in range(len(grid)):
        for j in range(len(grid[i]) - L + 1):
            product = 1
            for k in range(L):
                product *= grid[i][j + k]

            largestProduct = max(largestProduct, product)

    # Multiplicar verticales.
    for i in range(len(grid) - L + 1):
        for j in range(len(grid[i])):
            product = 1
            for k in range(L):
                product *= grid[i + k][j]

            largestProduct = max(largestProduct, product)

    # Multiplicar diagonales positivas.
    for i in range(len(grid) - L + 1): 
        for j in range(len(grid[i]) - L + 1):
            product = 1
            for k in range(L):
                product *= grid[i + k][j + k]

            largestProduct = max(largestProduct, product)

    # Multiplicar diagonales negativas.
    for i in range(len(grid) - L + 1):
        for j in range(L - 1, len(grid[i])):
            product = 1
            for k in range(L):
                product *= grid[i + k][j - k]

            largestProduct = max(largestProduct, product)

    return largestProduct


def test_function(func, param, ntests = 100):
    import time

    print(f'-> Testing {func.__name__}({param}) ... * {ntests}')

    start_time = int(time.time() * 1000)
    for n in range(ntests):
        result = func(param)
    stop_time = int(time.time() * 1000)

    print(f'    {func.__name__}({param}) = {result}')
    print(f'    {func.__name__}({param}) * {ntests} = {stop_time - start_time} ms')


if __name__ == '__main__':
    grid = []
    for grid_i in range(20):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid.append(grid_t)
        
    test_function(getLargestProductInAGrid, grid, 1000)