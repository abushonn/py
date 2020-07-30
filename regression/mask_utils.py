import pandas as pd

def handle_test_masking(df_test_set, test_masking_option):
    '''
    transform df_test_set based on test_masking_option:
    'ORIGINAL': keep the original examples in column 'example'
    'MASKED': examples are in 'example_masked' column
    :param df_test_set: pandas.DataFrame containing columns ['example', 'example_masked', 'intent']
    :param test_masking_option:
    :return: pandas.DataFrame containing columns ['example', 'intent']
    '''

    if test_masking_option == 'ORIGINAL':
        df_orig = df_test_set.copy()
        # drop the 'example_masked' column
        df_orig.drop(['example_masked'], axis=1, inplace=True)
        return df_orig
    elif test_masking_option == 'MASKED':
        df_masked = df_test_set.copy()
        # drop the 'example' column, and rename 'example_masked' to 'example'
        df_masked.drop(['example'], axis=1, inplace=True)
        df_masked.rename(index=str, columns={'example_masked': 'example'}, inplace=True)
        return df_masked
    else:
        print('ERROR: Test masking option ' + test_masking_option + ' not recognized')
        exit(1)


def handle_train_masking(df_training_set, train_masking_option):
    '''
    transform df_training_set based on train_masking_option:
    'ORIGINAL' : keep the original examples in column 'example'
    'MASKED': examples are in 'example_masked' column
    'ORIGINAL_AND_MASKED': put in 'example' column the union of the original and masked examples
    :param df_training_set: pandas.DataFrame containing columns ['example', 'example_masked', 'intent']
    :param train_masking_option:
    :return: pandas.DataFrame containing columns ['example', 'intent']
    '''

    # original
    df_orig = df_training_set.copy()
    # drop the 'example_masked' column
    df_orig.drop(['example_masked'], axis = 1, inplace = True)

    # masked
    df_masked = df_training_set.copy()
    # drop the 'example' column, and rename 'example_masked' to 'example'
    df_masked.drop(['example'], axis = 1, inplace = True)
    df_masked.rename(index=str, columns={'example_masked': 'example'}, inplace=True)

    # union
    df_union = pd.concat([df_orig, df_masked], ignore_index = True).drop_duplicates().reset_index(drop = True)
    # examples to lower case, then remove duplicates again
    # TODO: keep original example case. model after code in load_intents.py
    df_union['example'] = df_union['example'].str.lower()
    df_union = df_union.drop_duplicates().reset_index(drop = True)

    if train_masking_option == 'ORIGINAL':
        df_out = df_orig
    elif train_masking_option == 'MASKED':
        df_out = df_masked
    elif train_masking_option == 'ORIGINAL_AND_MASKED':
        df_out = df_union
    else:
        print('ERROR: Train masking option ' + train_masking_option + ' not recognized')
        exit(1)

    # remove empty or whitespace-only examples (e.g. all-masked, when masking strings are omitted)
    filter = df_out['example'].str.contains('^\s*$')
    df_out = df_out[~filter]

    return df_out
