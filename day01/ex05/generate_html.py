from elements import Html, Head, Body, Title, H1, Img

# Criação do documento HTML
html_document = Html([
    Head([
        Title("Hello ground!")
    ]),
    Body([
        H1("Oh no, not again!"),
        Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
    ])
])

# Escrevendo o HTML em um arquivo
with open('output.html', 'w') as f:
    f.write(str(html_document))

print("HTML gerado com sucesso e salvo em output.html!")
