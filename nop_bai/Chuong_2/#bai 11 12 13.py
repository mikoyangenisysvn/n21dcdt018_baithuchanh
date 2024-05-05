#bai 11 12 13
class BigInt:
    def __init__(self, sign, digits):
        self.sign = sign
        self.digits = list(map(int, digits))

    def to_int(self):
        # Chuyển BigInt thành số nguyên Python
        num = int("".join(map(str, self.digits)))
        if self.sign == 1:
            num = -num
        return num

    def __add__(self, other):
        return BigInt.from_int(self.to_int() + other.to_int())

    def __sub__(self, other):
        return BigInt.from_int(self.to_int() - other.to_int())

    def __mul__(self, other):
        return BigInt.from_int(self.to_int() * other.to_int())

    @staticmethod
    def from_int(value):
        sign = 0 if value >= 0 else 1
        digits = list(map(int, str(abs(value))))
        return BigInt(sign, digits)

    def __repr__(self):
        return f"{'-' if self.sign == 1 else ''}{''.join(map(str, self.digits))}"

# Ví dụ sử dụng
a = BigInt(0, [1, 2, 3])
b = BigInt(1, [1, 2])
print(a + b)  # Cộng
print(a - b)  # Trừ
print(a * b)  # Nhân
