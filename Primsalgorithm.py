import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    mst = []
    start_vertex = 0
    
    # Initialize priority queue with edges from the start vertex
    pq = [(0, start_vertex)]
    
    while pq:
        weight, vertex = heapq.heappop(pq)
        
        if visited[vertex]:
            continue
        
        visited[vertex] = True
        if len(mst) > 0:
            mst.append((prev_vertex, vertex, weight))
        else:
            mst.append((vertex, vertex, weight))
        
        for neighbor, edge_weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor))
        
        prev_vertex = vertex
    
    return mst[1:]  # Remove the dummy edge added at the start

# Example usage:
# Graph represented as adjacency list: {vertex: [(neighbor, weight), ...]}
graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (7, 11), (2, 8)],
    2: [(1, 8), (8, 2), (3, 7), (5, 4)],
    3: [(2, 7), (5, 14), (4, 9)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}

# Find minimum spanning tree using Prim's algorithm
mst = prim(graph)

# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
