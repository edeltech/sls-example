You will implement an AWS Lambda function using the Serverless Framework capable of modifying an image.


# Setup

**Requirements**

- [NPM](https://nodejs.org/en/download/) 16 or higher
- [Python](https://www.python.org/downloads/) 3.6 or higher


Install the Serverless framework

	$ npm install -g serverless

Clone this repository

	$ git clone git@github.com:edeltech/sls-example.git

Navigate into the directory and create a Python virtual environment

	$ cd sls-example

## Deploy

	$ serverless deploy

## Invoke

	$ serverless invoke --function process_image --path event.json

This will execute the function in the cloud and return the response. If all goes well, we should see a base64-encoder image. 

