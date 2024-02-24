from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    file.save(os.path.join('images', file.filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
