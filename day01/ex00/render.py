import sys
import os
import settings

def read_settings():
    return {key:value for key, value in settings.__dict__.items() if not key.startswith("__")}

def replace_placeholders(content, settings):
    for key, value in settings.items():
        content = content.replace(f"{{{key}}}", str(value).replace("\n", "<br>"))
    return content

def main():
    if len(sys.argv) != 2:
        print("Número errado de argumentos informado no terminal. Passe os argumentos corretamente")
        sys.exit(1)

    template_file = sys.argv[1]

    if not template_file.endswith(".template"):
        print("O arquivo deve ser da extensão .template")
        sys.exit(1)

    if not os.path.exists(template_file):
        print(f"O arquivo {template_file} não existe")
        sys.exit(1)

    try:
        with open(template_file, "r") as file:
            content = file.read()
        settings = read_settings()
        content = replace_placeholders(content, settings)
        html_file = template_file.replace(".template", ".html")

        with open(html_file, "w") as file:
            file.write(content)
        print(f"Arquivo {html_file} gerado com sucesso")

        
    except Exception as e:
        print(f"Erro ao processar o arquivo:{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    