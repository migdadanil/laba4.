from collections import deque
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex].append(to_vertex)

    def depth_first_search(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex)
        for neighbor in self.adjacency_list[start_vertex]:
            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)

    def breadth_first_search(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

graph = Graph()
for vertex in ['A', 'B', 'C', 'D']:
    graph.add_vertex(vertex)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.depth_first_search('A')
graph.breadth_first_search('A')