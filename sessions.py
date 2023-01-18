
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

while True:
    duration = 0

    #Scan table every ~60 sec
    response = signup_table.scan()

    user_list = [i['user_id'] for i in response["Items"]]

    while duration <= 60:
        
        
        
        daily_sessions = loader_yaml['metric']['sessions']
        
        cadence = 86400 / daily_sessions 
        
        time.sleep(cadence)
        
        user_id = random.choice(user_list)
        
        session = {
            'session_id': str(fake.random_number(fix_len=True, digits=11)),
            'session_start_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': user_id

        }
        duration += cadence

        session_table.put_item(Item=session)

        print(duration)

        print(session)


