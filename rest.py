from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
import wave
import numpy as np
import split
import os

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):        
        return {'hello': 'world'}
            

class UploadWavAPI(Resource):
    def post(self):
        os.system("rm -rf files/separate/audio")
        parse = reqparse.RequestParser()
        parse.add_argument('audio', type=FileStorage, location='files')

        args = parse.parse_args()
        stream = args['audio']
        #stream = args['audio']
        stream.save("files/audio.wav")
        #wav_file = wave.open(stream, 'rb')
        #signal = wav_file.readframes(-1)
        #signal = np.fromstring(signal, 'Int16')
        #fs = wav_file.getframerate() """
        #wav_file.close()        
        split.separa(2,"files/audio.wav")
        #split.separa(4,wav_file)
        os.system("rm -rf files/audio.wav")
        return "audio processado pelo split"                        

api.add_resource(HelloWorld, '/')

api.add_resource(UploadWavAPI, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
