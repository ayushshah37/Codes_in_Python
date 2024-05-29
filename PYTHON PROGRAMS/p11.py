def bfs(graph,src,gola,visited):
    visited.append(src)
    queue.append(src)
    non_visited=[]
    for i in graph.keys():
        if i not in visited:
            non_visited.append(i)
        print(f"{visited}\t {non-visited}\t\t FALSE")

    while queue:
        m=qeueu.pop(0)
        for i in graph(m):
            if i not in visited:
                visited.append(i)
                queue.append(i)
                not_visited=[]
                






graph = {
  'A': ['B','C'],
  'B': ['A','D','E'],
  'C': ['A','F','G'],
  'D': [],
  'E': [],
  'F': ['H','I'],
  'G': [],
  'H': [],
  'I': []
}

queue=[]
src=input("enter source node : ")
goal=input("enter goal node : ")


bfs(graph,src,goal,visited=[])