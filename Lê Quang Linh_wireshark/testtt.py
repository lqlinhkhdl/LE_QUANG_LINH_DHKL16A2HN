import boto3
from botocore.client import Config

s3 = boto3.client('s3',
    endpoint_url='http://172.20.10.3:9000',
    aws_access_key_id='student01',
    aws_secret_access_key='abc12345',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1')
s3.download_file('test', 'Data_LeQuangLinh_061.csv')
print("Download thành công!")
