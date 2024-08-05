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
        
class Cubic:
    #continue here to make it work for all cubics.
    #stores the values in the eq.
    def __init__(self, a, b, c, d=0):
        self.formula = f'{a}x^3 {b}x^2 {c}x {d} = 0'
        self.a = 1
        self.b = b/a
        self.c = c/a
        self.d = d/a

    def inner(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        print(a, b, c, d)
        val = ( 
            -((b**3) / 27) 
            + ((b*c) / 6) 
            - (d/2) 
            )
        print(val)
        return val

    def diff(self):
        a, b, c = self.a, self.b, self.c
        print(a, b, c)
        val = (
            c/3 - (b**2)/9
            )
        print(val)
        return val

    def cube(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        p, q = self.inner(), self.diff()
        val = (
            (p - (p**2 + q**3) **0.5) **(1/3)
            + (p + (p**2 + q**3) **0.5) **(1/3)
            - b/(3*a)
            )
        print(val)
        return val

eg = Cubic(1, -6, 11, -6)            
print(eg.cube())


#For example
eg = Quadratic(3, 13, 12)
print(eg.formula, '  equals  ', eg.quad())
# -4/3 and -3