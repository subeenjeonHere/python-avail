def dfs(g, st, visit=None):
    if visit is None:
        visit = set()
    visit.add(st)
    print(st, end=' ')

    for neighbor in g[st]:
        if neighbor not in visit:
            dfs(g, neighbor, visit)

# 그래프 예시 (인접 리스트 형태)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print()
dfs(graph, 'A')
