# README for Pythagorean

## RightTriangle Class
A Python class designed to calculate the length of sides in a right-angled triangle using the Pythagorean Theorem.

### Features
* Calculates the length of any side (adjacent, opposite, or hypotenuse) given the other two sides.
* You must pass two side lengths and a zero to the constructor for it to return the value of the missing side.
* If you pass just two side lengths, it will assume the hypotenuse is the unknown.

### Usage
1. Create a new instance of the `RightTriangle` class by passing in the lengths of each known side, and zero for the unknown side.
2. Call the `pyth()` method to get the length of the intended side.

**Example Use Cases**
* Find the length of the hypotenuse given the lengths of the other two sides: `RightTriangle(3, 4, 0)`
* Find the length of the opposite given the other two: `RightTriangle(5, 0, 13)`
* Find the length of the adjacent given the other two: `RightTriangle(0, 15, 17)`

### Notes
This code uses a simple if-else statement to determine which side to calculate based on the input. 
The `goal()` method checks which side is missing, so `pyth()` can solve for that side.
The code has no import statements or dependencies.
*MIT Licensed. Reuse and modify without restriction.*