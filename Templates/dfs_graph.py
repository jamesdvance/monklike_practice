

def parse_graph(graph):
    """
    'Graph' here can be an adjacency list
    """
    seen = set([])
    def dfs(node):

        ans =0 
        # some logic
        for neighbor in graph[node]:
            # some logic
            if neighbor.val not in seen:
                ans+=dfs(neighbor)
                seen.add(neighbor.val)

        return ans
    
    return dfs()
            
            