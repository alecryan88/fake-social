import faker
import yaml
import time
from events import events
from aws import dynamo_db

#Load config as yaml -> dict
config = open('config.yml', 'r')
config_yml = yaml.safe_load(config)

#Instantiate faker class
fake = faker.Faker(use_weighting=True, locale='en')

#Create a user class
user = events.User(fake, config_yml)

#Create a signup evnent
signup = user.create_account()

#Create dynamodb instance
db = dynamo_db.DynamoDB()

#Connect to sign uptable
signup_table = db.get_table('signups')

while True: 
    
    #Calculates daily cadence for creating fake events
    cadence = 86400 / config_yml['metrics']['signups']
    time.sleep(cadence)

    #Create a signup evnent
    signup = user.create_account()

    #Insert signup into table
    db.insert_into_table('signups', signup_table)