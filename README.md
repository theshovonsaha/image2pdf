# Image to PDF Conversion REST API Service

This is a Python backend service that exposes a REST API for converting an image to a PDF file. It uses the Pillow library for image processing and does not use ReportLab for PDF generation.

## Usage

To use the service, you can either run it locally on your machine or deploy it to a server. To run it locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone git@github.com:theshovonsaha/image2pdf.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the service:

   ```bash
   python convert.py
   ```

   This will start the service and listen for HTTP requests on port 5000.

4. Send a POST request to the `/convert` endpoint with an image file attached:

   ```css
   curl -X POST -F file=@image.jpg http://localhost:5000/convert --output image.pdf
   ```

   This command sends a POST request to `http://localhost:5000/convert` with the `image.jpg` file attached, and saves the resulting PDF file as `image.pdf`.

   Note that the `file` parameter in the request must match the name of the file input field in the HTML form or API endpoint.

## API Documentation

### `POST /convert`

Convert an image to a PDF file.

#### Request

Method: POST
URL: /convert
Headers:
Content-Type: multipart/form-data
Form Data:
file: The image file to convert (required)

#### Response

Status Code: 200 OK
Headers:
Content-Type: application/pdf
Body: The PDF file as binary data

#### Error Responses

If the request is invalid or the service encounters an error, it will return an appropriate error response with a JSON body.

400 Bad Request
Body: {'error': 'No file provided'}

500 Internal Server Error
Body: {'error': '<error message>'}

## License

This code is licensed under the MIT License. Feel free to use it, modify it, and distribute it as you wish.
