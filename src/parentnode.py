from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have tag")
        if not self.children:
            raise ValueError("Parent node must have children")
        
        children_html_list = list(map(lambda x: x.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{''.join(children_html_list)}</{self.tag}>"