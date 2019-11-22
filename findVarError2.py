#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import time

import modifyCode


# In[2]:


# input:
#   - code (string)
#   - tmpFilename (string)
#   - cFilename (string) (compiled file name)
#   - inputTestcases (list(bytes))
#   - outputTestcases (list(bytes))
#   - singleTestTimeout (int)
#   - stopFast (bool, optional) (if stopFast true, return immediately when the test fails)
# output:
#   - totalResultCode (0 for success. 1 for testcase error. 2 for compile error. 3 for no testcases)
#   - resultCode for each testcases (list(int)) (0 for success. 1 for W/A. 2 for timeout. 3 for other runtime errors.)
def codeTest(code, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout, stopFast=True):
    # exceptional case : no testcases
    if len(inputTestcases) < 1:
        return (3, [])
    
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
            p = subprocess.run([cFilename], input=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=singleTestTimeout)
        except subprocess.TimeoutExpired:
            totalResultCode = 1
            resultCodes.append(2)
            if stopFast:
                return totalResultCode, resultCodes
            else:
                continue
        except:
            totalResultCode = 1
            resultCodes.append(3)
            if stopFast:
                return totalResultCode, resultCodes
            else:
                continue
        if o == p.stdout:
            resultCodes.append(0)
        else:
            totalResultCode = 1
            resultCodes.append(1)
            if stopFast:
                return totalResultCode, resultCodes
    return totalResultCode, resultCodes


# In[3]:


# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - tmpFilename (string)
#   - cFilename (string)
#   - modNum (int) (the number of modifications)
#   - inputTestcases (list(bytes))
#   - outputTestcases (list(bytes))
#   - singleTestTimeout (represent timeout seconds.)
#   - totalTimeout (represent timeout seconds. int, optional)  (non-positive value for no-limit)
#   - printDebugInfo (bool, optional)
# output: multiple return values.
#   - modified code String (string) (If it fails to find, return '')
#   - modified codeline Indices, start from 0 (list(int))
#   - selected vscmIndices for successful modification (list(int))
#   - returnStatus(int) (0 for success, 1 for not-found, 2 for timeout, 3 for no testcases)
#   - resultCodes (list(int)) (results for each testcases: following the return value of codeTest.)
#   - elapsed time (int) (seconds)
#   - valid Iterate count (int)
from itertools import combinations

def findVarErr2(code, vscm, tmpFilename, cFilename, modNum, inputTestcases, outputTestcases, singleTestTimeout, totalTimeout=0, printDebugInfo=True):
    if printDebugInfo:
        print('findVarErr2 : dbg: findVarErr2 START')
    startTime = time.time()
    
    if len(inputTestcases) < 1:
        return ('', [], [], 3, [], (time.time() - startTime), 0)
    
    timeout = startTime + totalTimeout
    validModificationCount = 0
    
    # variables for debugging
    timeCache = startTime
    
    # debugging - print the length of vscm
    if printDebugInfo:
        print('findVarErr2 : dbg: VSCM Length: ', len(vscm))
    
    for mN in range(1, modNum + 1):
        # mT for modification-tuple
        # mL for modification-list
          
        #debugging - print current mN
        if printDebugInfo:
            print('findVarErr2 : dbg: < SET mN VALUE >')
            print('||  mN = ', mN)
          
        for mT in combinations(range(len(vscm)), mN):
            # timeout check
            if totalTimeout > 0 and time.time() > timeout:
                return ('', [], [], 2, [], (time.time() - startTime), validModificationCount)
        
            # modify Code
            mc, mcis, rs = modifyCode.modCodesFull(code, vscm, mT)
            
            if rs != 0:
                continue
                
            #  test code with testcases
            trc, rcs = codeTest(mc, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout)
            
            validModificationCount += 1
            # debugging - count the number of iteration
            if printDebugInfo:
                if validModificationCount % 50 == 1:
                    print('findVarErr2 : dbg: validModificationCount = ', validModificationCount)
                    print('||  ELAPSED TIME:' + str(time.time() - timeCache))
                    timeCache = time.time()
            
            if trc == 0:
                return (mc, mcis, list(mT), 0, rcs, (time.time() - startTime), validModificationCount)
    return ('', [], [], 1, [], (time.time() - startTime), validModificationCount)
        


# ## Naive Solver

# In[4]:


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

# outputs: multiple values.
# - multiple values returned from findVarErr2 function.
# - (-1)th return value: the length of vscm (integer)

import os
from modifyCode import readVscm, modCodeFull
from makeVscm import genVscm

def naiveSolution2(testDir, codeDir, tmpDir, codefname, modNumLimit=2, singleTestTimeout=2, testcaseLimit=1000, debugPrint=True):
    if debugPrint:
        print('naiveSolution2 : dbg: naiveSolution2 START')
    
    # set filenames
    codeFilename = os.path.join(codeDir, codefname)
    vscmFilename = os.path.join(tmpDir, 'vscm.csv')
    tmpFilename = os.path.join(tmpDir, 'tmpFile.cpp')
    cFilename = os.path.join(tmpDir, 'cfile.out')
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
    for i in range(1, testcaseLimit):
        fn = str(i)
        try:
            with open(os.path.join(inputTCDir, fn), 'rb') as itcf:
                with open(os.path.join(outputTCDir, fn), 'rb') as otcf:
                    inputTestcases.append(itcf.read())
                    outputTestcases.append(otcf.read())
        except IOError:
            break
    
    # run!
    src, linNums, vscmIndices, rs, rcs, etime, vIterNum = findVarErr2(code, vscm, tmpFilename, cFilename, modNumLimit, inputTestcases, outputTestcases, singleTestTimeout)
    if debugPrint:
        print('naiveSolution2 : dbg: findVarErr2 FINISH')
        print('||  Result Status Code : 0-success, 1-answerNotFound 2-totalTimeout 3-TCNotFound')
        print('||  Result Status : ', rs)
        print('||  Elapsed Time : ', etime)
        print('||  Modified Line Numbers : ', linNums)
        #print('====================================== RESULT')
        #print('====================================== RESULT')
        #print('====================================== RESULT')
        #print('====================================== SRC')
        #print(src)
        #print('====================================== RS')
        #print(rs)
        #print('====================================== Result code for each testcases')
        #print(rcs)
        #print('====================================== VSCM Indices')
        #print(vscmIndices)
        #print('====================================== modifiedLineNum')
        #print(linNums)
        #print('====================================== ELAPSED TIME')
        #print(etime)
        #print('')
    return src, linNums, vscmIndices, rs, rcs, etime, vIterNum, len(vscm)
    


# In[ ]:





# ## TEST

# In[5]:


TEST_FLAG_1=False
TEST_FLAG_2=False


# In[6]:


# run naiveSolution
if TEST_FLAG_1:
    testDir = '/home/ubuntu/workspace/pyws/modifyCpp/naiveSolverTestDir/test1'
    codefname = 'code.cpp'

    naiveSolution2(testDir, testDir, testDir, codefname)


# In[7]:


# run naiveSolution for realistic example

if TEST_FLAG_2:
    testDir = '/home/ubuntu/workspace/pyws/modifyCpp/naiveSolverTestDir/test2'
    codefname='code.cpp'
    
    naiveSolution2(testDir, testDir, testDir, codefname, modNumLimit=1)


# In[ ]:





# In[ ]:




