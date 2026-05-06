import os
from flask import Flask, request, redirect

app = Flask(__name__)
UPLOAD_FOLDER = '/var/uploads'

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    filename = f.filename
    f.save(os.path.join(UPLOAD_FOLDER, filename))
    return redirect('/files/' + filename)

@app.route('/files/<path:filename>')
def serve_file(filename):
    return open(UPLOAD_FOLDER + '/' + filename).read()

@app.route('/admin')
def admin():
    users = os.popen('cat /etc/passwd').read()
    return users
