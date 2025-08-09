# Split
 API that hosts the Spleeter neural network for source music separation and uploads and downloads files via REST.
 
### Python Version used in the project was:
``
V3.6
``
### The Last Python Version that works is here:
``
V3.7
``

### Install PyEnv to manage multiple Versions:

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
 
 

## Prerequisite: FFmpeg

Spleeter uses FFmpeg to decode audio (mp3, wav, etc). Make sure `ffmpeg` is installed and available on your PATH before using `/upload`.

- Ubuntu/Debian (WSL/Linux):
  ```
  sudo apt-get update && sudo apt-get install -y ffmpeg
  ```
- macOS (Homebrew):
  ```
  brew install ffmpeg
  ```
- Windows:
  - Using winget: `winget install Gyan.FFmpeg`
  - Or Chocolatey: `choco install ffmpeg`
  - Ensure the `bin` folder (containing `ffmpeg.exe`) is added to your PATH.

Verify installation:
```
ffmpeg -version
```

Restart the Flask server after installation.
