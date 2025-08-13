# Migração para Python 3.11

## Resumo das Mudanças

Este projeto foi atualizado para ser compatível com Python 3.11. As principais mudanças incluem:

### 1. Remoção de Dependências Desnecessárias
- Removidas **75+ bibliotecas** desnecessárias (Jupyter, Qt, bibliotecas de desenvolvimento, etc.)
- Mantidas apenas as dependências essenciais para o funcionamento da API

### 2. Duas Opções de Audio Processing

#### Opção A: Spleeter Atualizado
```bash
# Descomente no requirements.txt:
spleeter==2.4.0
tensorflow>=2.13.0,<2.16.0

# Use o arquivo:
cp utils/split_spleeter.py utils/split.py
```

#### Opção B: Demucs (Recomendado)
```bash
# Descomente no requirements.txt:
demucs>=4.0.0
torch>=2.0.0
torchaudio>=2.0.0

# Use o arquivo:
cp utils/split_demucs.py utils/split.py
```

## Instruções de Instalação

### 1. Criar ambiente Python 3.11
```bash
# Com pyenv
pyenv install 3.11.0
pyenv local 3.11.0

# Ou com uv
uv python install 3.11
```

### 2. Escolher uma opção de audio processing
Edite o `requirements.txt` e descomente uma das opções (Spleeter ou Demucs).

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Substituir arquivo de separação
```bash
# Para Spleeter:
cp utils/split_spleeter.py utils/split.py

# Para Demucs (recomendado):
cp utils/split_demucs.py utils/split.py
```

## Vantagens do Demucs sobre Spleeter

1. **Melhor qualidade** de separação
2. **Suporte nativo** ao Python 3.11
3. **Modelos mais modernos** (baseados em PyTorch)
4. **Melhor manutenção** e atualizações regulares
5. **Compatibilidade** com hardware moderno (GPU)

## Estrutura Final do Projeto

```
Split/
├── app.py                          # API Flask principal
├── requirements.txt                # Dependências limpas para Python 3.11
├── utils/
│   ├── split.py                   # Arquivo atual (substituir)
│   ├── split_spleeter.py          # Versão com Spleeter
│   ├── split_demucs.py            # Versão com Demucs
│   └── ziped.py                   # Utilitário de compressão
└── MIGRATION_PYTHON311.md         # Este arquivo
```

## Testando a Migração

1. Inicie o servidor: `python app.py`
2. Teste o endpoint: `curl -X POST -F "audio=@test.mp3" http://localhost:5000/upload`
3. Verifique se os arquivos são gerados em `files/separate/audio/`
