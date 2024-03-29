#!/usr/bin/env python
# coding: utf-8

# In[115]:



from makeVscm import genVscm


# In[116]:


# input: targetFilename(string)
# output: entireFile String line by line (list(string))
def readTargetFile(targetFilename):
    with open(targetFilename, 'r') as file:
        codeStr = file.readlines()
    return codeStr


# In[117]:


import csv

# input: vscmFilename(string)
# output: vscm = list(dictionary)
# -- dictionary layout
#    - targetLine (int)
#    - targetColumn (int)
#    - targetOffset (int)
#    - targetLength (int)
#    - targetStr (string)
#    - candidateLine (int)
#    - candidateColumn (int)
#    - candidateOffset (int)
#    - candidateLength (int)
#    - candidateStr (string)

def readVscm(vscmFilename, csvSeparator=','):
    vscm = []
    with open(vscmFilename, 'r') as csvfile:
        vscmReader = csv.reader(csvfile, delimiter=csvSeparator)
        for row in vscmReader:
            if (row[4] != 'operator>>' and row[4] != 'operator<<'
               and row[9] != 'operator>>' and row[9] != 'operator<<'):
                r = {}
                r['targetLine'] = int(row[0])
                r['targetColumn'] = int(row[1])
                r['targetOffset'] = int(row[2])
                r['targetLength'] = int(row[3])
                r['targetStr'] = row[4]
                r['candidateLine'] = int(row[5])
                r['candidateColumn'] = int(row[6])
                r['candidateOffset'] = int(row[7])
                r['candidateLength'] = int(row[8])
                r['candidateStr'] = row[9]
                vscm.append(r)
    return vscm


# In[3]:


# input: 
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndex (int)
# output: multiple return values.
#   - modified codeline String (string),
#   - modified codeline Index, start from 0 (int),
#   - returnStatus(int) (0 for success, (-1) for failure)
from copy import deepcopy

def modCode(code, vscm, vscmIndex):
    if len(vscm) < vscmIndex:
        return (code, -1, -1)
    modSpec = vscm[vscmIndex]
    lineNo = modSpec['targetLine'] - 1
    colNo = modSpec['targetColumn'] - 1
    mc = deepcopy(code[lineNo])
    front = mc[:colNo]
    end = mc[colNo + modSpec['targetLength']:]
    mc = "".join([front, modSpec['candidateStr'], end])
    return (mc, lineNo, 0)
    


# In[4]:


# function modCodeFull (make this for main functionality)
# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndex (int)
# output: multiple return values.
#   - modified whole source String (string)
#   - modified codeline Index, start from 0 (int)
#   - returnStatus(int) (0 for success, (-1) for failure)
def modCodeFull(code, vscm, vscmIndex):
    mc, mci, rs = modCode(code, vscm, vscmIndex)
    if rs != 0:
        return (code, (-1), (-1))
        
    codeFront = "".join(code[:mci])
    if mci + 1 < len(code):
        codeEnd = "".join(code[(mci + 1):])
    else:
        codeEnd = ""
    return ("".join([codeFront, mc, codeEnd]), mci, 0)


# ### Modify codes at multiple points.

# In[6]:


# input: 
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndice (list(int))
# output: multiple return values.
#   - modified codeline Strings (dict(int -> string)),
#   - modified codeline Index, start from 0 (list(int)),
#   - returnStatus(int) (0 for success, (-1) for failure, (-2) for failure)
from copy import deepcopy
import itertools

