#!/bin/bash

# Exibe a versão do pip
pip_version=$(pip --version)
echo "Usando a versão do pip: $pip_version"

# Define o diretório para instalar a biblioteca
install_dir="local_lib"

# Remove o diretório local_lib existente, se existir
if [ -d "$install_dir" ]; then
    echo "Removendo o diretório existente $install_dir..."
    rm -rf "$install_dir"
fi

# Instala a versão de desenvolvimento do path.py do repositório GitHub
echo "Instalando o path.py do repositório GitHub..."
pip install git+https://github.com/jaraco/path.py.git --target="$install_dir" > install.log 2>&1

# Verifica se a instalação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "Instalação bem-sucedida."
    
    # Executa o programa Python
    python program.py
else
    echo "Falha na instalação. Verifique o arquivo install.log para detalhes."
fi
