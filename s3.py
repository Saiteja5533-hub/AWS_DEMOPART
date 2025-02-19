import boto3
session = boto3.Session(
    aws_access_key_id="AKIAS74TMAZM7ZTJZUUW",
    aws_secret_access_key="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",
    region_name="US East (N. Virginia) us-east-1",
)
import os

os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAS74TMAZM7ZTJZUUW'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'   # Set the region you want

# Create a boto3 client for S3
s3_client = boto3.client('s3', region_name=region)

bucket_name = 'saitejabucket55338896'

try:
    # Create the S3 bucket
    response = s3_client.list_buckets()
    for bucket in response["Buckets"]:
     print(bucket["Name"])

except ClientError as e:
    print(f'Error creating bucket: {e}')
    import boto3
from botocore.exceptions import ClientError

region = 'us-east-1'   # Set the region you want

# Create a boto3 client for S3
s3_client = boto3.resource('s3', region_name=region)

bucket_name = 'saitejabucket55338896'

try:
    # Read the S3 bucket

# Retrieve the list of existing buckets
    for bucket in s3_client.buckets.all():
      print(bucket.name)

except ClientError as e:
    print(f'Error creating bucket: {e}')