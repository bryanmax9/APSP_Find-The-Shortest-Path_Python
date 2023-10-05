import networkx as nx


def read_input(filename):
    G = nx.DiGraph()  # Create a directed graph

    with open(filename, 'r') as file:
        content = file.read().strip()

        # Replacing curly braces, stripping spaces, and splitting by comma
        parts = content.replace("{", "").replace("}", "").split(",")

        # Removing white spaces and converting the strings into integers
        numbers = list(map(int, map(str.strip, parts)))

        # Checking if the total number of numbers is divisible by 3 (for u, v, w)
        if len(numbers) % 3 != 0:
            raise ValueError(
                "Unexpected format: The total number of numbers in the file should be divisible by 3.")

        for i in range(0, len(numbers), 3):
            u, v, w = numbers[i], numbers[i+1], numbers[i+2]
            G.add_edge(u-1, v-1, weight=w)  # -1 for 0-based indexing

    return G


filename = "graph.txt"
G = read_input(filename)
if not G:
    print("Failed to read the graph from the input file.")
    exit()

while True:
    try:
        source_vertex = int(input("Enter start vertex (or '0' to quit): "))
        if source_vertex == 0:
            break

        # -1 for 0-based indexing
        try:
            distances = nx.single_source_bellman_ford_path_length(
                G, source_vertex - 1)
        except nx.NetworkXUnbounded:
            print("Graph contains a negative-weight cycle.")
            continue

        end_vertex = int(input("Enter end vertex: "))
        d = distances.get(end_vertex - 1, float('inf')
                          )  # -1 for 0-based indexing
        if d == float('inf'):
            print(
                f"Shortest path from vertex {source_vertex} to vertex {end_vertex} is: inf")
        else:
            print(
                f"Shortest path from vertex {source_vertex} to vertex {end_vertex} is: {d}")

    except ValueError:
        print("Please enter a valid number.")

print("Thank you for using the program!")
