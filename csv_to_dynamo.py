import os
import boto3
import csv
import json
from concurrent.futures import ThreadPoolExecutor

def lambda_handler(event, context):
    aws_region = 'us-east-1'
    record_list = []
    
    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb', region_name=aws_region) 
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print('Bucket', bucket_name, "Key", key)
        
        csv_file = s3.get_object(Bucket=bucket_name, Key=key)
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        csv_reader = csv.reader(record_list, delimiter=',', quotechar="'")
        
        next(csv_reader, None)
        
        for row in csv_reader:
            item = {
                "Job Id": {'N': row[0]},  # Convert scientific notation to string representation
                "Experience": {'S': row[1]},  # Using row[1]
                "Qualifications": {'S': row[2]},
                "Salary Range": {'S': row[3]},
                "location": {'S': row[4]},  # Using row[4]
                "Country": {'S': row[5]},  # Using row[5]
                "latitude": {'N': row[6]},  # Using row[6]
                "longitude": {'N': row[7]},  # Using row[7]
                "Work Type": {'S': row[8]},  # Using row[8]
                "Company Size": {'N': row[9]},  # Using row[9]
                "Job Posting Date": {'S': row[10]},  # Using row[10]
                "Preference": {'S': row[11]},  # Using row[11]
                "Contact Person": {'S': row[12]},  # Using row[12]
                "Contact": {'S': row[13]},  # Using row[13]
                "Job Title": {'S': row[14]},  # Using row[14]
                "Role": {'S': row[15]},  # Using row[15]
                "Job Portal": {'S': row[16]},  # Using row[16]
                "Job Description": {'S': row[17]},  # Using row[17]
                "Benefits": {'S': row[18]},  # Using row[18]
                "skills": {'S': row[19]},  # Using row[19]
                "Responsibilities": {'S': row[20]},  # Using row[20]
                "Company": {'S': row[21]},  # Using row[21]
            }

            add_to_db = dynamodb.put_item(
                TableName="jobmatch_info",
                Item=item
            )
            print("Successfully added the record", row[0])     
            
    except Exception as e:
        print(f"An error occurred: {e}")

    return {
        'statusCode': 200,
        'body': 'Data added to DynamoDB successfully!'
    }
