

def get_smallest_multiple_brute_force(N: int):
    # minimo comun multiplo de los numeros de 1 a n.

    # the worst candidate is the product of all numbers from 1 to n.
    smallest = 1
    for x in range(N):
        smallest *= (x + 1)

    for x in range(1, smallest):
        is_divisible = True
        for n in range(1, N + 1):
            if x % n != 0:
                is_divisible = False
                break
        if (is_divisible):
            smallest = x
            break

    return smallest

def mcm_n(n):
    # inicializar un diccionario para almacenar las descomposiciones en factores primos
    factores = {}
    
    # iterar sobre los numeros del 1 al n
    for i in range(1, n+1):
        # descomponer el numero i en factores primos
        factores_i = {}
        d = 2
        while d*d <= i:
            while (i % d) == 0:
                if d in factores_i:
                    factores_i[d] += 1
                else:
                    factores_i[d] = 1
                i //= d
            d += 1
        if i > 1:
            if i in factores_i:
                factores_i[i] += 1
            else:
                factores_i[i] = 1
        
        # actualizar el diccionario global de factores primos
        for factor, potencia in factores_i.items():
            if factor in factores:
                if potencia > factores[factor]:
                    factores[factor] = potencia
            else:
                factores[factor] = potencia
    
    # calcular MCM a partir de los factores primos
    mcm = 1
    for factor, potencia in factores.items():
        mcm *= factor ** potencia
    
    return mcm



if __name__ == '__main__':
    import time

    start_time = int(time.time() * 1000)

    for i in range(10):
        mcm_1 = mcm_n(20)
        print(f'mcm = {mcm_1}')
        '''
        mcm_2 = get_smallest_multiple_brute_force(i)
        if (mcm_1 == mcm_2):
            print(f'Exito: mcm = {mcm_1}')
        else:
            print(f'ERROR: {mcm_1} <> {mcm_2}')
        '''

    stop_time = int(time.time() * 1000)

    print(f'{stop_time - start_time} ms')



    
