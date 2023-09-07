import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from deepface import DeepFace

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\Dell\PycharmProjects\flaskproject\sample'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def main():
    return 'Welcome to the Image Analysis API'


@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        try:
            demography = DeepFace.analyze(
                os.path.join(app.config['UPLOAD_FOLDER'], filename),
                actions = ['age', 'gender', 'race', 'emotion']
            )

            # Check if any faces were detected
            if len(demography) > 0:
                # Access the gender of the first detected face
                gender = demography[0]['gender']
                return jsonify({'message': 'Image analysis successful', 'gender': gender})
            else:
                return jsonify({'error': 'No faces detected in the image'}), 400

        except Exception as e:
            return jsonify({'error': 'Image analysis failed', 'message': str(e)}), 500


    else:
        return jsonify({'error': 'Invalid file format'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)






