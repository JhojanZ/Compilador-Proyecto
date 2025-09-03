from graphviz import Digraph
from model import Node

def ast_to_graph(node, graph=None, parent=None, counter=None):
    if counter is None:
        counter = [0]
    """Convierte el AST a un grafo Graphviz para exportar a PNG."""
    if graph is None:
        graph = Digraph("AST", format="png")
        graph.attr("node", shape="box", style="rounded,filled", color="lightblue")

    if isinstance(node, Node):
        counter[0] += 1
        node_id = f"n{counter[0]}"
        label = node.__class__.__name__
        graph.node(node_id, label)

        if parent:
            graph.edge(parent, node_id)

        for field, value in node.__dict__.items():
            if isinstance(value, (Node, list)):
                ast_to_graph(value, graph, node_id, counter)
            else:
                counter[0] += 1
                val_id = f"n{counter[0]}"
                graph.node(val_id, f"{field}: {value}", shape="ellipse", color="lightgray")
                graph.edge(node_id, val_id)

    elif isinstance(node, list):
        for item in node:
            ast_to_graph(item, graph, parent, counter)

    return graph
