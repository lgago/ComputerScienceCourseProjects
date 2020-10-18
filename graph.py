'''CS 2420 Project 8, Luis Gago, this code was completed without help from other students'''
import numpy as np

class Graph():
    '''Graph class is used to generate graphs'''
    def __init__(self, max_vertices=10):
        '''Initialize a new graph with the given parameters'''
        self.matrix = np.full((max_vertices, max_vertices), float('Inf'))
        self.num_vertices = 0
        self.vertex_to_index = {}

    def add_vertex(self, label):
        '''add a vertex to the graph'''
        if not isinstance(label, str):
            raise ValueError("label must be a string")
        if self.num_vertices == self.matrix.shape[0]:
            raise ValueError("graph is full")

        if label not in self.vertex_to_index:
            self.vertex_to_index[label] = self.num_vertices
            self.num_vertices += 1

        return self

    def add_edge(self, src, dest, weight):
        '''add an edge to the graph'''
        if src not in self.vertex_to_index or dest not in self.vertex_to_index:
            raise ValueError("src and dest must be inside the vertex dictionary")
        if not isinstance(weight, (float, int)):
            raise ValueError("weight must be a float or an integer")
        if weight <= 0:
            raise ValueError("Weight must be a positive non-zero number")
        self.matrix[self.vertex_to_index[src]][self.vertex_to_index[dest]] = weight
        return self

    def get_weight(self, src, dest):
        '''return the weight between two vertices'''
        if src not in self.vertex_to_index or dest not in self.vertex_to_index:
            raise ValueError("src and dest must be inside the vertex dictionary")
        return self.matrix[self.vertex_to_index[src]][self.vertex_to_index[dest]]

    def dfs(self, starting_vertex):
        '''conduct a depth first search'''
        if starting_vertex not in self.vertex_to_index:
            raise ValueError("starting_vertext must be in the graph")
        stack = [starting_vertex]
        discovered_set = set()

        while len(stack) != 0:
            current_v = stack.pop()
            if current_v not in discovered_set:
                yield current_v
                discovered_set.add(current_v)
                for adj_v in self.vertex_to_index:
                    if self.get_weight(current_v, adj_v) != float('Inf') and adj_v not in discovered_set:
                        stack.append(adj_v)

    def bfs(self, starting_vertex):
        '''conduct a breadth first search'''
        if starting_vertex not in self.vertex_to_index:
            raise ValueError("starting_vertext must be in the graph")
        frontier_queue = [starting_vertex]
        discovered_set = set(starting_vertex)
        while len(frontier_queue) != 0:
            current_v = frontier_queue.pop(0)
            yield current_v
            for adj_v in self.vertex_to_index:
                if self.get_weight(current_v, adj_v) != float('Inf') and adj_v not in discovered_set:
                    frontier_queue.append(adj_v)
                    discovered_set.add(adj_v)

    def dijkstra_shortest_path(self, src, dest=None):
        '''calculate dijkstra's shortest path between two points'''
        if src not in self.vertex_to_index:
            raise ValueError("src must be inside the vertex dictionary")
        path_dict = self.dijkstra_shortest_path_helper(src)
        if dest == None:
            return path_dict
        else:
            return path_dict[dest]

    def dijkstra_shortest_path_helper(self, src):
        '''calculate dijkstra's shortest path for all possibilities'''
        visited = []
        unvisited = []
        final_dict = {}

        for vertices in self.vertex_to_index:
            #Add vertice to the end of the unvisited set
            unvisited.append(vertices)
            #add values to the final dictionary
            if vertices == src:
                final_dict[src] = (0.0, [src])
            else:
                final_dict[vertices] = (float('Inf'), [vertices])
        while len(unvisited) > 0:
            temp_value = float('Inf')
            current_vertex = None
            for key, value in final_dict.items():
                # print(key, value)
                if value[0] < temp_value and key not in visited:
                    temp_value = value[0]
                    current_vertex = key
            for item in unvisited:
                try:
                    if self.get_weight(current_vertex, item) != float('Inf'):
                        if (self.get_weight(current_vertex, item) + final_dict[current_vertex][0]) < final_dict[item][0]:
                            final_dict[item] = ((self.get_weight(current_vertex, item) + final_dict[current_vertex][0]), [final_dict[item][1][0]] + final_dict[current_vertex][1])
                except:
                    final_dict[item] = (float('Inf'), [])

            if current_vertex == None:
                return final_dict
                    
            visited.append(current_vertex)
            unvisited.remove(current_vertex)
        return final_dict

    def __str__(self):
        '''return a string of the graph'''
        return "numVertices: " + str(self.num_vertices) + "\n" + str(self.matrix)


def main():
    '''main function'''
    graph = Graph(6)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_edge('A', 'B', 2.0)
    graph.add_edge('A', 'F', 9.0)
    graph.add_edge('B', 'F', 6.0)
    graph.add_edge('B', 'D', 15.0)
    graph.add_edge('B', 'C', 8.0)
    graph.add_edge('C', 'D', 1.0)
    graph.add_edge('E', 'D', 3.0)
    graph.add_edge('E', 'C', 7.0)
    graph.add_edge('F', 'E', 3.0)
 
    # print(graph.dijkstra_shortest_path('A', 'B'))
    print(graph.dijkstra_shortest_path("D",'A'))

if __name__ == "__main__":
    main()
