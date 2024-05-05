class Node:
  def __init__(self, heso, somu):
      self.HeSo = heso
      self.SoMu = somu
      self.KeTiep = None

class DaThuc:
  def __init__(self):
      self.head = None

  def Them(self, heso, somu):
      new_node = Node(heso, somu)

      if self.head is None:
          self.head = new_node
      else:
          current = self.head
          while current.KeTiep is not None:
              current = current.KeTiep
          current.KeTiep = new_node

  def HienThi(self):
      current = self.head
      while current is not None:
          print(f"{current.HeSo}x^{current.SoMu}", end=" ")
          current = current.KeTiep
      print()

# Sử dụng
dathuc = DaThuc()
dathuc.Them(3, 2)
dathuc.Them(-5, 1)
dathuc.Them(2, 0)
dathuc.HienThi()