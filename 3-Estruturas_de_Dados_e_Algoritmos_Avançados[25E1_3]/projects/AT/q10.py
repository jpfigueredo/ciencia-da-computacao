class UnionFind:  
    def __init__(self, size):  
        self.parent = list(range(size))  
      
    def find(self, x):  
        if self.parent[x] != x:  
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]  
      
    def union(self, x, y):  
        root_x = self.find(x)  
        root_y = self.find(y)  
        if root_x != root_y:  
            self.parent[root_y] = root_x  

def kruskal(graph):  
    edges = sorted(graph['edges'], key=lambda x: x[2])  # Ordena arestas por peso  
    node_map = {node: idx for idx, node in enumerate(graph['nodes'])}  
    uf = UnionFind(len(graph['nodes']))  
    mst = []  
    total_cost = 0  

    for u, v, weight in edges:  
        u_idx = node_map[u]  
        v_idx = node_map[v]  
        if uf.find(u_idx) != uf.find(v_idx):  
            uf.union(u_idx, v_idx)  
            mst.append((u, v, weight))  
            total_cost += weight  
            if len(mst) == len(graph['nodes']) - 1:  
                break  # MST completa  

    return mst, total_cost  


import heapq  

def prim(graph):  
    nodes = graph['nodes']  
    adj_list = {node: [] for node in nodes}  
    for u, v, w in graph['edges']:  
        adj_list[u].append((w, v))  
        adj_list[v].append((w, u))  

    start_node = nodes[0]  
    visited = set([start_node])  
    heap = []  
    for weight, neighbor in adj_list[start_node]:  
        heapq.heappush(heap, (weight, start_node, neighbor))  

    mst = []  
    total_cost = 0  

    while heap and len(visited) < len(nodes):  
        weight, u, v = heapq.heappop(heap)  
        if v not in visited:  
            visited.add(v)  
            mst.append((u, v, weight))  
            total_cost += weight  
            for next_weight, neighbor in adj_list[v]:  
                if neighbor not in visited:  
                    heapq.heappush(heap, (next_weight, v, neighbor))  

    return mst, total_cost  

graph = {  
    'nodes': ['A', 'B', 'C', 'D'],  
    'edges': [  
        ('A', 'B', 1), ('A', 'C', 2),  
        ('B', 'C', 3), ('B', 'D', 4),  
        ('C', 'D', 5)  
    ]  
}  

mst_kruskal, custo_kruskal = kruskal(graph)  
print("Kruskal - MST:", mst_kruskal, "Custo:", custo_kruskal)  

mst_prim, custo_prim = prim(graph)  
print("Prim - MST:", mst_prim, "Custo:", custo_prim)  