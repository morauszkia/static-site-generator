from textnode import *
from extract_markdown import *

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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type in [TextType.LINK, TextType.IMAGE]:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        remaining_text = node.text

        for image in images:
            alt_text, src = image
            before_text, remaining_text = remaining_text.split(f"![{alt_text}]({src})")
            if before_text != "":
                new_nodes.append(TextNode(before_text, node.text_type))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, src))
        
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, node.text_type))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type in [TextType.LINK, TextType.IMAGE]:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        remaining_text = node.text

        for link in links:
            link_text, url = link
            before_text, remaining_text = remaining_text.split(f"[{link_text}]({url})")
            if before_text != "":
                new_nodes.append(TextNode(before_text, node.text_type))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
        
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, node.text_type))
    return new_nodes