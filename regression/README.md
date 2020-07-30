# Regression tools

In this directory we have 2 main tools:
1. **eval** - that is used for regressino testing (e.g. evaluation of the current classifiers)- it uses k-fold validations. see more detail below.
2. **wcs_tester** - under the sub-folder `WCS-LearningProgress-master` - it used to test new examples against an existing workspace. The eval script above also use it


## Regression Testing for Intent Classification

Code is located at `/WFBWCSWorkspaces/src/python/regression`.
The instructions below refer to this location as [regression home].

## Running

In a command line window (before you run please configure as deseribed below)
cd [regression home]
python eval.py

## Results

Folder location: [regression home]/results

Result files:

1. wcs_test_results_[X].xlsx : results of one of the 5 cross-validation folds. [X] runs from 0 to 4.
2. details.csv : results of all 5 folds combined. Includes a row for each training example.
3. stats.csv : performance statistics of the 5 folds.
4. summary.csv: statistic summary of the 5 folds, in format: median [min-max]
5. 'Effectiveness Notebook WFB.html': Watson Assistant Effectiveness Notebook (customized to WFB).
6. intent-level statistics for all intents (computed by WA Effectiveness Notebook):
    - WorstPrecisionIntents.csv
    - WorstRecallIntents.csv
    - WorstOverallIntents.csv
    - ConfusedIntentPairs.csv

## Comparing Results

Module module compare.py is used to display the regression trend, comparing visually two or more runs.
Save the entire [regression home]/results folder at a separate location, and append the date in format yyyy-mm-dd. For example: results_2019-05-23.
The last 10 characters (the date) will be used for display.
To create the trend figure:
edit "main" at bottom of compare.py:

1. Set dirpath to point to the location where you placed your results subfolders.
2. Edit run_dirnames to include a list of the runs you want to compare.

Then run:
python compare.py

Last runs are stored at Box under:
Watson for Benefit - Haifa Development Zone / IntentClassification / regression
<https://ibm.box.com/s/s1x45eusvikq9jywnefdzp85of5ujus1>

## Configuration

[regression home]/config.json contains all configuration parameters:

- "masking_options": determine how masked examples are used in training and testing phases.
Valid values for "train": ['ORIGINAL', 'MASKED', 'ORIGINAL_AND_MASKED']
Valid values for "test": ['ORIGINAL', 'MASKED']

- "wa": Watson Assistant connection parameters. "max_wait" is the time (in seconds) to wait for WA to complete training  - if timed out often may need to increase it.

- "wcslp": WCS-LearningProgress parameters. This utility is used to submit a batch of test examples to WA and report results. May need to change these parameters only when updating WCS-LearningProgress version (source: <https://github.ibm.com/CanberraWatson/WCS-LearningProgress).>

- "wa_notebook": Watson Assistant Effectiveness Notebook parameters. This python notebook is used to calculate intent-level statistics. May need to change these parameters only when updating notebook version (source: <https://github.com/watson-developer-cloud/assistant-improve-recommendations-notebook/blob/master/notebook/Effectiveness%20Notebook.ipynb).>

### Python requirements

python (version 3)
pandas
watson_developer_cloud
xlrd
openpyxl
jupyter

Installation:

Step 1 below suggest using Anaconda, another approach is to use visual code studio with python plugin

1. Install the Anaconda (version 3.x) python distribution (<https://www.anaconda.com/download/)>
This will install python 3, pandas and many other packages.
NOTE - during Anaconda installation, check the "add to path" box. Should prevent issues with package import  (at least on Windows).

2. In a command line window:
cd [regression home]
pip install -r requirements.txt (in windows it will be py -m pip install -r requirements.txt)

This will install watson_developer_cloud package (not included in the Anaconda distribution)
If system can't find pip (a package management system) executable on your path, locate it at [Anaconda dir]/scripts/pip.
