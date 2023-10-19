# Source: https://github.com/sebastiangoetz/slr-toolkit/blob/master/ios-client/SLR%20Toolkit/Logic/Taxonomy%20Parser/TaxonomyParser.swift
class TaxonomyParserNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []


def parse_nodes(taxonomy: str):
    if taxonomy.count('{') != taxonomy.count('}'):
        return None

    nodes = []
    parent = None
    string = ""
    last_control_char = ""

    for char in taxonomy:
        if char == "{":
            trimmed_string = string.strip()
            if trimmed_string == "":
                return None
            else:
                new_node = TaxonomyParserNode(trimmed_string, parent)
                if parent:
                    parent.children.append(new_node)
                else:
                    nodes.append(new_node)
                parent = new_node
                string = ""
            last_control_char = "{"
        elif char == "}":
            trimmed_string = string.strip()
            if trimmed_string == "":
                if last_control_char == "{" or last_control_char == ",":
                    return None
                elif last_control_char == "}":
                    parent = parent.parent
            else:
                if parent:
                    parent.children.append(TaxonomyParserNode(trimmed_string, parent))
                else:
                    return None
                string = ""
            last_control_char = "}"
        elif char == ",":
            trimmed_string = string.strip()
            if trimmed_string == "":
                if last_control_char == "{" or last_control_char == ",":
                    return None
                elif last_control_char == "}":
                    parent = parent.parent
            else:
                if parent:
                    parent.children.append(TaxonomyParserNode(trimmed_string, parent))
                else:
                    nodes.append(TaxonomyParserNode(trimmed_string))
                string = ""
            last_control_char = ","
        else:
            string += char

    trimmed_string = string.strip()
    if trimmed_string != "":
        nodes.append(TaxonomyParserNode(trimmed_string))

    return nodes
