from flask import Flask, send_from_directory, make_response
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from utils import split, ziped
import os, json

app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

class TestApi(Resource):
    def get(self):
        data = {
            "response": "Test Api",
            "status": True,
        }

        return output_json(data, 200)

api.add_resource(TestApi, '/')

class DownloadAPI(Resource):
    def get(self):        
        #return {'Teste': 'Api'}
        return send_from_directory('files/separate/audio','extractFiles.zip') 
        
api.add_resource(DownloadAPI, '/download')            

class UploadAPI(Resource):
    def post(self):
        os.system("rm -rf files/separate/audio")        
        parse = reqparse.RequestParser()
        parse.add_argument('audio', type=FileStorage, location='files')

        args = parse.parse_args()
        stream = args['audio']
        
        stream.save("files/audio.wav")
               
        split.separa(2,"files/audio.wav")
        #split.separa(4,wav_file)
        os.system("rm -rf files/audio.wav")
        ziped.zipFilesInDir('files/separate/', 'files/separate/audio/extractFiles.zip', lambda name : 'wav' in name)

        data = {
            "response": "Source separation fineshed",
            "status": True,
        }

        return output_json(data, 200)                       

api.add_resource(UploadAPI, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
