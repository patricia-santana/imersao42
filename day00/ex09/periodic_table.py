import sys

def make_template(table):
    titulo = "..: TABELA PERIÓDICA :.."
    body_h1 = "Exercício 9"
    tabela = table
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <title>{titulo}</title>
    </head>
    <body>
        <center><h1>{body_h1}</h1></center>
        <table style="border-collapse: collapse" border=solid>{tabela}</table>
    </body>
    </html>
    """
    #html_template = html_template.format(titulo=titulo, body_h1=body_h1)
    with open("./periodic_table.html", "w") as arquivo:
        table = arquivo.write(html_template)
    return table


def read_elements():
    elements  = {}
    with open("./periodic_table.txt", "r") as arquivo:
        for linha in arquivo:
            if linha.strip():
                name, properties = linha.split("=")
                properties = properties.split(',')
                element_data = {
                    'name': name.strip(),
                    'position': int(properties[0].split(':')[1].strip()),
                    'number': int(properties[1].split(':')[1].strip()),
                    'symbol': properties[2].split(':')[1].strip(),
                    'molar': float(properties[3].split(':')[1].strip()),
                    'electron': properties[4].split(':')[1].strip()
                }
                elements[element_data['number']] = element_data
    return elements
    

def make_table(elements):
    max_columns = 5
    html_table = '<table style="border-collapse: collapse; width: 100%;">\n'

    current_column = 0
    for i in range(1, 119):
        element = elements.get(i)
        if current_column == 0:
            html_table += '<tr>\n'
        
        if element:
            color = "blue" if element["number"] % 2 == 0 else "lightblue"
            html_table += (
                f'<td style="border: 1px solid black; padding:10px; background-color: {color};">'
                f'<h4>{element["name"]}</h4>'
                f'<ul>'
                f'<li>No {element["number"]}</li>'
                f'<li>{element["symbol"]}</li>'
                f'<li>{element["molar"]} g/mol</li>'
                f'<li>{element["electron"]} electron</li>'
                f'</ul>'
                f'</td>'
            )
            current_column += 1
        else:
            if current_column < max_columns:
               continue
                
        if current_column == max_columns: 
            html_table += '</tr>\n'
            current_column = 0

    html_table += '</table>'
    return html_table


def main():
    
    elements = read_elements()
    table= make_table(elements)
    make_template(table)


if __name__ == '__main__':
    main()