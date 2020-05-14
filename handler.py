import json
import random
import boto3

def build_response(message):
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": message
            }
        }
    }

random_work_response = ['I work as a software engineer.', 'I do coding.', 'I am a programmer.']
about_me = ['I am Upen.', 'People call me Upen.', 'I am Upen from Nepal.', 'I am a chat machine.']

def hello(event, context):
    current_intent = event['currentIntent']
    intent_name = current_intent['name']

    if "Greeting" == intent_name:
        return build_response('Hi there, welcome to the world of virtual Upen! Who do I have pleasure of talking to today?')

    if "WhoAmITalkingTo" == intent_name:
        name = current_intent['slots']['name']
        return build_response('Nice to meet you {}. What do you want to know about me today?'.format(name)) 

    if "CurrentWork" == intent_name:
        return build_response(random.choice(random_work_response))

    if "Experience" == intent_name:
        return build_response('Here are my latest experiences \n 1. Software Engineer - Change Healthcare - 2017:Present')

    if "AboutMe" == intent_name:
        return build_response(random.choice(about_me))

