from flask import Flask, redirect, render_template, request, flash, jsonify, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os
from model import *



# Define the file path
file_path = '/Users/anjalijha/Downloads/LTS 2/flask_server/uploads'
# Specify the file path
file_path = '/Users/anjalijha/Downloads/LTS 2/flask_server/uploads'

# Print the file path
print("File path:", file_path)

# Check if the file exists
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")

# Print file path
print("File path:", file_path)

# Check if file exists
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")

UPLOAD_FOLDER = '/Users/anjalijha/Downloads/LTS 2/flask_server/uploads./upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'wav', 'ogg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            transcription = readLip(filename)
            full_path = app.root_path
            print(full_path)
            return render_template("fileUpload.html", transcription=transcription)
    return render_template("./fileUpload.html")

@app.route('/download', methods=['GET', 'POST'])
def download():
    full_path = app.root_path
    filename = "__temp__.mp4"
    return send_file(filename, as_attachment=True)

@app.route('/api', methods=['GET'])
def returnAscii():
    return {'output': ord(str(request.args['query']))}

if __name__ == "__main__":
    app.run(debug=True)


