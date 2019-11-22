#!/usr/bin/env python
# coding: utf-8

# ## pairDataTest
# test function for pairData

# # Function "modify One"
# 
# ## Input
# * WA codefilename, include path, string
# * OK codefilename, include path, string
# * testcases directory (testDir in this directory should follows the requirement of naiveSolution2 (string) 
# * tmp Directory, include path, string
# 
# 
# ## Running Condition
# * run for modNum=1
# * timeforRunOneTestcase=2(sec)
# * testcaseLimit=0 (no limit)
# 
# 
# ## Output
# * whether success or not (result code), integer, (0 for success, 1 for not-found, 2 for timeout, 3 for no testcases)
# * wrong code itself, string
# * modified code itself, string
# * original ok code itself, string
# * the size of vscm list, integer
# * which item is substitute (vscmIndex), list(integer)
# * which lines are substituted list(integer)
# * running time, integer(second)
# * human solving time, integer(second)
# * running iteration count, integer
# 

# In[1]:


import findVarError2
import os
import sys


# In[2]:


def modifyOne(wacodeFname, okcodeFname, tcDir, tmpDir):
    _modNum=1
    _singleTestTimeout=2
    _testcaseLimit=1000
    _debugPrint=True
    _totalTimeout=600
    
    waCFname_fnameOnly = os.path.basename(wacodeFname)
    
    
    modified_src, modified_linNums, used_vscmIndices, return_status, result_codes, elapsed_time, valid_moditer_count, vscm_length = findVarError2.naiveSolution2(
        tcDir,
        os.path.dirname(wacodeFname),
        tmpDir,
        os.path.basename(wacodeFname),
        modNumLimit=_modNum, 
        singleTestTimeout=_singleTestTimeout, 
        testcaseLimit=_testcaseLimit,
        debugPrint=_debugPrint,
        totalTimeout=_totalTimeout
    )
    
    with open(okcodeFname, 'r') as okf:
        ok_src = okf.read()
    with open(wacodeFname, 'r') as waf:
        wa_src = waf.read()
        
    
    wacodeFnameBase = os.path.basename(wacodeFname)
    okcodeFnameBase = os.path.basename(okcodeFname)
    wacodeTime = int(wacodeFnameBase[:(-6)])
    okcodeTime = int(okcodeFnameBase[:(-6)])
    human_solving_time = okcodeTime - wacodeTime
    
    return return_status, wa_src, modified_src, ok_src, vscm_length, used_vscmIndices, modified_linNums, elapsed_time, human_solving_time, valid_moditer_count


# In[3]:


# GET FILENAMES, CONTEST-NAMES, QUESTION-NAMES

# pairData directory (unzip of pairData4)
# length 52 is come from the common prefixes '_newdisk_autofix_get-codeforce_src_diff_.._.._datas_' in pairData directory.
pairDataDir = '/home/ubuntu/workspace/pyws/modifyCpp/pairData'
pdDirnames = next(os.walk(pairDataDir))[1]
pdDirnamesBaseSplitted = list(map(lambda x: os.path.basename(x)[52:].split('_'), pdDirnames))
pdDirContestStr = [x[0] for x in pdDirnamesBaseSplitted]
pdDirQuestionStr = [x[-1] for x in pdDirnamesBaseSplitted]

pdDirnamesFull = [os.path.join(pairDataDir, x) for x in pdDirnames]
pdFilenames = [next(os.walk(x))[2] for x in pdDirnamesFull]

pdOKFilenames = [list(filter(lambda k: 'OK' in k, x))[0] for x in pdFilenames]
pdWAFilenames = [list(filter(lambda k: 'WA' in k, x))[0] for x in pdFilenames]

# check the soundness of 'pdOKFilenames', 'pdWAFilenames'.
#for x in pdOKFilenames:
#    if 'OK' not in x:
#        print('ERROR: pairDataTest.py :: pdOKFilenames test failed. Filename: ' + x)
#        pdOKFilenames = []
#        break
#for x in pdWAFilenames:
#    if 'WA' not in x:
#        print('ERROR: pairDataTest.py :: pdWAFilenames test failed. Filename: ' + x)
#        pdWAFilenames = []
#        break

