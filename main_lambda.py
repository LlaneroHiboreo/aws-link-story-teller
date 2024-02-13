import boto3
import json

def lambda_handler(event,context):
    # Initialize boto3 clients
    bedrock_client = boto3.client('bedrock')
    s3_client = boto3.client('s3')

    # retrive method used and body
    method = event['requestContext']['http']['method']
    requestPayload = event['body']

    # Operated based on method
    if (method=='GET') and valid_json():
        # get path and parse it
        raw_path = event['rawPath']
        path = raw_path.split('/')
        print(path)
        
        return {
            'statusCode':200,
            'body':json.dumps('hello from lambda')
        }

    else:
        return {
            'statusCode':400,
            'body':json.dumps('Bad method used')
        }


def valid_json(body):
    try:
        json.loads(body)
    except ValueError as e:
        return False
    return True