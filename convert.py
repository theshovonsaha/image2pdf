from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_image_to_pdf():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    with Image.open(file) as im:
        
        pdf_file = io.BytesIO()
        im.save(pdf_file, format='PDF')
        pdf_file.seek(0)

        return pdf_file.read(), 200, {'Content-Type': 'application/pdf'}

if __name__ == '__main__':
    app.run()
