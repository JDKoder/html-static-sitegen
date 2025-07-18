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
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, ltag=None, lvalue=None, lprops=None):
        if lvalue == None:
            raise ValueError("Leaf nodes must have a value")
        super().__init__(tag=ltag, value=lvalue, props=lprops)


"""node = HTMLNode(tag="a", value="foo", props={"href":"https://www.foo.com"})
print(node)"""
