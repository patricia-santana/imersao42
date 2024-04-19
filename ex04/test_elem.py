from elem import Elem, Text

def test():
    # Test Text behavior
    assert str(Text("Hello\nWorld")) == str(Text("Hello\nWorld"))
    assert str(Text("<tag>")) == "&lt;tag&gt;"

    # Test basic Elem
    assert str(Elem()) == "<div></div>"
    assert str(Elem(tag='span', tag_type='simple')) == "<span />"
    assert str(Elem(tag='div', content=Text("Hello"))) == "<div>\nHello\n</div>"

    # Test nested Elems
    inner = Elem(tag='div', content=Text("Inner"))
    outer = Elem(tag='div', content=inner)
    assert str(outer) == "<div>\n<div>\nInner\n</div>\n</div>"

    # Test adding content
    elem = Elem()
    elem.add_content(Text("Added"))
    assert str(elem) == "<div>\nAdded\n</div>"

    print("All tests passed!")

if __name__ == '__main__':
    test()
