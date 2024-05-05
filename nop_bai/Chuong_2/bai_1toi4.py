class Matrix:
    def __init__(self, size):
        self.size = size
        self.data = [[0 for _ in range(size)] for _ in range(size)]

    def input_matrix(self):
        print("Nhập ma trận vuông kích thước", self.size, "x", self.size)
        for i in range(self.size):
            for j in range(self.size):
                self.data[i][j] = int(input(f"Nhập phần tử [{i}][{j}]: "))

    def is_lower_triangular(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.data[i][j] != 0:
                    return False
        return True

    def has_duplicate_columns(self):
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                if all(self.data[x][i] == self.data[x][j] for x in range(self.size)):
                    return True
        return False

# Ví dụ sử dụng:
size = int(input("Nhập kích thước ma trận vuông: "))
m = Matrix(size)
m.input_matrix()
print("Ma trận vừa nhập:")
for row in m.data:
    print(row)

print("Là ma trận tam giác dưới:", m.is_lower_triangular())
print("Có ít nhất hai cột giống nhau:", m.has_duplicate_columns())
