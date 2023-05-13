
def dec_to_bin(n: int):
    sbin = ''

    if (n == 0):
        sbin = '0'

    else:
        while (n > 0):
            if (n % 2 == 0):
                sbin = '0' + sbin
            else:
                sbin = '1' + sbin
            n = int(n / 2)

    return sbin

def count_ones(sbin: str):
    nones = 0
    max_nones = 0

    for d in range(len(sbin)):
        if sbin[d:d+1] == '0':
            nones = 0
        else: # bin[d:d+1] == '1'
            if (d == 0) or sbin[d-1:d] == '0':
                nones = 1
            else:
                nones += 1

        if nones > max_nones:
            max_nones = nones

    return (max_nones)

n = 3
bin = dec_to_bin(n)
print(f'{n} -> {bin}')    
print(f'{count_ones(bin)}')