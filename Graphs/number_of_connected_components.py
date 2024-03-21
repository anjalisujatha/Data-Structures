from queue import Queue
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    
    adj_list = [[] for _ in range(n)]
    for (a,b) in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    visited = [-1]*n
    components = 0
    
    def bfs(source):
        q = Queue()
        q.put(source)
        visited[source] = 1
        while not q.empty():
            node = q.get()
            for neighbor in adj_list[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    q.put(neighbor)
                    
    for i in range(n):
        if visited[i] == -1:
            components += 1
            bfs(i)
            
    return components
            