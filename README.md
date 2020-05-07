You will implement an AWS Lambda function using the Serverless Framework capable of applying a Sepia filter to an image.


# Setup

**Requirements**

- [Node](https://nodejs.org/en/download/) 6 or higher
- [Python](https://www.python.org/downloads/) 3.6 or higher
- [ImageMagick](https://imagemagick.org/script/download.php)


Install the Serverless framework

	$ npm install -g serverless

Clone this repository

	$ git clone git@github.com:edeltech/sls-example.git

Navigate into the directory and create a Python virtual environment

	$ cd sls-example
	$ python3 -m venv .venv

Activate the virtual environment

	$ source .venv/bin/activate

Install the Python dependencies

	$ pip install -r requirements.txt


## Test

	$ serverless invoke local --function process_image --path event.json

This will execute the function on your machine and return a base64 encoded image.


# Your turn

Add an `orientation` query parameter to rotate the input image by steps of 90 degrees before returning it.

