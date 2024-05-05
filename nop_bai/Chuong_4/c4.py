#c4, full
class Node:
  def __init__(self, info):
      self.info = info
      self.next = None

class DSLK:
  def __init__(self):
      self.head = None

  def Them(self, info):
      new_node = Node(info)
      if self.head is None:
          self.head = new_node
      else:
          current = self.head
          while current.next:
              current = current.next
          current.next = new_node

  def InNguoc_DeQui(self, node):
      if node:
          self.InNguoc_DeQui(node.next)
          print(node.info, end=" ")

  def InNguoc_KhongDeQui(self):
      stack = []
      current = self.head
      while current:
          stack.append(current.info)
          current = current.next
      while stack:
          print(stack.pop(), end=" ")

  def DaoNguoc(self):
      stack = []
      current = self.head
      while current:
          stack.append(current)
          current = current.next
      self.head = stack.pop()
      current = self.head
      while stack:
          current.next = stack.pop()
          current = current.next
      current.next = None

  def In(self):
      current = self.head
      while current:
          print(current.info, end=" ")
          current = current.next
      print()


# Example usage:
if __name__ == "__main__":
  dslk = DSLK()
  dslk.Them(1)
  dslk.Them(2)
  dslk.Them(3)
  dslk.Them(4)
  dslk.Them(5)

  print("Danh sách liên kết:")
  dslk.In()

  print("In ngược (dùng đệ qui):")
  dslk.InNguoc_DeQui(dslk.head)
  print()

  print("In ngược (không dùng đệ qui):")
  dslk.InNguoc_KhongDeQui()
  print()

  print("Đảo ngược danh sách liên kết:")
  dslk.DaoNguoc()
  dslk.In()