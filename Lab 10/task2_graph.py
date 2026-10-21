from collections import deque


def adj_matrix(n, edges):
    m = [[0] * n for _ in range(n)]
    for u, v in edges:
        m[u][v] = 1
        m[v][u] = 1
    return m


def adj_list(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g


def dfs(g, s):
    vis = [False] * len(g)
    res = []
    step = 0

    def go(u):
        nonlocal step
        vis[u] = True
        step += 1
        res.append((u, step))
        for v in g[u]:
            if not vis[v]:
                go(v)

    go(s)
    return res


def bfs(g, s):
    vis = [False] * len(g)
    q = deque([s])
    vis[s] = True
    res = []
    step = 0

    while q:
        u = q.popleft()
        step += 1
        res.append((u, step))
        for v in g[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)
    return res


edges = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4)]
g = adj_list(5, edges)
print("DFS:", dfs(g, 0))
print("BFS:", bfs(g, 0))
