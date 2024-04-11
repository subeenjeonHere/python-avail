class Calc:
    def setter(self, op1, op2):
        self.first = op1
        self.second = op2

    def mul(self):
        result = self.first * self.second
        return result

a = Calc()
a.setter(4, 2)
print(a.mul())
