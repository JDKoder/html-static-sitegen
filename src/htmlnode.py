class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def props_to_html(self):
        prop_str = ""
        if self.props and len(self.props)>0:
            for prop in self.props.keys():
                prop_str += f" {prop}=\"{self.props[prop]}\""
        return prop_str


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


    def to_html(self):
        node_string = f"{self.value}"
        if self.tag is not None:
            node_string =f"<{self.tag}{self.props_to_html()}>{node_string}</{self.tag}>"
        return node_string


class LeafNode(HTMLNode):
    def __init__(self, ltag=None, lvalue=None, lprops=None):
        if lvalue == None:
            raise ValueError("Leaf nodes must have a value")
        super().__init__(tag=ltag, value=lvalue, props=lprops)


class ParentNode(HTMLNode):

    def __init__(self, ptag=None, pchildren=None, pprops=None):
        if ptag == None:
            raise ValueError("ptag is required for ParentNode")
        if pchildren == None:
            raise ValueError("children is required for ParentNode")
        super().__init__(tag=ptag, children=pchildren, props=pprops)


    def to_html(self):
        if self.tag == None:
            raise ValueError("ptag is required for ParentNode")
        if self.children == None:
            raise ValueError("children is required for ParentNode")
        child_string = ""
        for child in self.children:
            child_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"
 
                         

"""node = HTMLNode(tag="a", value="foo", props={"href":"https://www.foo.com"})
print(node)"""
