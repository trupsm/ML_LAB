from queue import PriorityQueue
def best_first_search(graph, heuristic, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    while not pq.empty():
        h, current = pq.get()
        if current in visited:
            continue
        print(current, end=" ")
        if current == goal:
            print("\nGoal Reached")
            return
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
# Input
graph = {}
heuristic = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node: ")
    heuristic[node] = int(input("Enter heuristic value: "))
    graph[node] = input("Enter neighbors separated by space: ").split()
start = input("Enter start node: ")
goal = input("Enter goal node: ")
best_first_search(graph, heuristic, start, goal)