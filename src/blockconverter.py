from blocktype import BlockType
import re

def block_to_block_type(block):

    headings = re.match("^(#){1,6} ", block)
    if headings:
        return BlockType.HEADING
    code_blocks = re.findall("^(```.+?```)", block, flags=re.DOTALL|re.MULTILINE)
    if code_blocks:
        return BlockType.CODE
    quote = re.match("^>.", block)
    quote_missing = re.search("^[^>]", block, flags=re.MULTILINE)
    if quote and quote_missing is None:
        return BlockType.QUOTE
    ulist = re.match("^- (.*)", block, flags=re.MULTILINE)
    ul_missing = re.search("^-[^ ]|^[^-]", block, flags=re.MULTILINE)
    if ulist and ul_missing is None:
        return BlockType.UNORDERED_LIST
    olist = re.match("^\d+\.(.*)", block, flags=re.MULTILINE)
    ol_missing = re.search("^([\D]+)|^(\d+[^\.])", block, flags=re.MULTILINE)
    if olist and ol_missing is None:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    

