from block_conversions import markdown_to_blocks, block_to_htmlnode
from parentnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    nodes = [block_to_htmlnode(block) for block in blocks]
    return ParentNode("div", nodes)

