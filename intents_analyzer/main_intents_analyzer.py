from wa_communication import *

import os
import json
import pandas as pd
import subprocess
from shutil import copyfile
from intents import *
from text_words import *


workspace_id =''


def read_config(config_file_name):
    with open(config_file_name) as f:
        config = json.load(f)
    return config


def setup_wa_workspace(assistant, workspace_name, workspace_desc, intents):
    # assistant = wa_get_assistant(config['wa']['url'], config['wa']['version'], config['wa']['username'], config['wa']['password'])
    response = wa_create_workspace(assistant, workspace_name, workspace_desc)
    workspace_id = response['workspace_id']

    wa_set_intents(assistant, workspace_id, intents)

    wa_set_intents(assistant, workspace_id, intents)
    # status, elapsed = wa_wait_until_status_available(assistant, workspace_id)

    print('================= Added intents to workspace_id = ' + workspace_id)
    print(intents)

    #
    # wa_send_user_input(assistant, workspace_id, 'Do you want to play?')
    #
    # print('================= Send user input [Do you want to play?] to wa space id  = ' + workspace_id)

    return 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def get_text_intent(assistant, workspace_id, input_text):
    response = wa_send_user_input(assistant, workspace_id, input_text)
    ''' 
    intents is a list like:   [{'intent': 'playing', 'confidence': 0.95}, {'intent': 'shopping', 'confidence': 0.05}]
    '''
    intents = response['intents']

    '''
    intents[0] is an intent, like {'intent': 'playing', 'confidence': 0.95}
    '''
    if (len(intents) >0):
        #print('intent %s'%(intents[0]['intent']))
        print(' %s :: %s'%(input_text, (intents[0]['intent']) + ' :: ' +str(intents[0]['confidence']) ))
    else:
        print('%s :: %s' % (input_text, 'INTENT_NOT_FOUND'))


def get_intents_for_list_of_utterances(assistant, workspace_id, file_of_utterances):
    with open(file_of_utterances) as f:
        lines = f.readlines()
        for ll in lines:
            '''rstrip() is needed to remove newlines in each line'''
            get_text_intent(assistant, workspace_id, ll.rstrip())


if __name__ == "__main__":

    config_file_name = 'config.gitignore.json'
    config = read_config(config_file_name)

    assistant = wa_get_assistant(config['wa']['url'], config['wa']['version'], config['wa']['username'],
                                 config['wa']['password'])

    ''' ================= Init WA Workspace ================='''
    # setup_wa_workspace(assistant, '01 Yan Test WA Skill', 'auto-generated', test_intents)

    #workspace_id = '8c47515b-9aef-4f6c-9274-215a71e2bcf6' #<--------------------------
    # CORE
    # workspace_id = 'e82583d8-debb-4ef6-97eb-a2a8aef4233c'
    workspace_id = '6c5c69dd-b3b1-4ec8-9a0d-e82e7c16f645' #yan test
    # Welltok
    #workspace_id = '3962dbf1-2be8-47b3-8fff-75eab61a0566'

    ''' ================= Test intents for a single utterance  ================='''
    #get_text_intent(assistant, workspace_id, 'can i meet my deductible with copays?')

    ''' ================= Test intents for a file with list of utterance  ================='''
    IN_FILE = 'welltok-utter-s14.txt'
    get_intents_for_list_of_utterances(assistant, workspace_id, IN_FILE)






