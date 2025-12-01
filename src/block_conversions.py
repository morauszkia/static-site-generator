import re
from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode
from textnode_conversions import text_to_textnodes, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.split("\n\n")]
    blocks = [block for block in blocks if block != ""]
    return blocks


def all_lines_startswith(linesList, pattern):
    return all(re.search(pattern, line) for line in linesList)


def block_to_blocktype(block):
    if re.search("^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")
    if all_lines_startswith(lines, "^>"):
        return BlockType.QUOTE
    if all_lines_startswith(lines, "^\- "):
        return BlockType.UNORDERED_LIST
    if all_lines_startswith(lines, "^\d+\. "):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = [text_node_to_html_node(node) for node in textnodes]
    return children


def block_to_htmlnode(block):
    block_type = block_to_blocktype(block)

    match (block_type):
        case BlockType.CODE:
            content = block.strip().removeprefix("```").removesuffix("```").strip()
            children = [LeafNode("code", content)]
            return ParentNode("pre", children)
        case BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
            
            tag = "h" + str(level)
            content = block[level:].strip()
            children = text_to_children(content)
            return ParentNode(tag, children)
        case BlockType.UNORDERED_LIST:
            content = [line.removeprefix("- ") for line in block.split("\n")]
            children = [ParentNode("li", text_to_children(line)) for line in content]
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            content = [line.lstrip("0123456789.").strip() for line in block.split("\n")]
            children = [ParentNode("li", text_to_children(line)) for line in content]
            return ParentNode("ol", children)
        case BlockType.QUOTE:
            content = "\n".join([line.removeprefix("> ") for line in block.split("\n")])
            children = text_to_children(content)
            return ParentNode("blockquote", children)
        case BlockType.PARAGRAPH:
            children = text_to_children(block.replace("\n", " "))
            return ParentNode("p", children)

