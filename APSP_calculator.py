def bellman_ford(graph, source):
    V = len(graph)
    distance = [float('inf')] * V
    distance[source] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative-weight cycles
    for u, v, w in graph:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            return None  # Indicates a negative cycle

    return distance


def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        # print(f"Content of the file: \n{content}\n")

        # Replacing curly braces, stripping spaces, and splitting by comma
        parts = content.replace("{", "").replace("}", "").split(",")

        # Removing white spaces and converting the strings into integers
        numbers = list(map(int, map(str.strip, parts)))

        # Checking if the total number of numbers is divisible by 3 (for u, v, w)
        if len(numbers) % 3 != 0:
            raise ValueError(
                "Unexpected format: The total number of numbers in the file should be divisible by 3.")

        graph = []
        for i in range(0, len(numbers), 3):
            u, v, w = numbers[i], numbers[i+1], numbers[i+2]
            graph.append((u-1, v-1, w))  # -1 for 0-based indexing

    return graph


filename = "graph.txt"
graph = read_input(filename)
if not graph:
    print("Failed to read the graph from the input file.")
    exit()

while True:
    try:
        source_vertex = int(input("Enter start vertex (or '0' to quit): "))
        if source_vertex == 0:
            break

        # -1 for 0-based indexing
        distances = bellman_ford(graph, source_vertex - 1)

        if distances:
            end_vertex = int(input("Enter end vertex: "))
            d = distances[end_vertex - 1]  # -1 for 0-based indexing
            if d == float('inf'):
                print(
                    f"Shortest path from vertex {source_vertex} to vertex {end_vertex} is: inf")
            else:
                print(
                    f"Shortest path from vertex {source_vertex} to vertex {end_vertex} is: {d}")
        else:
            print("Graph contains a negative-weight cycle.")

    except ValueError:
        print("Please enter a valid number.")

print("Thank you for using the program!")
