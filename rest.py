from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
import wave
import numpy as np


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class UploadWavAPI(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('audio', type=FileStorage, location='files')

        args = parse.parse_args()

        stream = args['audio'].stream
        wav_file = wave.open(stream, 'rb')
        signal = wav_file.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        fs = wav_file.getframerate()        
        wav_file.close()       

api.add_resource(HelloWorld, '/')

api.add_resource(UploadWavAPI, '/upload')

if __name__ == '__main__':
    app.run(debug=True)