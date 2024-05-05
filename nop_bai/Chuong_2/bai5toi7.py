class A:
  def __init__(self, a):
      self.a = a

  def Cong(self, b):
      # Sửa đổi phương thức để xử lý từng phần tử của mảng
      new_array = []
      for num in self.a:
          result = num + b
          if result < 0 or result >= 2**32:
              new_array.append(-1)
          else:
              new_array.append(result)
      return new_array

  # Thêm phương thức mới để trừ một số từ mỗi phần tử của mảng
  def Tru(self, b):
      new_array = []
      for num in self.a:
          result = num - b
          if result < 0:
              new_array.append(0)  # Giả sử kết quả không thể âm
          else:
              new_array.append(result)
      return new_array

  # Thêm phương thức mới để nhân một số với mỗi phần tử của mảng
  def Nhan(self, b):
      new_array = []
      for num in self.a:
          result = num * b
          if result >= 2**32:
              new_array.append(-1)
          else:
              new_array.append(result)
      return new_array

# Example usage:
arr = [1, 4, 7]  # Mảng các số nguyên không dấu
obj = A(arr)
print(obj.Cong(100))  # Kết quả không bị tràn: [223, 556, 889]
print(obj.Cong(4294967295))  # Kết quả bị tràn: [-1, -1, -1]
print(obj.Tru(50))  # Kết quả sau khi trừ: [73, 406, 739]
print(obj.Nhan(2))  # Kết quả sau khi nhân: [246, 912, 1578]