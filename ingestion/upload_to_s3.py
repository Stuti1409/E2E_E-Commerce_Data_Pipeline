import boto3

s3 = boto3.client('s3')

file_name = "orders.csv"
bucket_name = ""

s3.upload_file(file_name, bucket_name, file_name)
print("File uploaded to s3")