from textnode import *
from split_nodes import *
from leafnode import LeafNode

delimiters = {
    "**": TextType.BOLD,
    "__": TextType.BOLD,
    "`": TextType.CODE,
    "*": TextType.ITALIC,
    "_": TextType.ITALIC,
}


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_image([text_node])
    new_nodes = split_nodes_link(new_nodes)
    
    for delimiter, text_type in delimiters.items():
        new_nodes = split_nodes_delimiter(new_nodes, delimiter, text_type)
    
    return new_nodes
    

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError("Link TextNode requires a non-empty url for href attribute")
            return LeafNode("a", text_node.text, { "href": text_node.url })      
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("Image TextNode requires a non-empty url for src attribute")
            alt_text = text_node.text if text_node.text else ""
            return LeafNode("img", "", { 
                "src": text_node.url, 
                "alt": alt_text
                })
        case _:
            raise ValueError("Text node has unknown type. Please, provide a valid type") 