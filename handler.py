import requests
import base64

from PIL import Image
from io import BytesIO


def process_image(event, context):
    # get image url from input context
    image_url = event['queryStringParameters']['url']

    # read image
    response = requests.get(image_url, stream=True)
    image = Image.open(response.raw)

    # build response body from provided image
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    body = base64.b64encode(buffer.getvalue())

    response = {
        'statusCode': 200,
        'body': body.decode('utf-8'),
        'headers': {
            'Content-Type': 'image/jpeg',
        },
        'isBase64Encoded': True
    }

    return response
