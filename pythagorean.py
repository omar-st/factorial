#Applies the Pythogrean Theorem any right angled triangle.
class RightTriangle:
    #Each argument is the length of a side
    #When initializing, pass one argument as zero so the program will solve for that side
    def __init__(self, adjacent, opposite, hypotenuse):
        self.ad = adjacent
        self.op = opposite
        self.hy = hypotenuse
    
    def goal(self):
        if self.ad == 0:
            return 'a'
        elif self.op == 0:
            return 'o'
        else:
            return 'h'
    
    def pyth(self):
        if self.goal() == 'a':
            ans = (self.hy**2 - self.op**2)**0.5
        elif self.goal() == 'o':
            ans = (self.hy**2 - self.ad**2)**0.5
        else:
            ans = (self.ad**2 + self.op**2)**0.5
        return ans

#Examples of the solution being run
eg = RightTriangle(3, 4, 0)
ej = RightTriangle(5, 0, 13)
ek = RightTriangle(0, 15, 17)
print(f'{eg.pyth()} \n {ej.pyth()} \n {ek.pyth()}')