import matplotlib.pyplot as plt
import networ

# Create a directed graph
G = nx.DiGraph()

# Define the nodes
fact_table = "fact_sales"
dimension_tables = ["dim_products", "dim_customers", "dim_employees", "dim_date"]

# Add nodes to the graph
G.add_node(fact_table, color="red")
for dim in dimension_tables:
    G.add_node(dim, color="blue")
    G.add_edge(dim, fact_table)

# Define node colors
node_colors = ["red" if node == fact_table else "blue" for node in G.nodes()]

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=12, font_weight="bold", edge_color="black")
plt.title("Star Schema for Sales Data Warehouse", fontsize=14)
plt.show()
