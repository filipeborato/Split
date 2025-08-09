from flask import Flask, send_from_directory, make_response, request
from flask_restful import Resource, Api
from werkzeug.datastructures import FileStorage
from werkzeug.exceptions import BadRequest, RequestEntityTooLarge, ClientDisconnected
from werkzeug.utils import secure_filename
from utils import split, ziped
import os, json

app = Flask(__name__)
# Limit upload size to avoid hanging/parsing huge bodies (can be overridden via env)
app.config['MAX_CONTENT_LENGTH'] = int(os.environ.get('MAX_CONTENT_LENGTH', 64 * 1024 * 1024))  # 64 MB
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):    
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
        try:
            return send_from_directory('files/separate/audio','extractFiles.zip') 
        except Exception as err:
            data = {
                "response": "Download Failed",
                "status": False,
                "error": repr(err)
            }
            return output_json(data, 400)                       

        
api.add_resource(DownloadAPI, '/download')            

class UploadAPI(Resource):
    def post(self):
        try:
            os.makedirs("files", exist_ok=True)
            # Clean previous outputs safely
            try:
                import shutil
                shutil.rmtree("files/separate/audio", ignore_errors=True)
            except Exception:
                pass

            # Quick header checks before parsing body
            te = request.headers.get('Transfer-Encoding', '').lower()
            if te == 'chunked':
                data = {
                    "response": "Chunked uploads not supported by this server",
                    "status": False,
                }
                return output_json(data, 400)

            if request.mimetype != 'multipart/form-data':
                data = {
                    "response": "Content-Type must be multipart/form-data with field 'audio'",
                    "status": False,
                }
                return output_json(data, 400)

            # Accessing request.files may raise parsing errors; handle them explicitly
            try:
                files = request.files
            except RequestEntityTooLarge as e:
                data = {
                    "response": "Uploaded file too large",
                    "status": False,
                    "error": str(e),
                }
                return output_json(data, 413)
            except (ClientDisconnected, BadRequest) as e:
                data = {
                    "response": "Failed to read upload (client disconnected or bad request)",
                    "status": False,
                    "error": str(e),
                }
                return output_json(data, 400)

            if 'audio' not in files:
                data = {
                    "response": "Missing file field 'audio' in multipart/form-data",
                    "status": False,
                }
                return output_json(data, 400)

            stream: FileStorage = files['audio']
            if not stream or stream.filename == "":
                data = {
                    "response": "Empty file for field 'audio'",
                    "status": False,
                }
                return output_json(data, 400)

            # Ensure ffmpeg is available before trying to process
            import shutil as _shutil
            if _shutil.which('ffmpeg') is None:
                data = {
                    "response": "ffmpeg binary not found. Please install ffmpeg and ensure it is on PATH.",
                    "status": False,
                    "error": "MissingDependency: ffmpeg"
                }
                return output_json(data, 400)

            # Save using the original extension for correct decoding
            os.makedirs("files", exist_ok=True)
            original_name = secure_filename(stream.filename)
            _, ext = os.path.splitext(original_name)
            if not ext:
                ext = ".wav"
            target_path = os.path.join("files", f"audio{ext}")
            stream.save(target_path)

            split.separa(2, target_path)
            # Clean input file after processing
            try:
                os.remove(target_path)
            except FileNotFoundError:
                pass

            ziped.zipFilesInDir('files/separate/', 'files/separate/audio/extractFiles.zip', lambda name : 'wav' in name)

            data = {
                "response": "Source separation finished",
                "status": True,
            }

            return output_json(data, 200)

        except Exception as err:
            app.logger.exception("Upload processing failed")
            data = {
                "response": "Source separation did not finish",
                "status": False,
                "error": repr(err)
            }
            return output_json(data, 400)

api.add_resource(UploadAPI, '/upload')

# Simple HTML form for manual testing via browser
@app.route('/upload', methods=['GET'])
def upload_form():
    return (
        """
        <!doctype html>
        <title>Upload audio</title>
        <h1>Upload an audio file</h1>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <input type="file" name="audio" accept="audio/*" required />
            <button type="submit">Upload</button>
        </form>
        """,
        200,
        {"Content-Type": "text/html; charset=utf-8"}
    )

if __name__ == '__main__':
    app.run(debug=True)
