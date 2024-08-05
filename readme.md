
# Readme / Documentation

1. `fac(n)`: calculates the factorial of a given integer `n`.
2. `subset(n, k)`: computes the number of subsets with `k` elements from a set of `n` elements.
3. `main()`: Demonstrates using each math function.

## Function 1: `fac(n)`
Calculates the factorial of a given integer `n`.
```python
def fac(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k
```
This function uses a loop to calculate the product of all integers from 1 to `n`. The result is returned as an integer.

## Function 2: `subset(n, k)`
Computes the number of subsets with `k` elements from a set of `n` elements.
```python
def subset(n, k):
    subsets = fac(n) / (fac(n - k) * fac(k))
    return int(subsets)
```
This function uses the formula for combinations to calculate the number of subsets with `k` elements from a set of `n` elements. It first calculates the factorial of `n`, then divides it by the product of the factorials of `(n-k)` and `k`. The result is returned as an integer.

## Main Function
The main function is a demonstration that uses the above functions by calculating the factorial of 10 and the number of subsets with 6 elements from a set of 10 elements.
```python
def main():
    total_elements = 10
    choose_n_elements = 6
    print(fac(total_elements))
    print(subset(total_elements, choose_n_elements))

main()
```

Note that if you want to reuse this code, you may want to just call the fac() and subset() functions directly. The code and docs are all MIT Licensed.