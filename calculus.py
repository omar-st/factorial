#Calculus

class Quantity:
    def __init__(self, coefficient=1, exponent=1):
        self.formula = f'{coefficient}x^{exponent}'
        self.a = coefficient
        self.n = exponent
    #pass the number for how many derivatives to take. 1st, 2nd, 3rd, etc
    def dx(self, count=1):
        a, n = self.a, self.n
        for i in range(count):
            a *= n
            n -= 1
        return (a, n)
    #pass the number for how many integrals to take. 1st, 2nd, 3rd, etc
    def ix(self, count=1):
        a, n = self.a, self.n
        for i in range(count):
            n += 1
            a /= n
        return (a, n)

    def TaylorProgression(self, lim=10):
        a, n = self.a, self.n
        progression = [(a,n)]
        for i in range(lim):
            n += 1
            a /= n
            progression.append((a, n))
        return(progression)


class Angle():
    def __init__(self, r): #r = angle size in radians
        self.r = r
        self.taylor = Quantity()
        self.t = self.taylor.TaylorProgression()

    #Uses the Taylor series of sine and cosine to compute the sin/cos values of any angle stated in radians. (To a depth of 10 integrals)
    def sin(self):
        r, t = self.r, self.t
        sine = 0  #sin starts at 0, then alternates +/- every odd power
        for i in range(5):
            poly = t[2*i]  #array starts at zero, so power 1 is at index 0
            #print(poly)
            if i%2 == 0:
                sine += poly[0]*(r**poly[1])
            else:
                sine -= poly[0]*(r**poly[1])
            #print(sine)
        return sine

    def cos(self):
        r, t = self.r, self.t
        cosine = 1  #cos starts at, then alternates -/+ every even power
        for i in range(5):
            poly = t[2*i+1]  #array starts at zero, so power 2 is at index 1
            #print(poly)
            if i%2 == 0:
                cosine -= poly[0]*(r**poly[1])
            else:
                cosine += poly[0]*(r**poly[1])
        return cosine


q = Quantity(4, 3)  #ie, the term 4x^3
#derivative example: 2nd derivative of 4x^3
print(q.dx(2))  #24x
#integral example: 1st integral of 4x^3
print(q.ix(1))  #x^4

theta = Angle(1.25)
print(theta.sin())  #sin of 1.25 radians
print(theta.cos())  #cos of 1.25 radians