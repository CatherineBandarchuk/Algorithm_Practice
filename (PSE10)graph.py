graph1 = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": ["E"],
    "E": ["D"],
    "F": []
}

graph2 = {}

graph3 = {
    "A": ["A","B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": ["E"],
    "E": ["D"],
    "F": []
}

def dfs_recursive(graph, node, visited):
    visited.append(node)

    for n in graph[node]:
        if n not in visited:
            dfs_recursive(graph, n, visited)
            

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        element = stack.pop(0)

        for n in graph[element]:
            if n not in visited:
                visited.append(n)
                stack.append(n)
    
    return visited

def component(graph):
    subgraph_list = []
    if len(graph)==0:
        return [subgraph_list]
    if not isinstance(graph, dict) or \
    not all(isinstance(value, list) for value in graph.values()):
        return -1
    
    visited_keys = []
    list_of_keys = graph.keys()

    for key in list_of_keys:
        if key not in visited_keys:
            subgraph = dfs(graph,key)
            visited_keys+= subgraph
            subgraph_list.append(subgraph)
    
    return subgraph_list

print(component(graph3))






