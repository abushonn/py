from watson_developer_cloud import AssistantV1
import json
import time
import mask_utils


def create_workspace(assistant, name, description):

    response = assistant.create_workspace(
        name=name,
        description=description
    ).get_result()

    print(json.dumps(response, indent=2))
    return response

def set_intents(assistant, workspace_id, intents):

    # # intent 1
    # example1 = {'text': 'going shopping'}
    # example2 = {'text': 'lets go shopping'}
    # intent1 = {'intent': 'shopping',
    #            'examples': [example1, example2]
    #            }
    #
    # # intent 2
    # example1 = {'text': 'time for games'}
    # example2 = {'text': 'wanna play?'}
    # intent2 = {'intent': 'playing',
    #            'examples': [example1, example2]
    #            }
    # intents = [intent1, intent2]

    response = assistant.update_workspace(
        workspace_id=workspace_id,
        intents=intents
    ).get_result()

    print(json.dumps(response, indent=2))
    return response

def delete_workspace(assistant, workspace_id):
    response = assistant.delete_workspace(
        workspace_id=workspace_id
    ).get_result()

    print(json.dumps(response, indent=2))
    return response

def get_workspace_status(assistant, workspace_id):
    response = assistant.get_workspace(
        workspace_id=workspace_id
    ).get_result()

    print(json.dumps(response, indent=2))
    return response['status']

def wait_until_status_available(assistant, workspace_id, delta):
    sleep_time = 10 # seconds
    start_time = time.time() # time in seconds
    status = ''
    elapsed = 0
    while(elapsed < delta):
        status = get_workspace_status(assistant, workspace_id)
        if status == 'Available':
            break
        time.sleep(sleep_time)
        now = time.time()
        elapsed = now - start_time

    return status, elapsed

def get_assistant(url, version, username, password):
    assistant = AssistantV1(
        version=version,
        username=username,
        password=password,
        url=url
    )

    return assistant

def create_wa_intents(df):
    """
    generate a list of intents, containing their examples, for training Watson Assistant
    :param df: pandas.DataFrame with columns "example", "intent"
    :return: list(dict)
    """
    grouped = df.groupby('intent')
    intents = []
    for name, group in grouped:
        examples = []
        for index, row in group.iterrows():
            examples.append({'text': row["example"]})
        intents.append({'intent': name, 'examples': examples})

    return intents

def train(df_training_set, config):
    '''
    Create intents data structure, create a WA workspace and submit the intents
    Handlind masking: train on (1) original only, (2) masked only, (3) original+masked
    :param df_training_set:
    :param wa_params:
    :return:
    '''
    df_training_set = mask_utils.handle_train_masking(df_training_set, config['masking_options']['train'])
    training_set_intents = create_wa_intents(df_training_set)

    assistant = get_assistant(config['wa']['url'], config['wa']['version'], config['wa']['username'],
                              config['wa']['password'])
    workspace_name = config['wa']['workspace_name']
    workspace_desc = config['wa']['workspace_descr']
    response = create_workspace(assistant, workspace_name, workspace_desc)
    workspace_id = response['workspace_id']
    set_intents(assistant, workspace_id, training_set_intents)
    status, elapsed = wait_until_status_available(assistant, workspace_id, config['wa']['max_wait'])

    if status != 'Available':
        print('ERROR: WA workspace status is ' + status + ' after waiting ' + str(elapsed) + ' seconds')
        print('workspace ID: ' + workspace_id)
        exit(1)
    else:
        print('WA workspace ' + workspace_id + ' is Available')

    return assistant, workspace_id


if __name__ == "__main__":
    print('__main__ :: workspace.py')
