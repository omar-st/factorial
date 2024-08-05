# Quadratic Class README
This Python class `Quadratic` is designed to solve quadratic equations of the form `ax^2 + bx + c = 0`, where `a`, `b`, and `c` are coefficients.

## Features
* The class takes in three parameters: `a`, `b`, and `c`
* It uses the quadratic formula to calculate two solutions for the equation.

## Methods
### `__init__(self, a, b, c=0)`:
* Initializes the class with coefficients `a`, `b`, and `c`.
### `inner(self)`:
* Calculates the inner part of the quadratic formula: `(b**2 - 4*a*c)**(1/2)`.
### `calc(self, inner)`:
* Uses the inner part to calculate one solution for the equation.
### `quad(self)`:
* Calls `calc` twice, where `calc` is passed positive and negative values of in the inner formula, to return 2 solutions.

## Example Usage
```python
eg = Quadratic(3, 13, 12)
print(eg.formula, '  equals  ', eg.quad())
```
This will output:
```
3x^2 + 13x + 12 = 0  equals   (-4/3, -3)
```

## Import Statements and Dependencies
* None are needed for this mathematics class.
## MIT Licensed. Reuse and modify without restriction.