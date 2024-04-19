# elem.py

class Elem:
    def __init__(self, tag_name, content=None, attributes=None):
        self.tag_name = tag_name
        self.content = content if content else []
        self.attributes = attributes if attributes else {}

    def add(self, element):
        if not isinstance(element, Elem) and not isinstance(element, Text):
            raise ValueError("Can only add Elem or Text instances")
        self.content.append(element)

    def __str__(self, level=0):
        indent = '  ' * level
        attrs = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items()) if self.attributes else ''
        open_tag = f'{indent}<{self.tag_name}{(" " + attrs) if attrs else ""}>\n'
        inner = ''.join(child.__str__(level + 1) if isinstance(child, Elem) else indent + '  ' + str(child) for child in self.content)
        close_tag = f'{indent}</{self.tag_name}>\n'
        return f'{open_tag}{inner}{close_tag}'

class Text(Elem):
    def __init__(self, text):
        self.text = text.strip()

    def __str__(self, level=0):
        indent = '  ' * (level - 1)
        return f'{indent}{self.text}\n'
