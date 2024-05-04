import boto3
from botocore.exceptions import ClientError
import json
from decimal import Decimal

aws_region = 'us-east-1'
dynamodb_table = 'jobmatchtable'

dynamodb = boto3.resource('dynamodb', region_name=aws_region)
table = dynamodb.Table(dynamodb_table)

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
        # Extract the job ID from the query parameters
        job_id = event.get('queryStringParameters', {}).get('job_id')

        if not job_id:
            return {
                'statusCode': 400,
                'body': 'Missing or invalid "job_id" parameter in the request.'
            }

        # Query DynamoDB for records based on the job ID
        response = table.get_item(
            Key={'JobmatchID': job_id}
        )

        item = response.get('Item', None)
        
        if not item:
            return {
                'statusCode': 404,
                'body': 'No job description found with the provided ID.'
            }

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Content-Type': 'application/json',
            },
            'body': json.dumps(item, cls=DecimalEncoder)
        }

    except ClientError as e:
        # Handle DynamoDB errors
        return {
            'statusCode': 500,
            'body': f"Error retrieving data from DynamoDB: {str(e)}"
        }

    except Exception as e:
        # Handle other unexpected errors
        return {
            'statusCode': 500,
            'body': f"An unexpected error occurred: {str(e)}"
        }
