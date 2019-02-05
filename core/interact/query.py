from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

def queryTable(table, kanji):
    table = dynamodb.Table(table)
    response = table.query(
        KeyConditionExpression=Key('kanji').eq(kanji)
    )

    for i in response['Items']:
        print(i['kanji'], ":", i['data'])
    return response['Items'][0]

if __name__ == "__main__":
    queryTable('Kanji', '発音')
