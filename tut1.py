import glob
import shutil
import uuid
import deepface.DeepFace
from flask import Flask, json, request, jsonify
import os
import urllib.request
from deepface import DeepFace
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = r'C:\Users\admin\PycharmProjects\flaskproject\sample'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def main():
    return 'Homepage'


@app.route('/upload', methods=['POST'])
def upload_file():

    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')
    anal = False
    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
            errors[file.filename] = 'File type is allowed'
            anal = True


    if success and anal:
        filename = str(uuid.uuid4())

        file1 = open(filename+".txt", "w")
        file2 = open(filename + ".png", "w")
        list_of_files: list[str] = glob.glob(r'C:\Users\admin\PycharmProjects\flaskproject\sample\*')
        latest_file = max(list_of_files, key=os.path.getctime)
        shutil.copyfile(latest_file, filename + ".png")
        try:
            demography = DeepFace.analyze(filename + ".png", actions=['age', 'gender', 'race', 'emotion'])

            print("gender:", demography["gender"])
            file = open(filename + ".txt", "w")

            file.write(demography['gender'])
            file.close()
            file = open(filename+".txt","r")


            gender = file.read()
            resp = jsonify({'message': 'valid image format', 'Gender': gender})
            file.close()
            resp.status_code = 201
            return resp
        except:
            file = open(filename+".txt","w")
            file.write("invalid image")
            file.close()
            file = open(filename+".txt","r")
            response =file.read()
            resp = jsonify({ 'message': response})

            return resp
        finally:
            dir = r'C:\Users\admin\PycharmProjects\flaskproject\sample'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))


    else:
        errors['message'] = "please enter a valid file"
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





