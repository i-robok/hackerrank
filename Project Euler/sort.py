
def sortHackerRank(alist):
    n = len(alist)
    totalSwaps = 0
    
    for i in range(n):
        numberOfSwaps = 0
        
        for j in range(n - 1):
            if alist[j] > alist[j + 1]:
                # swap ??
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                numberOfSwaps += 1
                
        totalSwaps += numberOfSwaps
        
        if numberOfSwaps <= 0:
            break
        
    return totalSwaps



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    nofSwaps = sortHackerRank(a)
    print(f'Array is sorted in {nofSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[len(a) - 1]}')
