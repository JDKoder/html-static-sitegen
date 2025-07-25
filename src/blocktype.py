from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"
