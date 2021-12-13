from flask import Flask, render_template, request, send_file
from datetime import datetime
import werkzeug
import os
from flask_cors import CORS
import subprocess
from logging import getLogger

logger = getLogger(__name__)
logger.info('logger init')

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['vrm'])

app = Flask(__name__, static_folder='./webapp/dist/static', template_folder='./webapp/dist')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/_ah/health")
def _ah_health():
    return "ok"

def vreducer(src, dst, fileName):
    args = ['python', '/env/src/vreducer/vreducer.py', src, '-f', '-e']
    try:
        res = subprocess.check_call(args)
    except:
        logger.error('errr.')
    return send_file(dst, \
        as_attachment = True, \
        attachment_filename = fileName, \
        mimetype = 'application/octet-stream')

def allowed_file(name):
    return '.' in name and \
        name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_multipart():
    if 'vrm' not in request.files:
        return 'result : vrm file not found'
    file = request.files['vrm']
    fileName = file.filename
    if '' == fileName:
        return 'result : vrm file name not found'
    if allowed_file(fileName) == False:
        return 'result : extension error'
    logger.info('fileName ' + fileName)
    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") \
        + werkzeug.utils.secure_filename(fileName)
    logger.info('saveFileName ' + saveFileName)
    src = os.path.join(UPLOAD_FOLDER, saveFileName)
    dst = os.path.join(UPLOAD_FOLDER + '/result', saveFileName)
    file.save(src)
    return vreducer(src, dst, saveFileName)

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@app.route('/sample')
def sample():
    src = './webapp/dist/static/3043414890365630408.vrm'
    dst = './webapp/dist/static/result/vroid-mobile-sample.vrm'
    return vreducer(src, dst)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
