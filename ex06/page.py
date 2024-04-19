from elements import *

class Page:
    def __init__(self, root_elem):
        if not isinstance(root_elem, Html):
            raise ValueError("root_elem must be an instance of Html")
        self.root = root_elem

    def is_valid(self):
        def validate_children(parent, valid_children_types, min_count=0, max_count=None, mutually_exclusive_with=None):
            count = 0
            for child in parent.content:
                if mutually_exclusive_with and isinstance(child, mutually_exclusive_with):
                    return False
                if not isinstance(child, valid_children_types):
                    return False
                if isinstance(child, (Title, H1, H2, Li, Th, Td, p, Span, Br, Hr)) and not isinstance(child.content, Text):
                    if len(child.content) != 1 or not isinstance(child.content[0], Text):
                        return False
                count += 1
            return count >= min_count and (max_count is None or count <= max_count)

        def validate(node):
            if isinstance(node, Html):
                has_head = has_body = False
                for child in node.content:
                    if isinstance(child, Head):
                        if not has_head and validate_children(child, Title, 1, 1):
                            has_head = True
                        else:
                            return False
                    elif isinstance(child, Body):
                        if not has_body and validate_children(child, (H1, H2, Div, Table, Ul, Ol, Span, Text, p)):
                            has_body = True
                        else:
                            return False
                return has_head and has_body
            elif isinstance(node, Head):
                return validate_children(node, Title, 1, 1)
            elif isinstance(node, Body):
                return validate_children(node, (H1, H2, Div, Table, Ul, Ol, Span, Text, p))
            elif isinstance(node, Div):
                return validate_children(node, (H1, H2, Div, Table, Ul, Ol, Span, Text, p))
            elif isinstance(node, Table):
                return validate_children(node, Tr)
            elif isinstance(node, Tr):
                return validate_children(node, (Th, Td), 1, mutually_exclusive_with=Th) or \
                       validate_children(node, (Td), 1, mutually_exclusive_with=Td)
            elif isinstance(node, Ul):
                return validate_children(node, Li, 1)
            elif isinstance(node, Ol):
                return validate_children(node, Li, 1)
            return True

        return all(validate(child) for child in self.root.content)

    def __str__(self):
        doctype = "<!DOCTYPE html>\n" if isinstance(self.root, Html) else ""
        return doctype + str(self.root)

    def write_to_file(self, filename):
        html_code = str(self)
        with open(filename, 'w') as file:
            file.write(html_code)

if __name__ == "__main__":
    html_structure = Html([
        Head([Title([Text("Example Title")])]),
        Body([
            Div([H1([Text("Header 1")]), p([Text("Paragraph text")])]),
            Table([Tr([Th([Text("Table header")]), Td([Text("Table cell")])])])
        ])
    ])
    page = Page(html_structure)
    print("Is the page valid?", page.is_valid())
    print(page)
    page.write_to_file("output.html")
