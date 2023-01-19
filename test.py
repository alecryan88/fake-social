
from datetime import datetime
import yaml
import boto3
import faker
from dotenv import load_dotenv
import random
import time

load_dotenv()

dynamodb = boto3.resource('dynamodb')
signup_table = dynamodb.Table('signups')
session_table = dynamodb.Table('sessions')


def dump_table(table_name):

    table = dynamodb.Table('signups')
    results = []
    last_evaluated_key = None
    while True:
        if last_evaluated_key:
            response = table.scan(
                ExclusiveStartKey=last_evaluated_key,
                FilterExpression=Attr('session_eligible').eq(True)
            )
        else: 
            response = table.scan()
        last_evaluated_key = response.get('LastEvaluatedKey')
        
        results.extend(response['Items'])
        
        if not last_evaluated_key:
            break
    return results

# Usage
data = dump_table('signups')


print(data)