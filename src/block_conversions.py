import re
from enum import Enum

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