class Function:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print("Twoja funkcja to: {0}x^3 + {1}x^2 + {2}x + {3}".format(a, b, c, d))

    def calculate(self, x):
        return self.a * x ** 3 + self.b * x ** 2 + self.c * x + self.d