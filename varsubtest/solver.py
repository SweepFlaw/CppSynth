import os

from setting import *
from modifyCode import readVscm, modCodesFull
from makeVscm import genVscm
from modifyVscm import applyNNResult
from findVarError2 import codeTest, findVarErr2




def readTC(inputTCDir, outputTCDir):
    inputTestcases = []
    outputTestcases = []
    for i in range(1, TCNUM_LIMIT):
        fn = str(i)
        try:
            with open(os.path.join(inputTCDir, fn), 'rb') as itcf:
                with open(os.path.join(outputTCDir, fn), 'rb') as otcf:
                    inputTestcases.append(itcf.read())
                    outputTestcases.append(otcf.read())
        except IOError:
            break
    return inputTestcases, outputTestcases


# outputs: multiple values.
# - multiple values returned from findVarErr2 function.
# - (-2)th return value: VSCM Modifier's recommendation list length (integer)
# - (-1)th return value: the length of vscm (integer)
def makeSolution(codeFilename, inputTCDir, outputTCDir):
    
    # set default return value
    recNum = 0
    
    # make code string list
    with open(codeFilename, 'r') as codefile:
        code = codefile.readlines()
        
    # read Testcases
    inputTestcases, outputTestcases = readTC(inputTCDir, outputTCDir)
    
    # make and read vscm
    genVscm(codeFilename, VSCM_FILENAME)
    vscm = sorted(readVscm(VSCM_FILENAME), key=lambda x: (x['targetLine'], x['targetColumn'], x['targetStr']))
    
    # before run, check whether W/A code pass the testcases
    mergedCode = ''.join(code)
    trc, rc = codeTest(
        mergedCode, 
        MODIFIEDSRC_FILENAME, 
        COMPILED_FILENAME, 
        inputTestcases, 
        outputTestcases,
        SINGLE_TIMEOUT,
        stopFast=STOP_FAST
    )
    if trc == 0:
        if DEBUG_PRINT:
            print('naiveSolution2 : dbg: findVarErr2 FINISHED')
            print('||  Result Status Code : 0-success, 1-answerNotFound 2-totalTimeout 3-TCNotFound 4-PASSTC')
            print('||  Result Status : ', 4)
            print('||  This Wrong-Answer code passes all Testcases')
            sys.stdout.flush()
            return (mergedCode, [], [], 4, rc, 0, 0, recNum, len(vscm))
    
    # modify vscm using position-learning
    if POSLEARN_APPLY:
        vscm, recNum = applyNNResult(vscm, codeFilename, DEBUG_PRINT)
    
    # run!
    src, linNums, vscmIndices, rs, rcs, etime, vIterNum = findVarErr2(code, vscm, MODIFIEDSRC_FILENAME, COMPILED_FILENAME, MOD_LIMIT, inputTestcases, outputTestcases, SINGLE_TIMEOUT, TOTAL_TIMEOUT)
    if DEBUG_PRINT:
        print('naiveSolution2 : dbg: findVarErr2 FINISHED')
        print('||  Result Status Code : 0-success, 1-answerNotFound 2-totalTimeout 3-TCNotFound 4-PASSTC')
        print('||  Result Status : ', rs)
        print('||  Elapsed Time : ', etime)
        print('||  Modified Line Numbers : ', linNums)
        sys.stdout.flush()
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
    return src, linNums, vscmIndices, rs, rcs, etime, vIterNum, recNum, len(vscm)
