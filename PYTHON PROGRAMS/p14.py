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



def dfs(graph,current_node,goal_node,visited):
    if current_node not in visited:
        visited.append(current_node)
        non_visited=[]
        for i in graph.keys():
            if i not in visited:
                non_visited.append(i)

        if (current_node==goal_node):
            print(f"{visited} \t {non_visited}  TRUE  ")
            exit()
        print(f"{visited} \t {non_visited}  FALSE  ")
        for i in graph[current_node]:
            dfs(graph,i,goal_node,visited)

start_node=input("enter start node : ")
goal_node=input(" enter goal node : ")

visited=[]

dfs(graph,start_node,goal_node,visited)
