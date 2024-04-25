import matplotlib.pyplot as plt
import numpy as np

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

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def min_cost_connect_points(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((manhattan_distance(points[i], points[j]), i, j))
    
    edges.sort()
    uf = UnionFind(n)
    min_cost = 0
    
    for edge in edges:
        cost, u, v = edge
        if uf.union(u, v):
            min_cost += cost
    
    return min_cost

def plot_points_and_tree(points, mst_edges):
    plt.figure(figsize=(8, 6))
    for i, (x, y) in enumerate(points):
        plt.scatter(x, y, color='blue', zorder=5)
        plt.text(x, y, f'{i}', fontsize=12, ha='center', va='bottom', color='black', zorder=10)
    
    for edge in mst_edges:
        p1, p2 = edge
        plt.plot([points[p1][0], points[p2][0]], [points[p1][1], points[p2][1]], color='red', zorder=1)
    
    plt.title('Minimum Spanning Tree')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Example usage:
points = [[0,0], [2,2], [3,10], [5,2], [7,0]]
min_cost = min_cost_connect_points(points)
print("Minimum cost to connect all points:", min_cost)

# Find MST edges
mst_edges = []
n = len(points)
for i in range(n):
    for j in range(i + 1, n):
        mst_edges.append((i, j))
mst_edges = [mst_edge for mst_edge in mst_edges if manhattan_distance(points[mst_edge[0]], points[mst_edge[1]]) == min_cost]
plot_points_and_tree(points, mst_edges)
