# Khan's Algorithm for Topological Sort

## Common Use
Khan's algorithm is commonly used to solve topological sort. When we want to return an order of notes in a directed graph

## Degrees
* In-Degree: Number Of Directed Edges Point Towards A Node
* Out-Degree: Number of Directed Edges Point Away From Node

## Steps
1. Calculate the In-Degree For Every Node 
2. When You See A Node With A Zero In-Degree, Add the Node To The Queue
3. Open Loop While Q. Pop out first node. Iterate over nodes's neighbors, decreasing in-degree for each. Add any items with 0 in-degrees to queue
4. Mark nodes popped from q as completed
5. Continue until all nodes visited
6. Is there is a cycle, there will be no topological sort order

## Variations

### Check If Cycle Exists
1. If a cycle exists, will never be able to find in-degree of 0. Therefore, finding in-degree of all nodes and never finding in-degree of 0 is a way to check for a cycle in V+E Time
2. Also, if the queue is empty before all nodes reach an in-degree of 0, there must be a cycle also. 

## Complexity
V = number of verteces, or "nodes"
E = number of (directed) edges

### Time 
O(V * E ) - in worse case, we iterate over all connected edges each time we iterate over all vertices
But if optimized with adjacency list, becomes O(V+E)

### Space
O(V) space for in-degree storage
If optimized with adjacency list, O(V+E)

