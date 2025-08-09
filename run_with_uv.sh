#!/bin/bash
# Script para rodar o projeto usando UV

echo "🚀 Iniciando o projeto Split com UV..."

# Verificar se está no ambiente virtual UV
if [ ! -d ".venv" ]; then
    echo "⚠️  Ambiente virtual não encontrado. Criando..."
    uv venv --python 3.11
fi

# Ativar ambiente virtual
source .venv/bin/activate

echo "📦 Verificando dependências..."
uv pip install -r requirements.txt

echo "🎵 Iniciando servidor Flask..."
uv run python app.py
