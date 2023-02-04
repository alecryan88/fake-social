import faker
import yaml
import time
import users
from aws.dynamodb import dynamo_db
import random

#Load config as yaml -> dict
config = open('config.yml', 'r')
config_yml = yaml.safe_load(config)

#Instantiate faker class
fake = faker.Faker(use_weighting=True, locale='en')

#Create a user class
user = users.User(fake, config_yml)

#Create dynamodb instance
db = dynamo_db.DynamoDB()

while True:
    #Set duration counter to 0
    duration = 0

    #Connect to signups table & sessions table
    signup_table = db.get_table('signups')
    sessions_table = db.get_table('sessions')

    #Scan entire signup table for all users eligible for session every ~60 sec
    eligible_users = db.dump_table(signup_table)

    while duration <= 60:
        
        #Calculates daily cadence for creating fake events
        cadence =  86400 / config_yml['metrics']['sessions']
        time.sleep(cadence)
        
        #Extracts signup user_id from list of eligible users if there are any
        
        user_data = random.choice(eligible_users)
        user_id = user_data['user_id']

        #Create a session_start evnent
        session_start = user.create_session_start(user_id)

        #Increment the duration by the cadence
        duration += cadence

        #Remove user that is currently in a session
        eligible_users.remove(user_data)

        #Inserts session start into dynamo table
        db.insert_into_table(sessions_table, session_start)

        #Updates session eligibility in signup table
        db.update_session_eligible(user_id, signup_table)

        print(duration)

        print(session_start)