import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imag = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imag)

    def __truediv__(self, no):
        denom = no.real**2 + no.imaginary**2
        real = (self.real * no.real + self.imaginary * no.imaginary) / denom
        imag = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(real, imag)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            return "%.2f+0.00i" % self.real
        elif self.real == 0:
            return "0.00%.2fi" % self.imaginary if self.imaginary >= 0 else "0.00-%.2fi" % abs(self.imaginary)
        elif self.imaginary > 0:
            return "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            return "%.2f-%.2fi" % (self.real, abs(self.imaginary))

if __name__ == '__main__':
    c = list(map(float, input().split()))
    d = list(map(float, input().split()))
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
