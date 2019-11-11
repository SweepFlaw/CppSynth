#!/usr/bin/env python
# coding: utf-8

# In[65]:


import subprocess
import time

import modifyCode


# In[66]:


# input:
#   - code (string)
#   - tmpFilename (string)
#   - cFilename (string) (compiled file name)
#   - inputTestcases (list(bytes))
#   - outputTestcases (list(bytes))
#   - singleTestTimeout (int)
#   - stopFast (bool, optional) (if stopFast true, return immediately when the test fails)
# output:
#   - totalResultCode (0 for success. 1 for testcase error. 2 for compile error.)
#   - resultCode for each testcases (list(int)) (0 for success. 1 for W/A. 2 for timeout. 3 for other runtime errors.)
def codeTest(code, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout, stopFast=True):
    # put code into file
    with open(tmpFilename, 'w') as file:
        file.write(code)
    # compile
    p = subprocess.run(['g++', tmpFilename, '-o', cFilename], shell=False)
    if p.returncode != 0:
        return (2, [])
    
    # run testcases
    totalResultCode = 0
    resultCodes = []
    for i, o in zip(inputTestcases, outputTestcases):
        try:
            p = subprocess.run([cFilename], stdin=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=singleTestTimeout)
        except TimeoutExpired:
            totalResultCode = 1
            resultCodes.append(2)
            if stopFast:
                return totalResultCode, resultCodes
            else:
                continue
        except _:
            totalResultCode = 1
            resultCodes.append(3)
            if stopFast:
                return totalResultCode, resultCodes
            else:
                continue
        if o == p.stdout:
            resultCodes.append(0)
        else:
            resultCodes.append(1)
            if stopFast:
                return totalResultCode, resultCodes
    return totalResultCode, resultCodes


# In[67]:


# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - tmpFilename (string)
#   - cFilename (string)
#   - inputTestcases (list(bytes))
#   - outputTestcases (list(bytes))
#   - singleTestTimeout (represent timeout seconds.)
#   - totalTimeout (represent timeout seconds. int, optional)  (non-positive value for no-limit)
# output: multiple return values.
#   - modified code String (string) (If it fails to find, return '')
#   - modified codeline Index, start from 0 (int)
#   - returnStatus(int) (0 for success, 1 for not-found, 2 for timeout)
#   - elapsed time (int) (seconds)
def findVarErr(code, vscm, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout, totalTimeout=0):
    startTime = time.time()
    timeout = startTime + totalTimeout
    for i, v in enumerate(vscm):
        if totalTimeout != 0 and time.time() > timeout:
            return ('', (-1), 2, (time.time() - startTime))
        mc, mci, rs = modCodeFull(code, vscm, i)
        if rs != 0:
            continue
        trc, rcs = codeTest(mc, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout)
        if trc == 0:
            return (mc, mci, 0, (time.time() - startTime))
        #print('debug information - findVarErr: ', trc, rcs)
    return ('', (-1), 1, (time.time() - startTime))
        


# ## Naive Solver

# In[68]:


### NAIVE SOLUTION
# expected directory layout
# testDir
# - codefname
# - input
#   - 1.txt
#   - 2.txt
#   - ...
# - output
#   - 1.txt
#   - 2.txt
#   - ...

import os
from modifyCode import readVscm, modCodeFull
from makeVscm import genVscm

def naiveSolution(testDir, codefname, singleTestTimeout=2, testcaseLimit=1000):
    # set filenames
    codeFilename = os.path.join(testDir, codefname)
    vscmFilename = os.path.join(testDir, 'vscm.csv')
    tmpFilename = os.path.join(testDir, 'tmpFile.cpp')
    cFilename = os.path.join(testDir, 'cfile.out')
    inputTCDir = os.path.join(testDir, 'input')
    outputTCDir = os.path.join(testDir, 'output')
    
    # make code string list
    with open(codeFilename, 'r') as codefile:
        code = codefile.readlines()
    
    # make and read vscm
    genVscm(codeFilename, vscmFilename)
    vscm = readVscm(vscmFilename)
    
    # read testcases
    inputTestcases = []
    outputTestcases = []
    for i in range(testcaseLimit):
        fn = str(i) + '.txt'
        try:
            with open(os.path.join(inputTCDir, fn)) as itcf:
                with open(os.path.join(outputTCDir, fn)) as otcf:
                    inputTestcases.append(itcf.read())
                    outputTestcases.append(otcf.read())
        except IOError:
            break
    
    # run!
    src, ind, rs, etime = findVarErr(code, vscm, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout)
    print('====================================== SRC')
    print(src)
    print('====================================== RS')
    print(rs)
    print('====================================== ELAPSED TIME')
    print(etime)
    return rs
    


# ## TEST

# In[73]:


TEST_FLAG=False


# In[74]:


# run naiveSolution
if TEST_FLAG:
    testDir = '/home/ubuntu/workspace/pyws/modifyCpp/naiveSolverTestDir/test1'
    codefname = 'code.cpp'

    naiveSolution(testDir, codefname)


# In[ ]:




