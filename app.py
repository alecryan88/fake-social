import sys
import time
import random
from datetime import datetime

event = {
            'session_id':'1234',
            'session_start_at':int(time.time()),
            'user_id': '8085268'

        }


def handler(event=None, context=None):
    #Generate random session duration
    duration = random.randint(1, 300)

    #Sleep for that duration to mimic an actual session
    #time.sleep(duration)

    #Decorate the session_start event with an end and duration event
    event['session_end'] = int(time.time()) + duration
    event['duration'] = duration

    return event

print(handler(event))