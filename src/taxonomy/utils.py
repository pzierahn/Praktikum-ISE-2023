from typing import List
from treelib import Tree

from src.taxonomy.parser import TaxonomyParserNode, parse_nodes


def _build_tree_recursively(tree: Tree, taxonomy: List[TaxonomyParserNode], parent="root"):
    for node in taxonomy:
        if not tree.contains(node.name):
            tree.create_node(node.name, node.name, parent=parent)
        _build_tree_recursively(tree, node.children, parent=node.name)


def build_taxonomy_tree(taxonomy: List[TaxonomyParserNode], root='Taxonomy') -> Tree:
    """
    Build a tree from the taxonomy
    :param taxonomy: Input taxonomy
    :param root: Root node name
    :return: taxonomy tree
    """

    tree = Tree()
    tree.create_node(root, root)
    _build_tree_recursively(tree, taxonomy, parent=root)

    return tree


def parse_taxonomy(taxonomy: str) -> Tree:
    """
    Parse the taxonomy and build a tree
    :param taxonomy: Input taxonomy
    :return: taxonomy tree
    """
    nodes = parse_nodes(taxonomy)
    return build_taxonomy_tree(nodes)
