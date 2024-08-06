**README for Angle Class**

The `Angle` class is a Python implementation that uses Taylor series expansions to compute sine and cosine values of any angle given in radians. The class builds upon the `Quantity` class provided, which handles polynomial expressions and derivatives/integrals.

**Key Features:**

* Uses Taylor series expansions up to 10th order for both sine and cosine functions
* Accepts an input angle in radians as a float or int value
* Provides methods to compute sin and cos values of the input angle

**Source Code Explanation**

The `Angle` class has two key components:

1. **Initialization**: The `__init__` method takes an input radius (r) which represents the size of the angle in radians. It also initializes a `taylor` object from the `Quantity` class to generate Taylor series expansions.
2. **Sine and Cosine Methods**:
	* `sin`: This method uses the Taylor series expansion of sine to compute the sin value of the input angle (r). It iterates up to 5 terms in the series, adding or subtracting each term depending on its parity.
	* `cos`: Similar to the `sin` method, this function uses the Taylor series expansion of cosine to compute the cos value of the input angle (r). It also iterates up to 5 terms in the series, adding or subtracting each term depending on its parity.

**Example Usage:**

```python
theta = Angle(1.25)
print(theta.sin())  # sin value of 1.25 radians
print(theta.cos())  # cos value of 1.25 radians
```

Note that this implementation assumes the input angle is in radians. If you need to work with degrees, you can convert them using the `math.radians()` function from the Python math module.

