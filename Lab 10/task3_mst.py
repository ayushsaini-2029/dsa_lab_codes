def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    mst = []
    total = 0
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total


def prim(n, graph, start=0):
    INF = 10**9
    key = [INF] * n
    parent = [-1] * n
    vis = [False] * n
    key[start] = 0
    total = 0

    for _ in range(n):
        u = min((i for i in range(n) if not vis[i]), key=lambda x: key[x])
        vis[u] = True
        total += key[u]
        for v, w in graph[u]:
            if not vis[v] and w < key[v]:
                key[v] = w
                parent[v] = u
    return total, parent


edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 5)]
print("Kruskal:", kruskal(4, edges))

graph = [[(1, 4), (2, 3)], [(0, 4), (2, 1), (3, 2)], [(0, 3), (1, 1), (3, 5)], [(1, 2), (2, 5)]]
print("Prim:", prim(4, graph))
