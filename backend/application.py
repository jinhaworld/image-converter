from flask import Flask, request, send_file, make_response
application = Flask(__name__)
from PIL import Image
from io import BytesIO
from image_process import *

@application.route('/', methods=['GET'])

def test():
    return 'Hello, World!'

@application.route('/upload', methods=['POST'])

def upload():
    f = request.files['image_file']

    # Open the received file into Image format 
    img = Image.open(f)
    
    # Process the image into color-blind suitable image
    converted_image = convert_pixel(open_image(img))

    # Return the processed image as a response
    img_io = BytesIO()
    img.save(img_io, 'jpeg')
    img_io.seek(0)

    response = make_response(send_file(img_io, mimetype='image/jpeg'))
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

