#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        # return super().__str__().replace('\n', '\n<br />\n')
        if super().__str__() == '<':
            str_to_replace = '<'
            str_replaced = '&lt;'
        elif super().__str__() == '>':
            str_to_replace = '>'
            str_replaced = '&gt;'
        elif super().__str__() == '"':
            str_to_replace = '"'
            str_replaced = '&quot;'
        else:
            str_to_replace = '\n'
            str_replaced = '\n<br />\n'
        return super().__str__().replace(str_to_replace, str_replaced)

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self):
            super().__init__("HTML page cannot be done")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        if not Elem.check_type(content) and content is not None:
            raise Elem.ValidationError
        self.content = content  
        self.tag_type = tag_type
        self._index = 0

    def __str__(self, level=0):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        indent = '  ' * level
        content = self.__make_content(level+1)
        if self.tag_type == 'double':
            result = "<{tag}{attributes}>{content}</{tag}>".format(
                tag=self.tag, 
                attributes= self.__make_attr(), 
                content=('\n' + content + '\n' + indent) if content.strip() else '',
            )

        elif self.tag_type == 'simple':
            result = "<{tag}{attributes} />".format(
                tag=self.tag,
                attributes = self.__make_attr()
            )
        return indent+result

    def __iter__(self): 
        yield self
 
    def __next__(self): 
        if self._index < len(self.content): 
            self._index += 1 
            yield self.content[self._index-1]
        else: 
            raise StopIteration 

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result
        
    def __make_content(self, level):
        if self.content is None:
            return ''

        if isinstance(self.content, list):
            content = '\n'.join(str(c) for c in self.content)
        elif isinstance(self.content, Elem):
            content = str(self.content)
        else:
            content = self.content if self.content else ''

        # Apply indentation to each line of the content
        return '\n'.join('  ' * level + line for line in content.split('\n') if line.strip())

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

def main():
    page = Elem(
        tag='html',
        content=[
            Elem(
                tag='head',
                content=[
                    Elem(
                        tag='title',
                        content=[Text('Hello ground!')],
                    )
                ]
            ),
            Elem(
                tag='body',
                content=[
                    Elem(
                        tag='h1',
                        content=[Text('Oh no, not again!')],
                    ),
                    Elem(
                        tag='img',
                        attr={'src': 'http://i.imgur.com/pfp3T.jpg'},
                        tag_type='simple'
                    )
                ]
            )
        ],
    )

    print(page)

if __name__ == '__main__':
    main()