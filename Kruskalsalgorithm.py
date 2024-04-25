class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal(graph):
    # Sort edges by weight
    edges = sorted(graph, key=lambda x: x[2])
    
    # Initialize Union-Find data structure
    n = len(set().union(*[(edge[0], edge[1]) for edge in edges]))
    uf = UnionFind(n)
    
    mst = []
    for edge in edges:
        u, v, weight = edge
        if uf.union(u, v):
            mst.append(edge)
    
    return mst

# Example usage:
# Graph represented as list of tuples (u, v, weight)
graph = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7),
         (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10),
         (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]

# Find minimum spanning tree using Kruskal's algorithm
mst = kruskal(graph)

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