pdOKFilenamesFull = [os.path.join(dnf, okf) for dnf, okf in zip(pdDirnamesFull, pdOKFilenames)]
pdWAFilenamesFull = [os.path.join(dnf, waf) for dnf, waf in zip(pdDirnamesFull, pdWAFilenames)]


# In[4]:


### inputs
# - contestStr (string)
# - questionStr (string)

### output with multiple values 
# - result code (0: normal, 1: path not found, 2: no testcases in path)
# - path to appropriate testcase directory (string)

def findTC(contestStr, questionStr):
    basePath = '/home/ubuntu/workspace/pyws/getTestcases/outputs'
    contestTCPath = os.path.join(basePath, contestStr)
    questionTCPath = os.path.join(contestTCPath, questionStr)
    
    resultCode = 0
    if not os.path.isdir(questionTCPath):
        resultCode = 1
    elif len(next(os.walk(os.path.join(questionTCPath, 'input')))[2]) < 1:
        resultCode = 2
    
    return resultCode, questionTCPath
    


# # Function "runAll"
#  Wrapper for multiple execution of the function `modifyOne`

# In[5]:


import time

def runAll(logFilename, tmpDir, logDir, runningStatusPrint=True, partialRunLimit=10):
    summary_fnames = []
    summary_return_status = []
    summary_human_solving_time = []
    summary_running_time = []
    summary_vscm_length = []
    summary_valid_moditer_count = []
    
    runningStatusCount = 0
    startTime = time.time()
    return_status = -1
    valid_moditer_count = -1
    if runningStatusPrint:
        print('runAll : dbg: # of W/A codes: ', len(pdDirContestStr))
    for cnstr, qsstr, okfn, wafn in zip(pdDirContestStr, pdDirQuestionStr, pdOKFilenamesFull, pdWAFilenamesFull):
        runningStatusCount += 1
        if runningStatusCount > partialRunLimit:
            print('runAll : dbg: for-loop: reach at partialRunLimit=', partialRunLimit)
            break
        
        if runningStatusPrint and True:  #(runningStatusCount % 10 == 1):
            print('\nrunAll : dbg: for-loop: loop #', str(runningStatusCount), ' in ', str(len(pdDirContestStr)))
            print('||  contest  : ', cnstr)
            print('||  question : ', qsstr)
            print('||  wrong-answer filename : ', wafn)
            print('||  ok-answer    filename : ', okfn)
            
            #print('||  lastrun return_status code: ', str(return_status))
            #print('||  lastrun valid_moditer_count: ', str(valid_moditer_count))
            #print('||  current elapsed time: ', str(time.time() - startTime))
        ftc_rc, qtc_path = findTC(cnstr, qsstr)
        
        # outputs in one loop
        # - contest_str, string
        # - question_str, string
        # - wa_fn, string
        # - ok_fn, string
        # * modifyOne
        #   - return_status, int
        #   - vscm_length, int
        #   - modified_linNums, list(int)
        #   - running_time, int
        #   - human_solving_time, int
        #   - valid_moditer_count, int
        #   - wrong_src, string
        #   - modified_src, string
        #   - ok_src, string
        
        contest_str = cnstr
        question_str = qsstr
        wa_fn = wafn
        ok_fn = okfn        
        
        if ftc_rc == 0:
            print('runAll : dbg: this W/A code has testcases.')
            return_status, wrong_src, modified_src, ok_src, vscm_length, used_vscmIndices, modified_linNums, running_time, human_solving_time, valid_moditer_count = modifyOne(
                wafn,
                okfn,
                qtc_path,
                tmpDir
            )
        else:
            print('runAll : dbg: this W/A code has no testcases.')
            continue  
            
        if runningStatusPrint:
            print('runAll : dbg: modifyOne FINISHED')
            
        sys.stdout.flush()
            
        # write output in loop
        fname = contest_str + '_' + question_str + '_modified_' + os.path.basename(wa_fn)
        fname_full = os.path.join(logDir, fname)
        with open(fname_full, 'w') as logfile:
            logfile.write(contest_str + '\n')
            logfile.write(question_str + '\n')
            logfile.write(wa_fn + '\n')
            logfile.write(ok_fn + '\n')
            logfile.write(str(return_status) + '\n')
            logfile.write(str(vscm_length) + '\n')
            logfile.write(str(modified_linNums) + '\n')
            logfile.write(str(running_time) + '\n')
            logfile.write(str(human_solving_time) + '\n')
            logfile.write(str(valid_moditer_count) + '\n')
            logfile.write('\n' + wrong_src + '\n')
            logfile.write('\n' + modified_src + '\n')
            logfile.write('\n' + ok_src + '\n')
        
        summary_fnames.append(fname)
        summary_return_status.append(return_status)
        summary_human_solving_time.append(human_solving_time)
        summary_running_time.append(running_time)
        summary_vscm_length.append(vscm_length)
        summary_valid_moditer_count.append(valid_moditer_count)
        
    # write summary
    rs_0_count = 0
    hst_sum = 0
    rt_sum = 0
    vl_sum = 0
    vmc_sum = 0
    for i, c in enumerate(summary_return_status):
        if c == 0:
            rs_0_count += 1
            hst_sum += summary_human_solving_time[i]
            rt_sum += summary_running_time[i]
            vl_sum += summary_vscm_length[i]
            vmc_sum += summary_valid_moditer_count[i]
    
    with open(os.path.join(logDir, logFilename), 'w') as logfile:
        logfile.write('<SUMMARY LOG>\n')
        if rs_0_count != 0:
            logfile.write('returnStatus_0_count: ' + str(rs_0_count) + '\n')
            logfile.write('human_solving_time_avg: ' + str(hst_sum / rs_0_count) + '\n')
            logfile.write('running_time_avg: ' + str(rt_sum / rs_0_count) + '\n')
            logfile.write('vscm_length_avg: ' + str(vl_sum / rs_0_count) + '\n')
            logifle.write('iterCount_avg: ' + str(vmc_sum / rs_0_count) + '\n')
        else:
            logfile.write('returnStatus_0_count is ZERO\n')
        
        logfile.write('\n<DETAIL LOG>\n')
        logfile.write('\nLOG_FILE_NAMES\n')
        logfile.write(str(summary_fnames))
        logifle.write('\nRETURN STATUS\n')
        logfile.write(str(summary_return_status))
        logfile.write('\nHUMAN_SOLVING_TIMES\n')
        logfile.write(str(summary_human_solving_time))
        logfile.write('\nRUNNING_TIMES\n')
        logfile.write(str(summary_running_time))
        logfile.write('\nVSCM_LENGTH\n')
        logfile.write(str(summary_vscm_length))
        logfile.write('\nVALID_MODITER_COUNT\n')
        logfile.write(str(summary_valid_moditer_count))
        logfile.write('\n')
        


# # RUN

# In[ ]:


runFlag = True
logFilename = 'aaaaaa_log.log'
tmpDir = '/home/ubuntu/workspace/pyws/runTestTmpDir'
logDir = '/home/ubuntu/workspace/pyws/runTestLogDir'
runningStatusPrint = True
partialRunLimit=10

# JUPYTER VER
#runAll(logFilename, tmpDir, logDir, runningStatusPrint, partialRunLimit)

# FILE-OUTPUT VER
import sys
old_stdout = sys.stdout
with open('jupyterlog.log', 'w') as stdFile:
    sys.stdout = stdFile
    runAll(logFilename, tmpDir, logDir, runningStatusPrint, partialRunLimit)
sys.stdout = old_stdout


# In[ ]:




