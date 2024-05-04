import boto3
import csv
from decimal import Decimal

# Initialize Boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('jobmatchtable')

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # S3 bucket and file details
    bucket_name = 'jobmatchdata'
    file_name = 'jobdescription_info.csv'

    # Read CSV file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    lines = response['Body'].read().decode('utf-8').splitlines()

    # Parse CSV
    chunk_size = 50

    for i in range(0, len(lines), chunk_size):
        chunk = lines[i:i + chunk_size]
        csv_reader = csv.reader(chunk)
        headers = next(csv_reader)

        # Convert CSV rows to DynamoDB items
        for row in csv_reader:
            item = {
                'JobmatchID': row[0],
                'work_year': int(row[1]),
                'experience_level': row[2],
                'employment_type': row[3],
                'job_title': row[4],
                'salary': Decimal(row[5]),
                'salary_currency': row[6],
                'salary_in_usd': Decimal(row[7]),
                'employee_residence': row[8],
                'remote_ratio': int(row[9]),
                'company_location': row[10],
                'company_size': row[11]
            }
            
            # Insert item into DynamoDB
            table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': 'Data loaded into DynamoDB table successfully!'
    }
