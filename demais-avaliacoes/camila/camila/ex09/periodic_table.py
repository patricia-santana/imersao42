def save_html(content):
    with open("periodic_table.html", "w") as file:
        file.write(content)

def document(content):
    return "\n".join([
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<title>Tabela Periódica dos Elementos Químicos</title>",
        "</head>",
        "<body>",
        content,
        "</body>",
        "</html>"
    ])
    
def element_table(data):
    ret = []
    for element in data:
        for name,values in element.items():
            ret.append(table_row(element_cell(name,values)))
    return table("\n".join(ret))

def element_cell(name, values):
    content = "\n".join([
        title(name),
        property_list(values)
    ])
    return table_data(content)

def table(content):
    return "\n".join([
        "<table>",
content,
"</table>"
    ])

def table_row(content):
    return "\n".join([
        "<tr>",
        content,
        "</tr>"
    ])

def table_data(content):
    return "\n".join([
"<td>",
content,
"</td>"
    ])

def title(content):
    return "".join([
"<h4>",
content,
"</h4>"
    ])

def property_list(properties):
    ret = ["<ul>"]
    for item in properties:
        ret.append("".join([
"<li>",
item,
"</li>"
        ]))
    ret.append("</ul>")
    return "\n".join(ret)

def break_element(element):
    ret = {}
    pair = element.split(" = ")
    key = pair[0]
    values = pair[1].split(",")
    ret[key] = values
    return ret



def main():
    with open("periodic_table.txt", "r") as file:
        lines = file.readlines()
    file.close()
    data = []
    for line in lines:
        data.append(break_element(line))    
    html = document(element_table(data))    
    save_html(html)

main()