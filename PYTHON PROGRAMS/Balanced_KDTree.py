class Node:
    def __init__(self,point,axis):
        self.axis=axis
        self.point=point
        self.left=None
        self.right=None
        
  
def build_kdtree(points, depth=0):
    if not points:
        return None
    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    node = Node(points[median], axis)
    if len(points) > 1:  # Added condition to handle empty list
        node.left = build_kdtree(points[:median], depth + 1)
        node.right = build_kdtree(points[median + 1:], depth + 1)
    return node
    

def print_kdtree(node, level=0, side=None):
    if node is not None:
        prefix = ""
        if side is not None:
            prefix = side + "---"
        print("    " * level + prefix + str(node.point))
        print_kdtree(node.left, level + 1, "L")  # Corrected the side parameter
        print_kdtree(node.right, level + 1, "R")  # Corrected the side parameter



points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
root=build_kdtree(points)
print_kdtree(root)  