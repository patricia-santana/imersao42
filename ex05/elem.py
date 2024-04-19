class Text(str):
    def __str__(self):
        return super().__str__().replace('\n', '\n<br />\n').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

class Elem:
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content = []
        if content is not None:
            self.add_content(content)

    def __str__(self):
        attrs = self.__make_attr()
        content_str = self.__make_content()
        if self.tag_type == 'double':
            return f"<{self.tag}{attrs}>{content_str}</{self.tag}>"
        else:  # Assume simple type for anything not double
            return f"<{self.tag}{attrs} />"

    def __make_attr(self):
        return ''.join(f' {key}="{value}"' for key, value in sorted(self.attr.items()))

    def __make_content(self):
        return '\n' + '\n'.join(str(elem) for elem in self.content) + '\n' if self.content else ''

    def add_content(self, new_content):
        if not self.check_type(new_content):
            raise Elem.ValidationError("Content must be Elem, Text, or a list of these.")
        if isinstance(new_content, list):
            self.content.extend(elem for elem in new_content if isinstance(elem, (Elem, Text)))
        else:
            self.content.append(new_content)

    @staticmethod
    def check_type(content):
        return isinstance(content, (Elem, Text)) or (isinstance(content, list) and all(isinstance(elem, (Elem, Text)) for elem in content))
