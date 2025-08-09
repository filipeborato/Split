# 🚀 Como usar o projeto Split com UV

## Comandos principais:

### 1. **Rodar o servidor com UV:**
```bash
uv run python app.py
```

### 2. **Rodar com script automático:**
```bash
./run_with_uv.sh
```

### 3. **Verificar se Demucs está funcionando:**
```bash
uv run python -c "import demucs; print('✅ Demucs OK!')"
```

### 4. **Testar a API:**
```bash
# Em outro terminal:
curl -X POST -F "audio=@seu_arquivo.mp3" http://localhost:5000/upload
```

## ✅ **Mudanças feitas para usar UV:**

1. **Arquivo `utils/split.py`** agora usa: `uv run python -m demucs`
2. **Arquivo `utils/ziped.py`** cria diretórios automaticamente
3. **Script `run_with_uv.sh`** para facilitar execução

## 🎵 **Como funciona agora:**

- **Demucs** faz a separação de áudio (melhor que Spleeter)
- **UV** gerencia o ambiente Python 3.11
- **Compatibilidade total** com Python 3.11
- **Dependências limpas** (de 95 para ~15 bibliotecas)

## 🔧 **Troubleshooting:**

Se der erro, rode:
```bash
uv pip install -r requirements.txt
source .venv/bin/activate
```
