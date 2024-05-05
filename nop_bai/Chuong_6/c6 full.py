#c6 full
class ArrayOperations:
  @staticmethod
  def Duynhat(arr):
      unique_sorted = sorted(set(arr))
      return unique_sorted

  @staticmethod
  def Hieu(a, b):
      unique_a = set(a)
      unique_b = set(b)
      diff = sorted(unique_a - unique_b)
      return diff

  @staticmethod
  def Giao(a, b):
      unique_a = set(a)
      unique_b = set(b)
      intersect = sorted(unique_a.intersection(unique_b))
      return intersect

  @staticmethod
  def Hop(a, b):
      unique_a = set(a)
      unique_b = set(b)
      union = sorted(unique_a.union(unique_b))
      return union

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 5, 9, 7]
b = [9, 6, 2, 3, 8]
print("Mảng duy nhất từ a:", ArrayOperations.Duynhat(a))
print("Hiệu của a và b:", ArrayOperations.Hieu(a, b))
print("Giao của a và b:", ArrayOperations.Giao(a, b))
print("Hợp của a và b:", ArrayOperations.Hop(a, b))

