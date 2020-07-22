
import os
import json
import time
import pandas as pd
import subprocess
from shutil import copyfile


from watson_developer_cloud import AssistantV1

from watson_developer_cloud import AssistantV1

import json

WA_MAX_WAIT = 300 # seconds

def wa_get_assistant(url, version, username, password):
    assistant = AssistantV1(
        version=version,
        username=username,
        password=password,
        url=url
    )

    return assistant

def wa_create_workspace(assistant, name, description):

    response = assistant.create_workspace(
        name=name,
        description=description
    ).get_result()

    # print(json.dumps(response, indent=2))
    return response

def wa_set_intents(assistant, workspace_id, intents):
    '''
    # intent 1
    example1 = {'text': 'going shopping'}
    example2 = {'text': 'lets go shopping'}
    intent1 = {'intent': 'shopping',
               'examples': [example1, example2]
               }

    # intent 2
    example1 = {'text': 'time for games'}
    example2 = {'text': 'wanna play?'}
    intent2 = {'intent': 'playing',
               'examples': [example1, example2]
               }
    intents = [intent1, intent2]
    '''

    response = assistant.update_workspace(
        workspace_id=workspace_id,
        intents=intents
    ).get_result()

    # print(json.dumps(response, indent=2))
    return response

def wa_send_user_input(assistant, workspace_id, input_text):
    response = assistant.message(
        workspace_id = workspace_id,
        input={
            'text': input_text
        }
    ).get_result()

    # print(json.dumps(response, indent=2))
    return response



def wa_get_workspace_status(assistant, workspace_id):
    response = assistant.get_workspace(
        workspace_id=workspace_id
    ).get_result()

    print(json.dumps(response, indent=2))
    return response['status']

def wa_wait_until_status_available(assistant, workspace_id):
    sleep_time = 10 # seconds
    start_time = time.time() # time in seconds
    status = ''
    elapsed = 0
    while(elapsed < WA_MAX_WAIT):
        status = wa_get_workspace_status(assistant, workspace_id)
        if status == 'Available':
            break
        time.sleep(sleep_time)
        now = time.time()
        elapsed = now - start_time

    return status, elapsed


if __name__ == "__main__":
    print('main wa_communication !!!')