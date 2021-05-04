import os
from flask import Flask, render_template, request
from s3_store import upload_file


application= app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "faceimag"

@app.route('/')
@app.route('/imageUpload')
def upload_image():
   return render_template('upload.html')
    
@app.route('/imageUploader', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(UPLOAD_FOLDER, f.filename))
      upload_file(f"uploads/{f.filename}", BUCKET)
      
      return 'file uploaded successfully'
        
if __name__ == '__main__':
   app.run(port=5000,debug = True)
