import os
from flask import Flask, request, redirect

app = Flask(__name__)
UPLOAD_FOLDER = '/var/uploads'

@app.route('/upload', methods=['POST'])
def upload_file():
    # VULNERABILITY: No file type validation
    f = request.files['file']
    filename = f.filename  # VULNERABILITY: No path sanitisation
    f.save(os.path.join(UPLOAD_FOLDER, filename))
    return redirect('/files/' + filename)

@app.route('/files/<path:filename>')
def serve_file(filename):
    # VULNERABILITY: Path traversal — ../../etc/passwd works
    return open(UPLOAD_FOLDER + '/' + filename).read()

@app.route('/admin')
def admin():
    # VULNERABILITY: No authentication check
    users = os.popen('cat /etc/passwd').read()
    return users
