class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def DoiXung(self):
        # Kiểm tra xem ma trận có số hàng và số cột bằng nhau không
        n = len(self.arr)
        if n != len(self.arr[0]):
            return False

        # Kiểm tra từng cặp phần tử đối xứng qua đường chéo chính
        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i][j] != self.arr[j][i]:
                    return False
        return True

# Sử dụng
matrix1 = Matrix([[1, 2, 3],
                  [2, 4, 5],
                  [3, 5, 6]])

matrix2 = Matrix([[1, 2, 3],
                  [2, 4, 5],
                  [3, 6, 7]])

print(matrix1.DoiXung())  # Output: True (vì ma trận 1 là ma trận đối xứng)
print(matrix2.DoiXung())  # Output: False (vì ma trận 2 không phải là ma trận đối xứng)
