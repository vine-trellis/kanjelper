import boto3


dynamodb = boto3.resource('dynamodb', region_name='dan-region', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Kanji2')

table.delete()
