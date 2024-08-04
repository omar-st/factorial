def fac(n):  #n!
    k = 1
    for i in range(1,n+1):
        k *= i
    return k

def subset(n, k):  #n choose k; how many subsets of k elements in set of n elements.
    subsets = fac(n) / ( fac(n - k) * fac(k) )
    return int(subsets)

def main():
    total_elements = 10  #edit for any size
    choose_n_elements = 6  #edit for any size < total
    print( fac( total_elements))
    print( subset( total_elements, choose_n_elements))

main()