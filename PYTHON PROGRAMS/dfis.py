graph = {
  'A': ['B', 'C'],
  'B': ['A','D','E'],
  'C': ['A','F','G'],
  'D': [],
  'E': [],
  'F': ['H','I'],
  'G': [],
  'H': [],
  'I': []
}



def dfid(graph,current_node,goal_node,visited,path,depth):
    for i in range(0,depth):
        print(f"Depth : {i}")
        dfs(graph,current_node,goal_node,[],[],0,i)

def dfs(graph,current_node,goal_node,visited,path,current_depth,depth):
    if current_depth<=depth:
        if current_node not in visited:
            visited.append(current_node)
            path.append(current_node)
            not_visited=[i for i in graph.keys() if i not in visited]
            if current_node==goal_node:
                print(f"{visited}\t\t{not_visited}\t\tTrue")
                print('path found',path)
                exit()
            print(f"{visited}\t\t{not_visited}\t\tFalse")
            for i in graph[current_node]:
                dfs(graph,i,goal_node,visited,path,current_depth+1,depth)
    
dfid(graph,'A','F',[],[],3) 




# if status:
#     print(f"Found\nPath : {path1}")
# else:
#     print(f"Not found")