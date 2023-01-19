import faker
import random
import yaml
import boto3
import time
from dotenv import load_dotenv

load_dotenv()


loader_config = open('config.yml', 'r')
loader_yaml = yaml.safe_load(loader_config)

fake = faker.Faker(
    use_weighting=True,
    locale='en')

genders = ['m', 'f', 'nb']

platforms = ['android', 'ios']

def create_account():

    gender = random.choice(genders)
    if gender == 'm':
        name = fake.name_male()
    elif gender == 'f':
        name = fake.name_female()
    else:
        name = fake.name_nonbinary()


    platform = random.choice(platforms)
    if platform == 'android':
        platform_token = fake.android_platform_token()
    else:
        platform_token = fake.ios_platform_token()
        
    account = {
        'user_id' : str(fake.random_number(fix_len=True, digits=9)),
        'gender': gender,
        'name' : name,
        'platform_token' : platform_token,
        'country' : fake.country(),
        'latitude' : str(fake.latitude()),
        'longitude' : str(fake.longitude()),
        'email' : fake.email(),
        'date_of_birth': fake.date_of_birth().strftime('%Y-%m-%d'),
        'signed_up_at': int(time.time()),
        'session_eligible': True
    }

    return account 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('signups')

while True: 
    duration = 86400 / loader_yaml['metric']['signups']
    time.sleep(duration)
    account = create_account()
    print(account)
    table.put_item(Item=account)