import boto3
import json
from decimal import Decimal

# Initialize Boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jobmatchtable')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
        # Scan the DynamoDB table to retrieve all items (job descriptions)
        response = table.scan()

        # Extract the items from the response
        items = response.get('Items', [])

        # Return the items as the response body, using custom Decimal encoder
        return {
            'statusCode': 200,
            'body': json.dumps(items, cls=DecimalEncoder)
        }

    except Exception as e:
        # Handle any unexpected errors
        return {
            'statusCode': 500,
            'body': f"An unexpected error occurred: {str(e)}"
        }
