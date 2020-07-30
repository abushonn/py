import os
from shutil import copyfile
import xlsx_editing
import subprocess

import mask_utils
import pandas as pd

def read_intent_examples(filepath):
    """
    :param filepath: path to mater copy of intent examples: a CSV file with columns ['example', 'example_masked', 'intent']
    :return:
    """
    df = pd.read_csv(filepath)
    # TODO: treat column ignore_masked. for now, omit it.
    df.drop(['ignore_masked'], axis=1, inplace=True)
    return df

def run_wcslp(config, wa_workspace_id):
    '''
    :return:
    the result of the process running WCS-LP

    '''
    # overwrite WCS-LP output file with a template file (empty),
    # since WCS-LP writes current results over previous ones and may have leftovers if previous results are longer than current.
    wcslp_templates_dirname = os.path.join(config['wcslp']['dirname'], config['wcslp']['templates_subdir_name'])
    wcslp_data_dirname = os.path.join(config['wcslp']['dirname'], config['wcslp']['data_subdir_name'])


    xlsx_editing.copy_file(wcslp_templates_dirname, config['wcslp']['output_template_filename'], wcslp_data_dirname, config['wcslp']['output_filename'])

    # run process
    cwd = os.getcwd()
    wcslp_wd = os.path.join(cwd, config['wcslp']['dirname']) # wcslp home is a subdir

    return subprocess.run(['python', config['wcslp']['main_module_name'], config['wa']['username'], config['wa']['password'], wa_workspace_id, config['wa']['url']], cwd = wcslp_wd)


def save_wcslp_results(config, run_number):
    '''
    Copy output file to the results folder, with run number added to file name
    '''
    src = os.path.join(config['wcslp']['dirname'],
                       config['wcslp']['data_subdir_name'],
                       config['wcslp']['output_filename'])
    dst = os.path.join(config['results_dirname'],
                       config['wcslp']['output_filename'].replace('.xlsx', '_' + str(run_number) + '.xlsx'))
    copyfile(src, dst)



def write_test_set(config, df_test_set):
    df_test_set = mask_utils.handle_test_masking(df_test_set, config['masking_options']['test'])

    templates_folder_name = os.path.join(config['wcslp']['dirname'], config['wcslp']['templates_subdir_name'])
    data_folder_name = os.path.join(config['wcslp']['dirname'], config['wcslp']['data_subdir_name'])

    xlsx_editing.copy_file(templates_folder_name, config['wcslp']['input_template_filename'], data_folder_name, config['wcslp']['input_filename'])
    xlsx_editing.write_intent_examples(df_test_set, os.path.join(data_folder_name, config['wcslp']['input_filename']))
