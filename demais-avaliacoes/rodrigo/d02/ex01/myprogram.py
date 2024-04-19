import sys
from path import Path

def main():
    # Cria uma pasta e um arquivo dentro dela
    folder_path = Path("output_folder")
    folder_path.mkdir(exist_ok=True)  # Cria a pasta se ela não existir
    file_path = folder_path / "output_file.txt"  # Caminho completo do arquivo dentro da pasta

    # Escreve algo no arquivo
    with open(file_path, "w") as file:
        file.write("Olá, isso está escrito no arquivo!")  # Escreve uma mensagem no arquivo

    # Lê e exibe o conteúdo do arquivo
    with open(file_path, "r") as file:
        content = file.read()  # Lê o conteúdo do arquivo
        print("Conteúdo do arquivo:")
        print(content)

if __name__ == "__main__":
    main()  # Chama a função principal quando o script é executado
