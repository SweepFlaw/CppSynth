import os
import sys

### TEST SETTING, IMPORTANT
LOWER_CLOSED_415_LIMIT = 4 
UPPER_OPENED_415_LIMIT = 5 
TEST_POSLEARN_APPLY = True
LOGFILENAME = 'summary_iter_999.log'


### PROJECT DIRECTORIES
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, 'data')
BIN_DIR = os.path.join(CURRENT_DIR, 'bin')
LOG_DIR = os.path.join(CURRENT_DIR, 'log')
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
PROBLEM_DIR = os.path.join(DATA_DIR, 'pairData_415')
TC_DIR = os.path.join(DATA_DIR, 'cftestcase')

### RNN PRIORITY CALCULATOR ("https://github.com/SweepFlaw/position-learning")
POSLEARN_APPLY = TEST_POSLEARN_APPLY
POSLEARN_PROJ_DIR = '/home/ubuntu/workspace/pyws/position-learning'
POSLEARN_APPFILE = os.path.join(POSLEARN_PROJ_DIR, 'app.py')

### VSCM (variable-substitution-candidate-map)
# to compile vscm source, see "https://github.com/SweepFlaw/VarSubsCandListGenCpp"
VSCM_GENERATOR_BINARY = os.path.join(BIN_DIR, 'vscm')
VSCM_MAIN_OPTION = 0
VSCM_SELECT_MODE = 2

### Test Setting
TOTAL_TIMEOUT=1200
SINGLE_TIMEOUT=2
MOD_LIMIT=1
DEBUG_PRINT=True
TCNUM_LIMIT = 200
STOP_FAST=True
HUMANTIME_UPPER_LIMIT=7200


### Temporary Filenames
VSCM_FILENAME = os.path.join(TMP_DIR, 'vscm.csv')
MODIFIEDSRC_FILENAME = os.path.join(TMP_DIR, 'modified_src.cpp')
COMPILED_FILENAME = os.path.join(TMP_DIR, 'compiled.out')

### Lof Filename
SUMMARY_LOGFILENAME = os.path.join(LOG_DIR, LOGFILENAME)
