import json
import boto3

# Get the service resource and instantiate a table resource object
dydbTable = boto3.resource('dynamodb').Table('PropertyBasic')

def lambda_handler(event, context):
    # Extract the 'pid' parameter from the query string parameters
    pid = event["queryStringParameters"]["pid"]

    # Delete the item from the DynamoDB table
    dydbTable.delete_item(
        Key={
            "pid": pid
        }
    )
    
    # Create the response body
    body = {"result": "The property is deleted"}
   
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(body)
    }