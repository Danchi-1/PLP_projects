import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Define Hogwarts houses
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# Add nodes (houses)
G.add_nodes_from(houses)

# Define connections (friendships, rivalries, or alliances)
connections = [
    ("Gryffindor", "Hufflepuff"),
    ("Gryffindor", "Ravenclaw"),
    ("Gryffindor", "Slytherin"),  # Rivalry
    ("Hufflepuff", "Ravenclaw"),
    ("Hufflepuff", "Slytherin"),
    ("Ravenclaw", "Slytherin"),
]

# Add edges (connections) to the graph
G.add_edges_from(connections)

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(
    G, 
    with_labels=True, 
    node_color=["red", "yellow", "blue", "green"], 
    node_size=3000, 
    font_size=12, 
    edge_color="gray"
)
plt.title("Hogwarts House Connections")
plt.show()
