from flask import Flask, render_template, request, send_file
from datetime import datetime
import werkzeug
import os
from flask_cors import CORS
import subprocess
from logging import getLogger

from os.path import dirname, join, exists, basename
from argparse import ArgumentParser
from src.vreducer.vrm.debug import print_stat
from src.vreducer.vrm.reducer import reduce_vroid
from src.vreducer.vrm.vrm import load
from src.vreducer.vrm.version import app_name

logger = getLogger(__name__)
logger.info('logger init')

VREDUCER_PATH = './src/vreducer/vreducer.py'
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['vrm'])

app = Flask(__name__, static_folder='./webapp/dist/static', template_folder='./webapp/dist')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/_ah/health")
def _ah_health():
    return "ok"

def parse_texture_size(texture_size_option):
    # テクスチャサイズオプションのパース
    option = texture_size_option.split(',')[:2]
    w, h = (option * 2)[:2]
    return int(w), int(h)

def convert_vrm(src, dst, fileName):    
    parser = ArgumentParser()
    parser.add_argument('path', help=u'VRM file exported by VRoid Studio.')
    parser.add_argument('-s', '--replace-shade-color', action='store_true', help=u'Replace shade color to main color.')
    parser.add_argument('-e', '--emissive-color', action='store_true',
                        help=u'Set main texture as emissive texture and ignore light color.')
    parser.add_argument('-t', '--texture-size', default='2048,2048',
                        help=u'Change texture size less equal than this size. (-t 512,512)')
    parser.add_argument('-f', '--force', action='store_true', help=u'Overwrite file if already exists same file.')
    parser.add_argument('-V', '--version', action='version', version=app_name())
    opt = parser.parse_args([src, '-f'])

    path = opt.path
    print(path)

    # vrm読み込み
    vrm = load(path)
    print_stat(vrm.gltf)
    print( '-' * 30 )
    vrm.gltf = reduce_vroid(vrm.gltf, opt.replace_shade_color, parse_texture_size(opt.texture_size), opt.emissive_color)

    print( '-' * 30 )
    print_stat(vrm.gltf)
    
    save_path = join(dirname(path), 'result_' + basename(path))

    # vrm保存
    vrm.save(save_path)
    print( 'saved.' )

    return fileName

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
    src = os.path.join(UPLOAD_FOLDER, fileName)
    dst = os.path.join(UPLOAD_FOLDER, 'result_' + fileName)
    file.save(src)
    # 変換
    downloadName = convert_vrm(src, dst, saveFileName)
    return send_file(dst, \
        as_attachment = True, \
        download_name = downloadName, \
        mimetype = 'application/octet-stream')

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
