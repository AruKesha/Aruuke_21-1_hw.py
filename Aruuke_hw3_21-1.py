class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __add__(self, other):
        numerator = self.numerator * other.denumerator + self.denumerator * other.numerator
        denumerator = self.denumerator * other.denumerator
        return f'{numerator}/{denumerator}'

    def __sub__(self, other):
        numerator = self.numerator * other.denumerator - self.denumerator * other.numerator
        denumerator = self.denumerator * other.denumerator
        return f'{numerator}/{denumerator}'

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denumerator = self.denumerator * other.denumerator
        return f'{numerator}/{denumerator}'
        
    def __floordiv__(self, other):
        numerator = self.numerator * other.denumerator
        denumerator = self.denumerator * other.numerator
        return f'{numerator}/{denumerator}'


frac1 = Fraction(numerator=1, denumerator=2)
frac2 = Fraction(denumerator=3, numerator=1)
print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 // frac2)
print(frac1 * frac2)

