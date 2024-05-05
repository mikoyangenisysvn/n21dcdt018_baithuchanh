class Matrix:
    def __init__(self, size):
        self.size = size
        self.data = [[0 for _ in range(size)] for _ in range(size)]

    def input_matrix(self):
        print("Nhập ma trận vuông kích thước", self.size, "x", self.size)
        for i in range(self.size):
            row = input(f"Nhập hàng thứ {i + 1} (các giá trị cách nhau bằng dấu cách): ")
            values = row.split()
            if len(values) != self.size:
                print("Lỗi: Vui lòng nhập đúng số lượng giá trị cho mỗi hàng.")
                return False
            try:
                self.data[i] = [int(val) for val in values]
            except ValueError:
                print("Lỗi: Vui lòng chỉ nhập các giá trị số nguyên.")
                return False
        return True

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

    def print_duplicate_column_groups(self):
        groups = []
        visited = set()
        for i in range(self.size - 1):
            if i not in visited:
                group = [i]
                for j in range(i + 1, self.size):
                    if all(self.data[x][i] == self.data[x][j] for x in range(self.size)):
                        group.append(j)
                        visited.add(j)
                if len(group) > 1:
                    groups.append(group)

        if not groups:
            print("Không có nhóm cột giống nhau.")
            return

        for group in groups:
            print("Nhóm cột giống nhau:", group)

# Ví dụ sử dụng:
size = int(input("Nhập kích thước ma trận vuông: "))
m = Matrix(size)

while not m.input_matrix():
    pass  # Lặp lại yêu cầu nhập ma trận nếu có lỗi nhập

print("Ma trận vừa nhập:")
for row in m.data:
    print(row)

print("Là ma trận tam giác dưới:", m.is_lower_triangular())
print("Có ít nhất hai cột giống nhau:", m.has_duplicate_columns())

m.print_duplicate_column_groups()
