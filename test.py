

for x in range(3*10**8,10**9,10**5):
    n = int((x - 1) / 3)

    suma_1 = int(3 * (n * (n + 1)//2))
    suma_2 = sum(range(3,x,3))

    if x % 1000 == 0:
        print(f'{x}')

    if suma_1 != suma_2:
        print(f'Diferencia para {x}:{n}: {suma_1} - {suma_2} = {suma_1 - suma_2}')
        break