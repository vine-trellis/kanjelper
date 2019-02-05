from decimal_encoder import DecimalEncoder
import json


def putToTable(table, payload):
    table = dynamodb.Table(table)
    response = table.put_item(Item=payload)

    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

if __name__ == "__main__":
    import boto3
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
    putToTable('Kanji', {'kanji': '研究室', 'junk': [1,2,3]})
