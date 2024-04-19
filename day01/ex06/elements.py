
from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None):
        super().__init__('html', content)

class Head(Elem):
    def __init__(self, content=None):
        super().__init__('head', content)

class Body(Elem):
    def __init__(self, content=None):
        super().__init__('body', content)

class Title(Elem):
    def __init__(self, content=None):
        super().__init__('title', content)

class Meta(Elem):
    def __init__(self, attributes=None):
        super().__init__('meta', None, attributes)

class Img(Elem):
    def __init__(self, attributes=None):
        super().__init__('img', None, attributes)

class Table(Elem):
    def __init__(self, content=None):
        super().__init__('table', content)

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__('tr', content)

class Td(Elem):
    def __init__(self, content=None):
        super().__init__('td', content)

class Th(Elem):
    def __init__(self, content=None):
        super().__init__('th', content)


class Ul(Elem):
    def __init__(self, attributes=None):
        super().__init__('ul', None, attributes)

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__('ol', content)

class Li(Elem):
    def __init__(self, content=None):
        super().__init__('li', content)

class H1(Elem):
    def __init__(self, content=None):
        super().__init__('h1', content)

class H2(Elem):
    def __init__(self, content=None):
        super().__init__('h2', content)

class p(Elem):
   def __init__(self, content=None):
        super().__init__('p', content)

class Div(Elem):
    def __init__(self, content=None):
        super().__init__('div', content)

class Span(Elem):
    def __init__(self, content=None):
        super().__init__('span', content)

class Hr(Elem):
    def __init__(self, content=None):
        super().__init__('hr', content)

class Br(Elem):
    def __init__(self, content=None):
        super().__init__('br', content)