from rich.tree import Tree
from rich.console import Console
from model import Node

def ast_to_tree(node, label="AST"):
    """Convierte el AST a un árbol Rich para imprimir en consola."""
    def build_tree(tree, obj):
        if isinstance(obj, Node):
            branch = tree.add(obj.__class__.__name__)
            for field, value in obj.__dict__.items():
                sub = branch.add(f"[bold]{field}[/]:")
                build_tree(sub, value)
        elif isinstance(obj, list):
            branch = tree.add("list")
            for item in obj:
                build_tree(branch, item)
        else:
            tree.add(repr(obj))

    root = Tree(label)
    build_tree(root, node)
    return root

def print_astt(node):
    console = Console()
    console.print(ast_to_tree(node))
