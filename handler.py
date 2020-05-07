import base64

from wand.image import Image

from urllib import request


def process_image(event, context):
    # get image url from input context
    image_url = event['queryStringParameters']['url']

    # read image
    response = request.urlopen(image_url)
    image = Image(file=response)

    # save image to local in debug mode
    if event.get('debug'):
        image.save(filename='output_image.jpg')

    # build response body with the image
    image_blob = image.make_blob('jpeg')
    body = base64.b64encode(image_blob)

    response = {
        'statusCode': 200,
        'body': body.decode('utf-8'),
        'headers': {
            'Content-Type': 'image/jpeg',
        },
        'isBase64Encoded': True
    }

    return response
