from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        fragments = node.text.split(delimiter)

        if not len(fragments) % 2:
            raise Exception("Invalid Markdown Syntax: Missing delimiter")
        
        for i in range(len(fragments)):
            if not fragments[i]:
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(fragments[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(fragments[i], text_type))
    
    return new_nodes