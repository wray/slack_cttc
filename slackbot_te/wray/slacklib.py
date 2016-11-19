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

def open():
    return shelve.open('topics')

def save_topic(topic):
    topics = open()
    if not topics.has_key(topic):
        topics[topic] = ()
        topics.close()
        return topic
    else:
        return None

def all_topics():
    topics = open()
    topics_str = str(topics)
    topics.close()
    return topics_str

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
        ti = command.find(':')
        topic = command[ti+1:].strip()
        ret = save_topic(topic)
        response = (ret + " added.") if ret else (topic + " already in there.")
        

    elif command.find(COMMAND5) >= 0:
        response = all_topics()
        


    return response

