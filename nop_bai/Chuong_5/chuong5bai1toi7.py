class Node:
  def __init__(self, data):
      self.info = data
      self.left = None
      self.right = None

class Cay:
  def __init__(self):
      self.root = None

  def SoNut(self, node):
      if node is None:
          return 0
      else:
          return 1 + self.SoNut(node.left) + self.SoNut(node.right)

  def SoNutCay(self):
      return self.SoNut(self.root)

  def ChieuCao(self, node):
      if node is None:
          return -1
      else:
          left_height = self.ChieuCao(node.left)
          right_height = self.ChieuCao(node.right)
          return 1 + max(left_height, right_height)

  def ChieuCaoCay(self):
      return self.ChieuCao(self.root)


# Example usage:
# Tạo cây
tree = Cay()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Tính số nút của cây
print("Số nút của cây:", tree.SoNutCay())

# Tính chiều cao của cây
print("Chiều cao của cây:", tree.ChieuCaoCay())
