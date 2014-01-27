import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
 
UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['gif','jpeg','jpg','png'])
 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from sklearn import linear_model

def load_classifier_from_disk():
    try:
        return pickle.load(open("../data/classifier.bin", "rb"))
    except:
        return False

clf = load_classifier_from_disk()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
@app.route('/info/')
def info():
    return """
    <!doctype html>
    <title>Info</title>
    <h1>Info</h1>
    <p>Whatever</p>
    """

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('info'))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
