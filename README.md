# Split
 API that hosts the Spleeter neural network and uploads and downloads files via REST.
 
 # Crie um ambiente python virtual no linux
 python3.6 -m venv venv
 
 source venv/bin/activate
 
 # instalar requesitos e bibliotecas
 pip install -r requirements.txt

 # Rodar a aplicação em Rest 
Comando dentro da pasta do projeto: python rest.py

127.0.0.1:5000/ - GET - Retorna uma string de teste em formato Json

127.0.0.1:5000/upload - POST - Upload de arquivo por parâmetro no Body - "audio" : <nameFile> - e processamento da rede neural
 
127.0.0.1:5000/download - GET - Download da última faixa processada pela rede neural
