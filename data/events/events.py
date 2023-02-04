import random
import time
from datetime import datetime


class User:

    def __init__(self, fake, config_yml):
        ''' Initialize the users class by parsing yml config and inheriting faker object'''
        self.genders = config_yml['dimensions']['genders']
        self.platforms = config_yml['dimensions']['platforms']
        self.signups = config_yml['metrics']['signups']
        self.sessions = config_yml['metrics']['sessions']

        #faker class
        self.fake = fake
        

    def get_gender(self):
        '''Takes list of genders specified in config.yml and sets random gender and name as attributes'''
    
        self.gender = random.choice(self.genders)
        
        if self.gender == 'm':
            self.name = self.fake.name_male()
        elif self.gender == 'f':
            self.name = self.fake.name_female()
        else:
            self.name = self.fake.name_nonbinary()

        

    def get_platform(self):
        '''Takes list of platforms specified in config.yml and sets platform token as attributes'''

        self.platform = random.choice(self.platforms)
        if self.platform == 'android':
            self.platform_token = self.fake.android_platform_token()
        else:
            self.platform_token = self.fake.ios_platform_token()
                

    def create_account(self):
        '''Creates a new account and returns a dict'''

        self.get_gender()

        self.get_platform()
            
        account = {
            'user_id' : str(self.fake.random_number(fix_len=True, digits=9)),
            'gender': self.gender,
            'name' : self.name,
            'platform_token' : self.platform_token,
            'country' : self.fake.country(),
            'latitude' : str(self.fake.latitude()),
            'longitude' : str(self.fake.longitude()),
            'email' : self.fake.email(),
            'date_of_birth': self.fake.date_of_birth().strftime('%Y-%m-%d'),
            'signed_up_at': int(time.time()),
            'session_eligible': True
        }

        print(account)
        return account 

    
    def create_session_start(self, user_id):
        '''Creates a session start event from a dictionary containing user data.'''
        
        session = {
            'session_id': self.fake.uuid4(),
            'session_start_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': user_id

        }

        return session
