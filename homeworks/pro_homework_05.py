import math

class CorrectFraction:
    def __init__(self, top_num, bottom_num):
        if bottom_num == 0:
            raise ValueError("This fraction would be incorrect.")
        if top_num > bottom_num:
            raise ValueError("Top number can not be bigger than bottom number.")
        self.top_num = top_num
        self.bottom_num = bottom_num
        self.correction()

    def correction(self):
        gcd_shit = math.gcd(self.top_num, self.bottom_num)
        self.top_num //= gcd_shit
        self.bottom_num //= gcd_shit

    def __add__(self, other):
        if isinstance(other, CorrectFraction):
            new_top_num = self.top_num * other.bottom_num + self.bottom_num * other.top_num
            new_bottom_num = self.bottom_num * other.bottom_num
            return CorrectFraction(new_top_num, new_bottom_num)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, CorrectFraction):
            self.top_num = self.top_num * other.bottom_num + self.bottom_num * other.top_num
            self.bottom_num *= other.bottom_num
            self.correction()
            return self
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return CorrectFraction(self.top_num + other * self.bottom_num, self.bottom_num)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, CorrectFraction):
            new_top_num = self.top_num * other.bottom_num - other.top_num * self.bottom_num
            new_bottom_num = self.bottom_num * other.bottom_num
            return CorrectFraction(new_top_num, new_bottom_num)
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, CorrectFraction):
            self.top_num = self.top_num * other.bottom_num - other.top_num * self.bottom_num
            self.bottom_num *= other.bottom_num
            self.correction()
            return self
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return CorrectFraction(other * self.bottom_num - self.top_num, self.bottom_num)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, CorrectFraction):
            new_top_num = self.top_num * other.top_num
            new_bottom_num = self.bottom_num * other.bottom_num
            return CorrectFraction(new_top_num, new_bottom_num)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, CorrectFraction):
            self.top_num *= other.top_num
            self.bottom_num *= other.bottom_num
            self.correction()
            return self
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return CorrectFraction(self.top_num * other, self.bottom_num)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, CorrectFraction):
            new_top_num = self.top_num * other.bottom_num
            new_bottom_num = self.bottom_num * other.top_num
            return CorrectFraction(new_top_num, new_bottom_num)
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, CorrectFraction):
            self.top_num *= other.bottom_num
            self.bottom_num *= other.top_num
            self.correction()
            return self
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return CorrectFraction(other * self.bottom_num, self.top_num)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, CorrectFraction):
            return self.top_num == other.top_num and self.bottom_num == other.bottom_num
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, CorrectFraction):
            return not (self == other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, CorrectFraction):
            return self.top_num * other.bottom_num < other.top_num * self.bottom_num
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, CorrectFraction):
            return self.top_num * other.bottom_num <= other.top_num * self.bottom_num
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, CorrectFraction):
            return self.top_num * other.bottom_num > other.top_num * self.bottom_num
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, CorrectFraction):
            return self.top_num * other.bottom_num >= other.top_num * self.bottom_num
        return NotImplemented
    
    def __str__(self):
        return f"{self.top_num}/{self.bottom_num}"
    
#a = CorrectFraction(4, 8)
#b = CorrectFraction(2, 4)
#a /= b
#c = a + b
#print(a > b)
