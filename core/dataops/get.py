import json
from decimal_encoder import DecimalEncoder
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def getFromTable(table, key):
    table = dynamodb.Table(table)
    try:
        response = table.get_item(
            Key=key
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        try:
            item = response['Item']
            print("GetItem succeeded:")
            print(json.dumps(item, indent=4, cls=DecimalEncoder))
        except KeyError as e:
            print(str(e))
        

if __name__ == "__main__":
    import boto3
    dynamodb = boto3.resource("dynamodb", region_name='us-west-2', endpoint_url="http://localhost:8000")
    getFromTable('Kanji', {'kanji': '研究室'})
