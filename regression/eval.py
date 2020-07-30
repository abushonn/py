import os
import analyze
import config_utils
import wcslp_facade

from sklearn.model_selection import StratifiedKFold
import workspace

def perform_cross_validation(config):

    cwd = os.getcwd()
    filepath = os.path.join(cwd, config['data_source']['dir_name'], config['data_source']['file_name'])
    df_intent_examples = wcslp_facade.read_intent_examples(filepath)

    # generate random folds
    skf = StratifiedKFold(n_splits = config['n_splits'], shuffle=True, random_state=0)
    folds_generator = skf.split(df_intent_examples['example'], df_intent_examples['intent'])
    folds = []
    for train_index, test_index in folds_generator:
        folds.append({'train': train_index, 'test': test_index})

    # cross-validation loop
    first_fold = 0 # default: 0 (run all folds). change this to start from the middle of a run, in case the previous run failed
    for fold_num in range(first_fold, len(folds)):
        print('Running fold ' + str(fold_num))
        train_index = folds[fold_num]['train']
        test_index = folds[fold_num]['test']
        df_training_set = df_intent_examples.loc[train_index]
        df_test_set = df_intent_examples.loc[test_index]

        # train
        wa_assistant, wa_workspace_id = workspace.train(df_training_set, config)

        # test and write test set into batch xlsx file
        wcslp_facade.write_test_set(config, df_test_set)
        # invoke wcslp on input file, as system call
        proc = wcslp_facade.run_wcslp(config, wa_workspace_id)
        if proc.returncode:
            print('ERROR running WCS-LP, return code: ' + str(proc.returncode))
            workspace.delete_workspace(wa_assistant, wa_workspace_id)
            exit(1)
        # handle output file: copy aside to another folder with iteration number in file name
        wcslp_facade.save_wcslp_results(config, fold_num)

        # cleanup
        workspace.delete_workspace(wa_assistant, wa_workspace_id)

if __name__ == "__main__":

    config_file_name = 'config.json'
    config = config_utils.read_config(config_file_name)

    perform_cross_validation(config)

    analyze.run(config)



