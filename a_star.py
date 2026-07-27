from queue import PriorityQueue
# A* Search Function
def a_star(graph, heuristic, start, goal):
    visited = set()
    pq = PriorityQueue()
    # (f(n), g(n), node)
    pq.put((heuristic[start], 0, start))
    while not pq.empty():
        f, g, current = pq.get()
        if current in visited:
            continue
        print(current, end=" ")
        if current == goal:
            print("\nGoal Reached")
            print("cost: ",g)
            return
        visited.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                pq.put((f_new, g_new, neighbor))
# -------- INPUT --------
graph = {}
heuristic = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("\nEnter node: ")
    heuristic[node] = int(input("Enter heuristic value: ") )
    neighbors = int(input("Enter number of neighbors: "))
    graph[node] = []
    for j in range(neighbors):
        neighbor = input("Enter neighbor: ")
        cost = int(input("Enter cost: "))
        graph[node].append((neighbor, cost))
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
a_star(graph, heuristic, start, goal)