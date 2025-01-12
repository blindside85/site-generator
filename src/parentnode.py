from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        if not isinstance(children, list):
            raise ValueError("Children must be a list")
            
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        # Generate opening tag with props
        props_html = self.props_to_html()
        html = f"<{self.tag}{props_html}>"
        
        # Recursively render all children
        for child in self.children:
            html += child.to_html()
            
        # Add closing tag
        html += f"</{self.tag}>"
        
        return html
