## Quantity Class
The `Quantity` class is a simple mathematical tool designed to represent polynomial terms of the form ax^n, where 'a' is the coefficient and 'n' is the exponent.

### Usage
To use the `Quantity` class, create an instance by passing in the desired coefficient and exponent values. For example:
```python
q = Quantity(4, 3)  # represents the term 4x^3
```

You can then perform the basic operations of calculus on this term using the `dx()` method for differentiation and the `ix()` method for integration. They take as their argument the number of differentiations or integrations you wish to perform.

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
### Taylor Progression
The taylor series is the sequence of values yielded by repeated integrations. In its most basic form, you can add the terms to yield other mathematical quantities. eg, adding every integral of x yields e^x; including only integrals with odd degree (exponent) and alternately adding and subtracting them yields sin(x), and doing the same with only integrals of even degree yields cos(x).

***
## Euler Function
The Euler Function, defined in math as f(x) = e^x, where e is the base of the natural logarithm. e is the number such that its derivative or integral is itself. 
* The Taylor series is used to compute the Euler function
* Every integral of the series is added
* The sum of the integrals of x is equal to e^x
* This is because the sum of integrals will yield an exponentional process, where the base of the exponential must be the number whose integral is itself: e.

***
## Angle Class
The `Angle` class is a Python implementation that uses Taylor series expansions to compute sine and cosine values of any angle given in radians. The class builds upon the `Quantity` class above, which handles polynomial expressions and derivatives/integrals.

### Features:
* Uses Taylor series expansions up to 10th order for both sine and cosine functions
* Accepts an input angle in radians as a float or int value
* Provides methods to compute sin and cos values of the input angle

### Source Explanation
The `Angle` class has two key components:

1. **Initialization**: The `__init__` method takes an input radius (r) which represents the size of the angle in radians. It also initializes a `taylor` object from the `Quantity` class to generate Taylor series expansions.
2. **Sine and Cosine Methods**:
	* `sin` and `cos` These methods use the Taylor series expansion of sine and cosine to compute the said values of an input angle (r). It iterates over the first 16 terms of the series; adding, subtracting, or excluding each term depending on its parity.

**Example Usage:**
```python
theta = Angle(1.25)
print(theta.sin())  # sin value of 1.25 radians
print(theta.cos())  # cos value of 1.25 radians
```
Note that this implementation assumes the input angle is in radians.
