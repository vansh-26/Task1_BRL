class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    def get_real(self):
        return self.real
    def set_real(self, real):
        self.real = real
    def get_imag(self):
        return self.imag
    def set_imag(self, imag):
        self.imag = imag
    def add(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)
    def subtract(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return Complex(real_diff, imag_diff)
    def multiply(self, other):
        real_product = self.real * other.real - self.imag * other.imag
        imag_product = self.real * other.imag + self.imag * other.real
        return Complex(real_product, imag_product)
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

c1 = Complex(3, 4)
c2 = Complex(1, -2)

print("Complex Number 1:", c1)
print("Complex Number 2:", c2)
result_add = c1.add(c2)
print("Addition Result:", result_add)
result_subtract = c1.subtract(c2)
print("Subtraction Result:", result_subtract)
result_multiply = c1.multiply(c2)
print("Multiplication Result:", result_multiply)