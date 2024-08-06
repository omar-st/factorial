class Quantity:
    def __init__(self, coefficient, exponent):
        self.formula = f'{coefficient}x^{exponent}'
        self.a = coefficient
        self.n = exponent
    #pass the number for how many derivatives to take. 1st, 2nd, 3rd, etc
    def dx(self, count):
        a, n = self.a, self.n
        for i in range(count):
            a *= n
            n -= 1
        return (a, n)
    #pass the number for how many integrals to take. 1st, 2nd, 3rd, etc
    def ix(self, count):
        a, n = self.a, self.n
        for i in range(count):
            n += 1
            a /= n
        return (a, n)

q = Quantity(4, 3)  #ie, the term 4x^3
#derivative example: 2nd derivative of 4x^3
print(q.dx(2))  #24x
#integral example: 1st integral of 4x^3
print(q.ix(1))  #x^4