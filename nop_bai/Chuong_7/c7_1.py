
#nguyen chương 7, chưa check
import networkx as nx

class MyGraph:
    def __init__(self, directed=False):
        if directed:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()

    def LienThong(self):
        # Đối với đồ thị vô hướng
        if type(self.graph) == nx.Graph:
            return nx.is_connected(self.graph)
        # Đối với đồ thị hữu hướng
        else:
            return nx.is_strongly_connected(self.graph)

    def SoThanhPhan(self):
        # Đối với đồ thị vô hướng
        if type(self.graph) == nx.Graph:
            return nx.number_connected_components(self.graph)
        # Đối với đồ thị hữu hướng
        else:
            return nx.number_strongly_connected_components(self.graph)

    def ChuTrinh(self):
        return any(nx.simple_cycles(self.graph))

    def ChuaDinh(self, v):
        return v in self.graph.nodes

    def BacDinh(self, v):
        # Chỉ hoạt động với đồ thị vô hướng
        assert type(self.graph) == nx.Graph, "This method only supports undirected graphs."
        return self.graph.degree[v]

    def SoCungVao(self, v):
        # Chỉ hoạt động với đồ thị hữu hướng
        assert type(self.graph) == nx.DiGraph, "This method only supports directed graphs."
        return self.graph.in_degree[v]

    def SoCungRa(self, v):
        # Chỉ hoạt động với đồ thị hữu hướng
        assert type(self.graph) == nx.DiGraph, "This method only supports directed graphs."
        return self.graph.out_degree[v]

    def DuongDi(self, v1, v2):
        return nx.has_path(self.graph, v1, v2)

# Thử nghiệm một vài phương thức
dt = MyGraph(directed=True)  # Tạo đồ thị hữu hướng
dt.graph.add_edge('A', 'B')
dt.graph.add_edge('B', 'C')
dt.graph.add_edge('C', 'A')

print(dt.LienThong())  # True
print(dt.SoThanhPhan())  # 1
print(dt.ChuTrinh())  # True
print(dt.ChuaDinh('A'))  # True
print(dt.SoCungVao('A'))  # 1
print(dt.SoCungRa('A'))  # 1
print(dt.DuongDi('A', 'C'))  # True
