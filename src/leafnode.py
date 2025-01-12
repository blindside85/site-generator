from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        # We pass None as children since LeafNodes cannot have children
        super().__init__(tag=tag, value=value, children=None, props=props)
        # Ensure children remains an empty list and can't be modified
        self.children = []
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
            
        # If there's no tag, return the raw text value
        if self.tag is None:
            return self.value
            
        # Generate the HTML with tag and props
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