def modCodes(code, vscm, vscmIndice):
    # check if vscmIndex is valid index
    for vscmindex in vscmIndice:
        if len(vscm) < vscmindex:
            return ({}, [], -1)
        
    modSpecs = [{'lineNo': vscm[k]['targetLine'] - 1,
                 'colNo': vscm[k]['targetColumn'] - 1,
                 'tarStr': vscm[k]['targetStr'],
                 'canStr': vscm[k]['candidateStr']
                } for k in vscmIndice]
    
    # modSpecsDict : dict(int -> list(modSpec))
    #   map the lineNumber to the subset of modSpecs.
    modSpecsDict = {}
    for ms in modSpecs:
        modSpecsDict.setdefault(ms['lineNo'], [])
        modSpecsDict[ms['lineNo']].append(ms)
    
    # msbl for mode-spec-___-list. I don't know why i named it like that.
    # check if two or more vscm indice points to the same location or 
    for k, msbl in modSpecsDict.items():
        for (spec1, spec2) in itertools.combinations(msbl, 2):
            if (spec1['colNo'] == spec2['colNo']):
            #or len(spec1['tarStr']) + spec1['colNo'] > spec2['colNo']:
                return ({}, [], -2)
        # sort lists in modSpecsDict by 'colNo' value.
        modSpecsDict[k] = sorted(msbl, key=lambda x:x['colNo'])
    
    # mcs : modified codeline Strings(dict(int -> string)), return value.
    mcs = {}
    for k, msbl in modSpecsDict.items():
        if 0 < len(msbl):
            lineNum = msbl[0]['lineNo']
            mc = deepcopy(code[lineNum])
            if len(msbl) < 2:
                msbl0 = msbl[0]
                # same as the function 'modCode'
                front = mc[:msbl0['colNo']]
                end = mc[msbl0['colNo'] + len(msbl0['tarStr']):]
                mc = "".join([front, msbl0['canStr'], end])
                mcs[lineNum] = mc
            else:
                cc = []
                cc.append(mc[:(msbl[0]['colNo'])])
                for i in range(0, len(msbl)-1):
                    cc.append(msbl[i]['canStr'])
                    start = msbl[i]['colNo'] + len(msbl[i]['tarStr'])
                    end = msbl[i+1]['colNo']
                    cc.append(mc[start:end])
                cc.append(msbl[-1]['canStr'])
                start = msbl[-1]['colNo'] + len(msbl[-1]['tarStr'])
                cc.append(mc[start:])
                mcs[lineNum] = ''.join(cc)
        else:
            pass
    
    return (mcs, [k for (k,v) in modSpecsDict.items()], 0)


# In[2]:


# function modCodesFull
# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndice (list(int))
# output: multiple return values.
#   - modified whole source String (string)
#   - modified codeline Index, start from 0 (list(int))
#   - returnStatus(int) (0 for success, (-1) for failure, (-2) for failure)
def modCodesFull(code, vscm, vscmIndice):
    mcs, mcis, rs = modCodes(code, vscm, vscmIndice)
    if rs != 0:
        return (code, [], rs)
       
    mcsList = []
    for i in range(0, len(code)):
        if i in mcis:
            mcsList.append(mcs[i])
        else:
            mcsList.append(code[i])
    return (''.join(mcsList), mcis, 0)


# In[ ]:





# ## MAIN

# In[3]:


# run main function (code for command-line interface)
import sys

# argv[1]: targetCppSourcePath (string)
# argv[2]: vscmOutputFilePath (string)
# argv[3]: vscmIndexNum (int)
# standard output:
#   If the modifying process done well,
#     this prints out modifiedCode whole string.
#   If not, prints nothing.
def mainFunc (tcsp, vofp, vscmIndexNum):
    genVscm(tcsp, vofp)
    code = readTargetFile(tcsp)
    vscm = readVscm(vofp)
    mcode, mci, rs = modCodeFull(code, vscm, vscmIndexNum)
    if rs == 0:
        print(mcode)

if __name__ == '__main__':
    if(len(sys.argv) > 3):
        mainFunc(sys.argv[1], sys.argv[2], int(sys.argv[3]))


# ## TEST

# In[4]:


# TEST FLAG
TEST_FLAG = False


# In[5]:


# run main function (code for jupyter interface)
import os

if TEST_FLAG:
    # readTargetFile test
    #tc_fn = '/home/ubuntu/workspace/VarSubsCandListGenCpp/test/tc.cpp'
    #print(readTargetFile(tc_fn))
    
    # readVscm test
    #vscm_fn = '/home/ubuntu/workspace/VarSubsCandListGenCpp/test/log6.txt'
    #vscm_test = readVscm(vscm_fn)
    #print(vscm_test)
    
    # modCode test
    #code_test = readTargetFile(tc_fn)
    #vscm_test = readVscm(vscm_fn)
    #print("MODIFICATION:")
    #vscm_index_test = 3
    #print(vscm_test[vscm_index_test])
    #modedstr_test, modedLine_test, returnStatus_test = modCode(code_test, vscm_test, vscm_index_test)
    #print("BEFORE:")
    #print(code_test[modedLine_test])
    #print("AFTER:")
    #print(modedstr_test)
    
    # mainFunc test
    #print(mainFunc(tc_fn, vscm_fn, 1))
    pass
    


# In[ ]:





# In[ ]:





# In[ ]:




