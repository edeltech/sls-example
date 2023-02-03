import requests
import base64

from PIL import Image
from io import BytesIO


def get_image(event, context):
    # get image url from input context
    defaut_image_url = 'https://atlantis.nyc3.digitaloceanspaces.com/styled/72025f140f22a3eb32950bbb9d76e68d'
    image_url = event.get('queryStringParameters', {}).get('url', defaut_image_url)

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
