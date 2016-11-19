import random
import json
import urllib3
import shelve

import temp_humidity
#import led

COMMAND1 = "who are you"
COMMAND2 = "what can you do"
COMMAND3 = "temp"
#COMMAND4 = "name an animal"
#COMMAND5 = "green led"
COMMAND4 = "topic:"
COMMAND5 = "topics"

def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I am a simpleton bot."
    elif command.find(COMMAND2) >= 0:
        response = "Not much right now... waiting for you to teach me."
    elif command.find(COMMAND3) >= 0:
        try:
            temp_c,temp,humidity = temp_humidity.read_temp_humidity()
            response = "At my location, the temperature is " + str(temp) + " and the relative humidity is " + str(humidity)
        except:
            response = "At my location, there is a sensor malfunction."

    elif command.find(COMMAND4) >= 0:
        command = command.encode('utf-8')
        topics = shelve.open('topics')
        ti = command.find(':')
        topic = command[ti+1:].strip()
        if not topics.has_key(topic):
            topics[topic] = 0
            response = topic + " added."
        else:
            response = topic + " already exists."

    elif command.find(COMMAND5) >= 0:
        response = str(shelve.open('topics'))


    return response

