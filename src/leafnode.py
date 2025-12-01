from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>" + (f"{self.value}</{self.tag}>" if self.tag != "img" else "")