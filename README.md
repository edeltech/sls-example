You will implement an AWS Lambda function using the Serverless Framework capable of applying a Sepia filter to an image.


# Setup

**Requirements**

- [Node](https://nodejs.org/en/download/) 6 or higher
- [Python](https://www.python.org/downloads/) 3.6 or higher
- [ImageMagick](https://imagemagick.org/script/download.php)


Install the Serverless framework

	$ npm install -g serverless

Create a directory where you want to run the example

	$ mkdir sls-example

Navigate into the directory and create a Python virtual environment

	$ cd sls-example
	$ python3 -m venv .venv

Activate the virtual environment

	$ source .venv/bin/activate

Create a Python requirements file

	$ echo "Wand==0.5.9" > requirements.txt

Install the Python dependencies

	$ pip install -r requirements.txt


# Create the serverless application

We will create a serverless application using the `aws-python3` runtime.

	$ serverless create --template aws-python3

You should now see 2 files:

1. `handler.py` - this is the application "main" function
1. `serverless.yml` - this is the serverless configuration YAML file

The `aws-python3` will create a template for Python 3.8. If you have a lower version, modify the `serverless.yml` file:

```yaml
provider:
  name: aws
  runtime: python3.7
```

## Test

	$ serverless invoke local --function hello

This will execute the function on your machine and should return:

	{
	    "statusCode": 200,
	    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {}}"
	}

# Assignment

Load an image from an URL and use the `Pillow` library to apply an effect and return the image. Because a Lambda function can only return

> **Pillow Image Filter module reference**
>
> https://pillow.readthedocs.io/en/3.0.x/reference/ImageFilter.html

## Test

	$

## Deploy to AWS

	$ serverless deploy

