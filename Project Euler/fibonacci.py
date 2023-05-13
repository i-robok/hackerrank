

def fibonacci(max_value):

    fib = [1, 2]
    n = len(fib)
    while (fib[n - 2] + fib[n - 1]) < max_value:
        fib.append(fib[n - 2] + fib[n - 1])
        n += 1
        
    return(fib)

if __name__ == "__main__":
    fib = fibonacci(4 * 10 ** 16) 

    suma = sum(x for x in fib if x % 2 == 0)

    print(f'suma={suma}')