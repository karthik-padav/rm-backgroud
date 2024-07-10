from flask import Flask, request, send_file
from PIL import Image
import io
import rembg

app = Flask(__name__)

@app.route("/")
def start():
    return "The MBSA Server is Running"

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return {"error": "No image file provided"}, 400
    
    file = request.files['image']
    input_image = Image.open(file.stream)

    # Use rembg to remove the background
    output_image = rembg.remove(input_image)

    # Save the output image to a BytesIO object
    img_io = io.BytesIO()
    output_image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


