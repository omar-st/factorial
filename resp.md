## Overview
The `Quantity` class is a simple mathematical tool designed to represent polynomial terms of the form ax^n, where 'a' is the coefficient and 'n' is the exponent.

## Usage
To use the `Quantity` class, create an instance by passing in the desired coefficient and exponent values. For example:
```python
q = Quantity(4, 3)  # represents the term 4x^3
```

You can then perform the basic operations of calculus on this term using the `dx()` method for differentiation and the `ix()` method for integration. They take as their argument the number of differentiations or integrations you wish to perform.

## Methods

### dx(count)

* Function: Compute the kth derivative of the polynomial term 'ax^n' with respect to x, up to the specified depth (k/count).
* Parameters: count (int) - The number of derivatives to take.
* Returns: A tuple containing the new coefficient and exponent values after differentiation. For example:
```python
print(q.dx(2))  # outputs (24, 1), representing the term 24x
```

### ix(count)

* Description: Compute the kth integral of the polynomial term 'ax^n' with respect to x, up to the specified depth (k/count).
* Parameters: count (int) - The number of integrals to take.
* Returns: A tuple containing the new coefficient and exponent values after integration. For example:
```python
print(q.ix(1))  # outputs (4, 4), representing the term x^4
```
