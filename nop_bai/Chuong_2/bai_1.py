class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def get_value(self, row, col):
        return self.data[row][col]

    def display(self):
        for row in self.data:
            print(row)

    def nhap_ma_tran_vuong(self):
        print("Nhập các phần tử của ma trận vuông:")
        for i in range(self.rows):
            for j in range(self.cols):
                value = float(input("Nhập phần tử ở hàng {} cột {}: ".format(i + 1, j + 1)))
                self.set_value(i, j, value)

    def la_ma_tran_doi_xung(self):
        if self.rows != self.cols:
            return False

        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True
    
    def la_ma_tran_tam_giac_tren(self):
        for i in range(1, self.rows):
            for j in range(i):
                if self.data[i][j] != 0:
                    return False
        return True
    def co_hai_hang_giong_nhau(self):
        for i in range(self.rows - 1):
            for j in range(i + 1, self.rows):
                if self.data[i] == self.data[j]:
                    return True
        return False

# Tạo một đối tượng Matrix
mang = Matrix(3, 3)

# Nhập ma trận vuông từ người dùng
mang.nhap_ma_tran_vuong()

# Hiển thị ma trận vừa nhập
print("Ma trận vừa nhập:")
mang.display()

# Kiểm tra xem ma trận có phải ma trận đối xứng hay không
if mang.la_ma_tran_doi_xung():
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")

# Kiểm tra xem ma trận có phải ma trận tam giác trên hay không
if mang.la_ma_tran_tam_giac_tren():
    print("Ma trận là ma trận tam giác trên.")
else:
    print("Ma trận không phải là ma trận tam giác trên.")

# Kiểm tra xem ma trận có ít nhất hai hàng giống nhau hay không
if mang.co_hai_hang_giong_nhau():
    print("Ma trận có ít nhất hai hàng giống nhau.")
else:
    print("Ma trận không có ít nhất hai hàng giống nhau.")
