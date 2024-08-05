#Solve all quadratic equations, returns both solutions (roots) as a tuple. Note: Sometimes the roots are complex numbers.
class Quadratic:
    #stores the values in the eq.
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.formula = f'{a}x^2 {b}x {c} = 0'

    #The quadratic formula includes a section, sqrt(b^2 - 4ac), inside of -b{}/2a, which is both added and subtracted, to return 2 solutions
    def inner(self):
        a, b, c = self.a, self.b, self.c
        return (b**2 - 4*a*c)**(1/2)
     
    def calc(self, inner):
        a, b = self.a, self.b
        return (-b + inner)/(2*a)
    
    def quad(self):
        a,b,c, calc,inner = self.a, self.b, self.c, self.calc, self.inner
        p = self.calc(self.inner())
        q = self.calc(-1*self.inner())
        #Uses both the + and - of inner() to return both roots of the quadratic
        return (p, q)
        
#For example
eg = Quadratic(3, 13, 12)
print(eg.formula, '  equals  ', eg.quad())
# -4/3 and -3