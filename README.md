# Split
 API that hosts the Spleeter neural network for source music separation and uploads and downloads files via REST.
 
### Python Version on the project was made:
``
V3.6
``
### The Last Python Version that works is here:
``
V3.6.15
``

### Install PyEnv to manage the multiple Versions:

https://realpython.com/intro-to-pyenv/
 
 ### Create a virtual Python3.8 environment on Linux, Win, or Mac:
 ```
 python -m venv venv3-8
 ```
 
 ```
 source venv3-8/bin/activate
 ```
 ### install requirements and libraries
 ```
 pip install -r requirements.txt
 ```

 ### Run the application in the Rest.py file, for now.
Command inside project folder: 
```
python app.py
```

### Routes: 
``
127.0.0.1:5000/ - GET - Returns a test string in Json format
``

``
127.0.0.1:5000/upload - POST - File upload by parameter in Body - "audio" : <nameFile> - and neural network processing:
``
```
curl --location '127.0.0.1:5000/upload' \
--form 'audio=@"/home/filipe-borato/Documents/It dont mean i think_ master.mp3"'
```
``
127.0.0.1:5000/download - GET - Download the last track processed by the neural network
``
### Split connects to another project of mine called CompressorAndSplit

The Split project is coupled to a plugin I created with the name Boratio, in C++ with Juce Framework, and it's a github project called CompressorAndSplit

### THIS IS MY SERVER AND HE HOSTED THE SPLEETER NEURAL NETWORK
this project is a neural network that removes or separates the voice between the instruments
 
 
