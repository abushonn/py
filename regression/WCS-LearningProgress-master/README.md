# WCS-LearningProgress

This script runs a test set of questions agains a Watson Conversation Service
instance and reports the intents that were matched.

The script can be used for

1. *Regression testing* to check if WCS still correctly maps questions to question intents after changes have been made.
2. *Track continuous improvement* of the WCS system against a blind set of random questions.
3. *Learning automation* by mapping new question examples to an appropriate intent to feed back into training.
4. *Confusion detection* by identifying existing question examples that might have a more appropriate intent they should be mapped to.

## Input and Output Files

Before you can run this code, make sure you have the following files in the data directory
under where the script wcs_tester.py exists.

- data/wcs_test_questions.xlsx - this is the file that includes the utterances you would like to test
- data/wcs_test_results.xlsx

Example question and result files for testing whether the right answers are returned are also in the data directory.  To use these, rename them to wcs_test_questions.xlsx and wcs_test_results.xlsx.

### wcs_test_questions

The "TestQuestions" sheet needs to contain the following column headings (in any order) on the first row:

- *Reference*: Numeric ID or any other piece of text for each row that should be copied to the results (Optional).
- *Question Text*: Text of the user question you want to test.
- *Intent*: Which intent it is expected to classify to (can be blank).
- *Entity Name*: Name of entity that should be matched on the input (can be blank).
- *Entity Value*: Value of entity that should be matched on the input (can be blank).
- *Status*: This is copied to the results.  All rows are tested, regardless of status (Optional).
- *Scope*: It's used for adding predefined prefixes to the intent, but at the moment you would need to edit global variables in the python script to suit your needs (Optional).
- *Expected Answer*: For regression testing of a chat script you can include the text of the expected answer (Optional). Multiple answers in the output text array are concatenated with a space.

In order to use this code, please select a certain number of questions (say 250)
at random from the collected questions and paste them in the TestQuestions
worksheet of the data/wcs_test_questions.xlsx file.

#### Log Extractor (less relevant for WAfHB use-cases)

If you already have a WCS workspace that is being tested or used in production, you may wish to
pull logs from that workspace for testing purposes.  The wcs_log_extracter.py script can be used
to pull a single conversation or a datetime range of chat logs into a CSV file in a format ready
for use by the Tester.

`python wcs_log_extracter.py <username> <password> <workspace_id> <conversation_id>`

or

`python wcs_log_extracter.py <username> <password> <workspace_id> <start_date_time> <end_date_time>`

The output log data will be fould in `./data/WCS_Logging.csv`.
Just copy the output from this file into you wcs_test_questions spreadsheet.

### wcs_test_results

The "WCS Results" sheet needs to reserve the columns A to Z for receiving the data output from
the python script.  Columns AA onwards can be used for your own calculations, and other sheets
can be added to this spreadsheet for charts and result statistics.  See the *Summary* tab in
the wcs_test_results.xlsx spreadsheet for an example.

If you are running at the end of each test cycle, be sure to create a copy of the updated
wcs_test_results.xlsx file and rename the copy to a standard name of your choice such as
wcs_test_results_sprint1.xlsx.  You will require the Results.xlsx file for future runs if you
are tracking continuous improvement.

- *Top Result*:
  - **True Positive** means the expected intent had the top confidence and wasn't irrelevant.
  - **True Negative** means there was no intent expected and the top confidence was irrelevant.
  - **False Positive** means an unexpected intent was the top match.
  - **False Negative** means there was an expected intent but the top confidence was irrelevant.
- *Top 5*: The expected intent was in the 5 intents listed.
- *Confusion*: This is an indication of whether the top 3 returned intents are similar in confidence.
- *Recommendation*: Based on the results, this is a suggestion for how to treat this example row.
  - **Include** - This example matches the expected intent, but was not highly confident / unconfident /  => the example is candidate to be added for WA taining set
  - **Train** - This example did NOT match the expected intent, maybe the other intent is a better match => need to evaluate the confusion. If the other intent is a better match consider adding this example to WA training set
  - **Irrelevant** - No intent seems to match this example. => need to evaluate the result
- *Recommended Intent*: Most likely intent this example needs to train.

**Note**: Ignore *Top Result* and *Top 5* when testing new collected data because the Intent
column from the Test Questions sheet will not be filled in for any row, so every result will
be *False Positive* and *FALSE*.

## To Run

### Requirements

1. python (3 or later)
2. Python installation Packager (pip)
3. Openpyxl
4. xlrd
5. Watson developer cloud

python
pip install -r requirements.txt

### Execution

Run this code in your local Command Line Tool (Terminal for Macs or Command
Prompt for Windows).  Make sure to substitute in your own Watson Conversation Service credentials.

`python wcs_tester.py <username> <password> <workspace>`

**username** is `apikey`

**Note**: Large files of questions can take a long time to execute.

**Also note**: Each question tested will equate to one call of the message API for Watson Conversation Service.  Frequent testing may add up to a lot of API calls and could equate to a large bill for the account.

### What this tool can do

This tool can suggest the intent to map to for new training data sets.  You should review each
suggestion rather than blindly accepting them, as some could be not what you are after.

This tool can help identify questions mapped to two different intents (1st and 2nd intents have
confidence 100%).  It can also highlight where there is a lot of confusion for a group of intents,
which may indicate a lot of overlapping training examples that need to be moved to different intents.

This tool can suggest alternate intents to map to (either 1st intent has confidence less than
90%, or 2nd intent has confidence more than 80%).

This tool can also help identify overtraining.  To do that you would need to train up
a workspace on a random selection of question examples (80% of all examples for instance) and look
for any results where examples that were excluded from training (the other 20%) still matched the
right intent at over 95% confidence.  Those "Very Accurate" rows could be excluded from the final training.

This tool can calculate *precision* and *recall* for a test set.  See the charts in the example
results sheet for an example.

This tool can regression test chat scripts to ensure all answers were as expected.
