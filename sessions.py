
from datetime import datetime
import yaml
import boto3
import faker
from dotenv import load_dotenv
import random
import time

load_dotenv()

loader_config = open('config.yml', 'r')
loader_yaml = yaml.safe_load(loader_config)


fake = faker.Faker(
    use_weighting=True,
    locale='en')

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
            response = table.scan(
                FilterExpression=Attr('session_eligible').eq(True)
            )
        last_evaluated_key = response.get('LastEvaluatedKey')
        
        results.extend(response['Items'])
        
        if not last_evaluated_key:
            break
    return results


while True:
    duration = 0

    #Scan table every ~60 sec
    user_list = dump_table('signups')

    while duration <= 60:
    
        daily_sessions = loader_yaml['metric']['sessions']
        
        cadence = 86400 / daily_sessions 
        
        time.sleep(cadence)
        
        user_data = random.choice(user_list)
        
        session = {
            'session_id': str(fake.random_number(fix_len=True, digits=11)),
            'session_start_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': user_data['user_id']

        }

        duration += cadence

        #Remove user that is currently in a session
        user_list.remove(user_data)

        session_table.put_item(Item=session)
        signup_table.update_item(
             Key={'user_id': user_data['user_id']},
             UpdateExpression='SET session_eligible = :s',
             ExpressionAttributeValues={
                ':s': False
             }
        )

        print(duration)

        print(session)


