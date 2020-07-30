# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
This script pulls chat logs from Watson Conversation Service / Watson Assistant
and puts them into a csv file.

You can either pull logs for a single conversation or for a date range.

Usage: wcs_log_extractor.py username password workspace_id conversation_id
Usage: wcs_log_extractor.py username password workspace_id start_date_time end_date_time

The format of the produced CSV file is intended for use with the wcs_tester.py script,
but you will need to copy the file content into Excel to use it.

This python script requires:
1. python 3
2. Python installation Packager (pip)
5. Watson developer cloud

Copyright: IBM
Version: 0.2
Last updated on: 13/06/2018
'''
import warnings
import csv, os, re
import datetime, sys
from watson_developer_cloud import ConversationV1

'''------------------------------------------------------------------'''
''' Following are a set of global variables. '''

#api_version = "2017-05-26"
api_version = "2018-02-16"

data_dir = "./data"
output_file = "WCS_Logging.csv"

title_qid = "Reference"
title_question = "Question Text"
title_intent = "Intent"
title_entityname = "Entity Name"
title_entityvalue = "Entity Value"
title_status = "Status"
title_inscope = "Scope"
title_answer = "Expected Answer"
answer_bubble_separator = " "

col_qid = None
col_question = None
col_intent = None
col_entityname = None
col_entityvalue = None
col_inscope = None
col_status = None
col_answer = None


'''------------------------------------------------------------------'''
''' Utility functions. '''

def strip_non_ascii(string):
    ''' This cleans the questions variable of any non-ascii characters such as
    smart apostrophes and en-dashes '''

    # Strip question of non-ascii characters
    stripped = (c for c in string if 0<ord(c)<127)
    # return question stripped of non-ascii characters.
    return ''.join(stripped)


def api_call():
    ''' This function makes the api call by sending the question to WCS and
    getting a response which is stored in the variable classes.'''

    conversation = ConversationV1(username = sys.argv[1],
                                  password = sys.argv[2],
                                  version = api_version)
    workspace_id = sys.argv[3]

    if len(sys.argv) == 5:
        return conversation.list_logs(workspace_id = workspace_id,
                                        filter = "response.context.conversation_id::" + sys.argv[4],
                                        sort = "request_timestamp",
                                        page_limit = 500)
    else:
        return conversation.list_logs(workspace_id = workspace_id,
                                        filter = "request_timestamp>=" + sys.argv[4] + ",request_timestamp<=" + sys.argv[5],
                                        sort = "request_timestamp",
                                        page_limit = 10000)



'''------------------------------------------------------------------'''


def main():
    ''' Pull logs into a CSV file. '''

    if len(sys.argv) <= 4:
        print ('usage: wcs_tester.py <username> <password> <workspace_id> <conversation_id>')
        print ('usage: wcs_tester.py <username> <password> <workspace_id> <start_date_time> <end_date_time>')
        sys.exit

    # Create a csv file by the name WCS_Mapping.csv
    outputFile = open(data_dir + "/" + output_file, "w+", newline='')
    # Call csv writer module and assign it the variable f
    f = csv.writer(outputFile)

    # Now write the column header line in the csv file.
    f.writerow([title_question, title_intent, title_entityname, title_entityvalue, title_answer])

    log_data = api_call()

    # Loop through all the input question rows in the source spreadsheet.
    q = None
    i = None
    et = None
    ev = None
    a = None

    for item in log_data.get("logs"):

        print ("Processing row " + str(item))

        q = item.get("request").get("input").get("text")
        try:
            i = item.get("response").get("intents")[0].get("intent")
        except:
            i = ""
        # With entities, how do we know which of the many entities is significant???
        # Should we return them all???
        # Should we give up?
        try:
            et = item.get("response").get("entities")[0].get("entity")
        except:
            et = ""
        try:
            ev = item.get("response").get("entities")[0].get("value")
        except:
            ev = ""
        a = answer_bubble_separator.join(item.get("response").get("output").get("text"))

        # Populate the csv file with this q&a row.

        f.writerow ([ q, i, et, ev, a])

    # Close the created CSV file.
    outputFile.close()

    print ("Done! You can now check " + data_dir + "/" + output_file + " for the output results.")
    return

if __name__ == '__main__':
    main()
